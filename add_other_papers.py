#!/usr/bin/env python3
"""
Add 814 papers from 'other/' primary areas to the ICLR 2026 website.
Uses Claude Sonnet API to classify each paper into one of 41 existing categories.
"""

import csv
import json
import os
import re
import time
from collections import defaultdict
from anthropic import Anthropic

# ── Config ────────────────────────────────────────────────────────────────────
OTHER_CSV_DIR = "/home/v-qinglinzhu/code/B_other/iclr/iclr26_trends_out/primary_area_split/other/"
ALL_JSON_PATH = "/home/v-qinglinzhu/code/B_other/read_paper/iclr/data/all.json"
OUTPUT_PATH = ALL_JSON_PATH  # overwrite in place
CLASSIFICATION_CACHE = "/home/v-qinglinzhu/code/B_other/read_paper/iclr/classification_cache.json"

BATCH_SIZE = 20  # papers per API call
MODEL = "claude-sonnet-4-20250514"

# Subcategory definitions from add_subcats.py (for regenerating subcats)
SUBCATS_DEFS = {
    0: [  # LLM推理与思维链
        ("数学与逻辑推理", ["math", "mathematics", "arithmetic", "logic", "symbolic", "theorem", "proof", "gsm", "aime", "competition", "olympiad"]),
        ("代码推理与程序合成", ["code", "programming", "program", "software", "execution", "python", "algorithm"]),
        ("推理过程与验证", ["process reward", "step-by-step", "verification", "verifier", "critique", "prm", "outcome reward", "orm", "reward hacking", "reasoning faithfulness", "faithful"]),
        ("思维链方法", ["chain-of-thought", "cot", "scratchpad", "rationale", "thought", "deliberate", "tree of thought", "beam search reasoning", "monte carlo"]),
        ("推理可靠性与幻觉", ["hallucination", "factual", "reliability", "consistency", "confabulation", "sycophancy", "calibration"]),
        ("多步规划与搜索", ["planning", "search", "mcts", "tree search", "beam", "lookahead", "backtracking", "explore"]),
        ("其他推理", []),
    ],
    1: [  # 扩散模型与Flow Matching
        ("Flow Matching方法", ["flow matching", "rectified flow", "optimal transport flow", "flow-based", "cnf", "normalizing flow", "continuous normalizing"]),
        ("扩散模型理论", ["score matching", "diffusion theory", "sde", "stochastic differential", "ode", "denoising score", "reverse process", "noise schedule", "ddpm", "ddim"]),
        ("文本到图像生成", ["text-to-image", "text-guided", "stable diffusion", "imagen", "dalle", "t2i"]),
        ("扩散模型应用", ["protein", "molecule", "drug", "3d generation", "point cloud", "audio diffusion", "video diffusion", "motion diffusion", "graph diffusion", "inverse problem", "image restoration", "super resolution", "inpainting"]),
        ("扩散模型加速与控制", ["accelerat", "distillation", "few step", "consistency model", "guidance", "classifier-free", "controlnet", "lora diffusion", "editing", "inversion"]),
        ("其他扩散", []),
    ],
    2: [  # LLM Agent与工具使用
        ("网络与GUI Agent", ["web", "browser", "gui", "ui", "webpage", "website", "click", "navigation", "grounding"]),
        ("代码执行Agent", ["code agent", "coding agent", "software agent", "swe", "code execution", "program agent", "coding task", "repository"]),
        ("多Agent系统", ["multi-agent", "multiagent", "agent collaboration", "agent communication", "society", "cooperative agent", "agent team"]),
        ("工具调用与函数", ["tool use", "tool call", "function call", "api", "plugin", "tool learning", "tool selection"]),
        ("Agent规划与记忆", ["planning", "task planning", "memory", "reflection", "react", "chain of action", "task decomposition"]),
        ("其他Agent", []),
    ],
    3: [  # LLM推理加速与压缩
        ("量化", ["quantization", "quantize", "int8", "int4", "bnb", "gptq", "weight quantization", "activation quantization", "post-training quantization"]),
        ("剪枝与稀疏化", ["pruning", "sparsity", "sparse", "magnitude pruning", "structured pruning"]),
        ("知识蒸馏", ["distillation", "knowledge distillation", "teacher", "student model"]),
        ("推测解码", ["speculative decoding", "speculative", "draft model", "token speculation"]),
        ("注意力与KV缓存优化", ["kv cache", "attention efficient", "linear attention", "flash attention", "paged attention", "sliding window", "long context efficient"]),
        ("其他加速", []),
    ],
    4: [  # LLM训练与预训练
        ("预训练方法与数据", ["pretraining", "pre-training", "data mixture", "corpus", "web data", "data curation", "tokenomics", "pretraining data", "data selection for"]),
        ("微调与PEFT", ["fine-tuning", "finetuning", "lora", "peft", "adapter", "prefix tuning", "full fine-tuning", "parameter efficient"]),
        ("指令遵循与对话训练", ["instruction tuning", "instruction following", "sft", "supervised fine-tuning", "chat", "conversation training", "instruction", "helpfulness"]),
        ("持续学习与遗忘", ["continual learning", "catastrophic forgetting", "lifelong", "sequential learning", "knowledge retention"]),
        ("训练稳定性与效率", ["training stability", "loss spike", "gradient", "batch size", "learning rate", "warmup", "training efficiency", "mixed precision", "distributed training"]),
        ("其他训练", []),
    ],
    6: [  # 多模态大模型
        ("视觉语言理解", ["visual question", "vqa", "image captioning", "visual reasoning", "image understanding", "visual grounding", "referring", "ocr", "chart", "document"]),
        ("视频语言模型", ["video language", "video llm", "videollm", "video understanding", "video question", "temporal reasoning", "video captioning", "videollava"]),
        ("多模态推理与空间", ["spatial", "3d understanding", "depth", "spatial reasoning", "multimodal reasoning", "geometry", "physical reasoning"]),
        ("多模态生成与编辑", ["multimodal generation", "image generation llm", "any-to-any", "unified generation", "multimodal editing", "image editing llm"]),
        ("多模态对齐与训练", ["multimodal alignment", "visual instruction", "llava", "clip", "vision encoder", "visual representation", "multimodal training"]),
        ("其他多模态", []),
    ],
    7: [  # AI安全与攻防
        ("越狱与提示注入", ["jailbreak", "prompt injection", "red team", "safety bypass", "harmful", "refusal", "toxicity"]),
        ("对抗样本与攻击", ["adversarial example", "adversarial attack", "adversarial perturbation", "evasion", "pgd", "fgsm", "adversarial training"]),
        ("后门与投毒攻击", ["backdoor", "trojan", "poisoning", "data poisoning", "supply chain"]),
        ("鲁棒性认证", ["certified robustness", "randomized smoothing", "formal verification", "lipschitz", "verification", "provable"]),
        ("模型隐私与推断攻击", ["model extraction", "model stealing", "inference attack", "gradient inversion", "model inversion"]),
        ("其他安全", []),
    ],
    12: [  # RLHF与对齐
        ("偏好学习与DPO", ["dpo", "direct preference", "preference optimization", "preference learning", "ipo", "kto", "simpo"]),
        ("奖励建模", ["reward model", "reward learning", "reward shaping", "reward signal", "process reward", "reward hacking"]),
        ("安全与价值对齐", ["safety alignment", "value alignment", "constitutional", "harmless", "helpful harmless", "safe rlhf", "red teaming alignment"]),
        ("多元偏好与价值", ["pluralistic", "diverse preference", "preference aggregation", "social choice", "democratic", "value pluralism", "group preference"]),
        ("其他对齐", []),
    ],
    35: [  # LLM评测与基准
        ("推理能力评测", ["reasoning evaluation", "reasoning benchmark", "math evaluation", "logic evaluation", "problem solving evaluation"]),
        ("多模态评测", ["multimodal evaluation", "visual benchmark", "vision language benchmark", "image benchmark", "multilingual evaluation", "video evaluation"]),
        ("LLM-as-Judge方法", ["llm-as-a-judge", "llm judge", "judge", "evaluator model", "gpt-4 judge", "auto evaluation"]),
        ("基准设计与污染", ["benchmark design", "contamination", "benchmark contamination", "data contamination", "test set", "leakage", "overfitting benchmark"]),
        ("综合能力评测", ["capability", "general evaluation", "mmlu", "hellaswag", "instruction following evaluation", "chat evaluation", "human eval"]),
        ("其他评测", []),
    ],
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_problem(explain_zh: str) -> str:
    """Extract the problem summary from explain_zh (line after '解决的问题是什么？')."""
    if not explain_zh:
        return ""
    lines = explain_zh.split("\n")
    for i, line in enumerate(lines):
        if "解决的问题是什么" in line:
            # The answer is on the next line(s), usually starts with "  - "
            for j in range(i + 1, min(i + 3, len(lines))):
                ans = lines[j].strip()
                if ans.startswith("- "):
                    ans = ans[2:].strip()
                if ans:
                    return ans
    return ""


def csv_to_paper(row: dict) -> dict:
    """Convert a CSV row to the compact paper format used in all.json."""
    r = float(row.get("avg_rating", 0) or 0)
    c = float(row.get("avg_confidence", 0) or 0)
    venue = row.get("venue", "")
    is_oral = "Oral" in venue
    # Recommended: Oral papers, or very high rating
    rec = is_oral or r >= 7.5

    return {
        "t": row.get("title", ""),
        "r": r,
        "v": venue,
        "u": row.get("openreview_url", ""),
        "k": row.get("keywords", ""),
        "a": row.get("primary_area", ""),
        "c": c,
        "p": extract_problem(row.get("explain_zh", "")),
        "rec": rec,
        "ab": row.get("abstract", ""),
        "ez": row.get("explain_zh", ""),
    }


def recompute(papers: list) -> tuple:
    """Recompute avg_rating and oral_count for a list of papers."""
    ratings = [p["r"] for p in papers if p["r"] is not None and p["r"] > 0]
    avg = round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    oral = len([p for p in papers if p.get("v") and "Oral" in p["v"]])
    return avg, oral


def assign_subcat(text: str, subcats_def: list) -> int:
    """Assign a paper to a subcat based on text matching."""
    text_lower = text.lower()
    for si, (name, keywords) in enumerate(subcats_def):
        if not keywords:  # catch-all
            return si
        for kw in keywords:
            if kw in text_lower:
                return si
    return len(subcats_def) - 1


def regenerate_subcats(cat_idx: int, cat: dict):
    """Regenerate subcategories for a category if it has subcat definitions."""
    if cat_idx not in SUBCATS_DEFS:
        return

    subcats_def = SUBCATS_DEFS[cat_idx]
    subcat_indices = [[] for _ in subcats_def]

    for pi, paper in enumerate(cat["papers"]):
        combined = (paper.get("k", "") or "") + " " + (paper.get("ab", "") or "") + " " + (paper.get("t", "") or "")
        si = assign_subcat(combined, subcats_def)
        subcat_indices[si].append(pi)

    subcats = []
    for si, (name, keywords) in enumerate(subcats_def):
        if subcat_indices[si]:
            subcats.append({"name": name, "paper_indices": subcat_indices[si]})

    # Only add subcats if there are meaningful groups
    catchall_names = {name for name, kws in subcats_def if not kws}
    non_catchall = [sc for sc in subcats if sc["name"] not in catchall_names]
    if len(non_catchall) > 0:
        cat["subcats"] = subcats
    else:
        cat["subcats"] = []


# ── Classification via API ────────────────────────────────────────────────────

def classify_papers_batch(client: Anthropic, papers: list, categories: list) -> list:
    """
    Classify a batch of papers into categories using Claude Sonnet.
    Returns a list of category indices.
    """
    cat_list = "\n".join(f"{i}: {name}" for i, name in enumerate(categories))

    papers_text = ""
    for i, p in enumerate(papers):
        title = p.get("title", "")
        abstract = p.get("abstract", "")[:500]  # truncate for context efficiency
        keywords = p.get("keywords", "")
        papers_text += f"\n[Paper {i}]\nTitle: {title}\nKeywords: {keywords}\nAbstract: {abstract}\n"

    prompt = f"""You are classifying ICLR 2026 papers into research categories.

Here are the {len(categories)} categories:
{cat_list}

Classify each paper below into exactly ONE category. Output ONLY a JSON array of integers (category indices), one per paper, in order.

Example output for 3 papers: [5, 12, 0]

Papers to classify:
{papers_text}

Output the JSON array now:"""

    resp = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    text = resp.content[0].text.strip()
    # Extract JSON array from response
    match = re.search(r"\[[\d,\s]+\]", text)
    if match:
        indices = json.loads(match.group())
        # Validate
        n_cats = len(categories)
        indices = [min(max(0, idx), n_cats - 1) for idx in indices]
        if len(indices) != len(papers):
            print(f"  WARNING: Expected {len(papers)} indices, got {len(indices)}. Padding with 34 (其他).")
            while len(indices) < len(papers):
                indices.append(34)
            indices = indices[: len(papers)]
        return indices
    else:
        print(f"  ERROR: Could not parse response: {text[:200]}")
        return [34] * len(papers)  # default to "其他"


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # 1. Load existing data
    print("Loading existing data/all.json ...")
    with open(ALL_JSON_PATH) as f:
        data = json.load(f)

    categories = [cat["name"] for cat in data]
    n_cats = len(categories)
    print(f"  {n_cats} categories, {sum(c['count'] for c in data)} papers")

    existing_urls = set()
    for cat in data:
        for p in cat["papers"]:
            existing_urls.add(p["u"])

    # 2. Read all CSV files from other/
    print(f"\nReading CSV files from {OTHER_CSV_DIR} ...")
    all_rows = []
    for fname in sorted(os.listdir(OTHER_CSV_DIR)):
        if not fname.endswith(".csv"):
            continue
        fpath = os.path.join(OTHER_CSV_DIR, fname)
        with open(fpath, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            # Skip duplicates
            new_rows = [r for r in rows if r.get("openreview_url") not in existing_urls]
            print(f"  {fname}: {len(rows)} total, {len(new_rows)} new")
            all_rows.extend(new_rows)

    print(f"\nTotal new papers to classify: {len(all_rows)}")

    if not all_rows:
        print("No new papers to add. Exiting.")
        return

    # 3. Classify papers using Sonnet API
    # Try loading cache first
    classification = {}
    if os.path.exists(CLASSIFICATION_CACHE):
        with open(CLASSIFICATION_CACHE) as f:
            classification = json.load(f)
        print(f"Loaded {len(classification)} cached classifications")

    # Find papers that still need classification
    to_classify = [(i, row) for i, row in enumerate(all_rows)
                   if row["openreview_url"] not in classification]

    if to_classify:
        print(f"\nClassifying {len(to_classify)} papers via Sonnet API ...")
        client = Anthropic(api_key="dummy", base_url="http://localhost:4141")

        for batch_start in range(0, len(to_classify), BATCH_SIZE):
            batch = to_classify[batch_start : batch_start + BATCH_SIZE]
            batch_rows = [row for _, row in batch]
            batch_indices_orig = [i for i, _ in batch]

            print(f"  Batch {batch_start // BATCH_SIZE + 1}/{(len(to_classify) + BATCH_SIZE - 1) // BATCH_SIZE} "
                  f"({len(batch)} papers) ...")

            cat_indices = classify_papers_batch(client, batch_rows, categories)

            for (orig_idx, row), cat_idx in zip(batch, cat_indices):
                url = row["openreview_url"]
                classification[url] = cat_idx

            # Save cache after each batch
            with open(CLASSIFICATION_CACHE, "w", encoding="utf-8") as f:
                json.dump(classification, f, ensure_ascii=False)

            time.sleep(0.5)  # small delay between batches

        print(f"Classification complete. {len(classification)} total cached.")
    else:
        print("All papers already classified (from cache).")

    # 4. Convert and add papers to categories
    print("\nAdding papers to categories ...")
    affected_cats = set()
    cat_additions = defaultdict(int)

    for row in all_rows:
        url = row["openreview_url"]
        cat_idx = classification.get(url, 34)  # default to 其他
        if cat_idx < 0 or cat_idx >= n_cats:
            cat_idx = 34

        paper = csv_to_paper(row)
        data[cat_idx]["papers"].append(paper)
        affected_cats.add(cat_idx)
        cat_additions[cat_idx] += 1

    print(f"  Papers distributed across {len(affected_cats)} categories:")
    for cat_idx in sorted(affected_cats):
        print(f"    {cat_idx}: {categories[cat_idx]} (+{cat_additions[cat_idx]})")

    # 5. Update category metadata
    print("\nUpdating category metadata ...")
    for cat_idx in affected_cats:
        cat = data[cat_idx]
        avg, oral = recompute(cat["papers"])
        cat["count"] = len(cat["papers"])
        cat["avg_rating"] = avg
        cat["oral_count"] = oral

    # 6. Regenerate subcategories for affected categories
    print("\nRegenerating subcategories ...")
    for cat_idx in affected_cats:
        if cat_idx in SUBCATS_DEFS:
            regenerate_subcats(cat_idx, data[cat_idx])
            print(f"  Cat {cat_idx} ({categories[cat_idx]}): {len(data[cat_idx].get('subcats', []))} subcats")

    # 7. Write output
    print(f"\nWriting {OUTPUT_PATH} ...")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    # 8. Verification
    total = sum(c["count"] for c in data)
    all_urls = set()
    for cat in data:
        for p in cat["papers"]:
            all_urls.add(p["u"])

    print(f"\n=== Verification ===")
    print(f"Total papers: {total} (expected {len(existing_urls) + len(all_rows)})")
    print(f"Unique URLs: {len(all_urls)}")
    print(f"Categories: {n_cats}")
    print(f"\nCategory distribution:")
    for i, cat in enumerate(data):
        changed = " [UPDATED]" if i in affected_cats else ""
        print(f"  {i:2d}. {cat['name']:40s} {cat['count']:4d}{changed}")

    if total != len(existing_urls) + len(all_rows):
        print(f"\nWARNING: Total mismatch! Expected {len(existing_urls) + len(all_rows)}, got {total}")
    else:
        print(f"\nSUCCESS: All {len(all_rows)} new papers added!")


if __name__ == "__main__":
    main()
