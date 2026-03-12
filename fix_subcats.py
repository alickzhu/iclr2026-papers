#!/usr/bin/env python3
"""Fix imbalanced subcategories in data/index.json."""

import json
import os

DATA_DIR = "/home/v-qinglinzhu/code/read_paper/iclr/data"

# ── New subcat rules for categories that need redoing ──────────────────────

subcat_rules_35 = [
    ("LLM-as-Judge与自动评估", ["llm-as-a-judge", "llm judge", "llm as a judge", "judge model", "evaluator model", "automatic evaluation", "model-based evaluation", "gpt-4 evaluation", "claude evaluation"]),
    ("基准污染与公平性", ["contamination", "data contamination", "benchmark contamination", "test set contamination", "overfitting", "leakage", "train-test", "memorization evaluation"]),
    ("推理与数学能力评测", ["math benchmark", "reasoning benchmark", "logic benchmark", "math evaluation", "problem solving benchmark", "competition math", "aime", "gsm evaluation", "proof evaluation"]),
    ("多模态与语言评测", ["visual benchmark", "multimodal benchmark", "multilingual benchmark", "image benchmark", "video benchmark", "cross-lingual benchmark", "vision-language benchmark", "speech evaluation"]),
    ("对话与指令遵循评测", ["chat evaluation", "instruction following evaluation", "helpfulness", "conversational evaluation", "preference evaluation", "human judgment", "arena", "chatbot evaluation"]),
    ("代码与软件能力评测", ["code benchmark", "coding benchmark", "software benchmark", "humaneval", "mbpp", "swe-bench", "code evaluation"]),
    ("安全与对齐评测", ["safety evaluation", "alignment evaluation", "harmless evaluation", "toxicity evaluation", "bias evaluation", "safety benchmark"]),
    ("其他评测", []),
]

subcat_rules_6 = [
    ("视觉语言理解与问答", ["visual question", "vqa", "image captioning", "visual reasoning", "image understanding", "visual grounding", "referring expression", "ocr", "chart understanding", "document understanding", "image qa"]),
    ("视频语言模型", ["video language", "video llm", "video understanding", "video question", "temporal", "video captioning", "video reasoning", "video-text"]),
    ("多模态空间与3D推理", ["spatial", "3d understanding", "depth", "spatial reasoning", "geometry", "physical reasoning", "embodied multimodal", "scene", "navigation"]),
    ("多模态预训练与对齐", ["multimodal pretrain", "vision-language pretrain", "clip", "vision encoder", "visual representation", "contrastive learning", "image-text alignment", "multimodal alignment", "visual instruction", "llava"]),
    ("多模态生成与编辑", ["multimodal generation", "any-to-any", "unified model", "multimodal editing", "image generation", "image editing", "text-to-image", "image synthesis"]),
    ("多模态安全与鲁棒性", ["multimodal safety", "visual attack", "multimodal attack", "multimodal robustness", "visual hallucination", "hallucination", "multimodal bias"]),
    ("其他多模态", []),
]

subcat_rules_7 = [
    ("越狱与提示注入", ["jailbreak", "prompt injection", "red team", "safety bypass", "harmful content", "refusal", "toxicity", "unsafe", "guardrail"]),
    ("对抗样本与对抗训练", ["adversarial example", "adversarial attack", "adversarial perturbation", "evasion attack", "pgd", "fgsm", "adversarial training", "adversarial robustness"]),
    ("后门与数据投毒", ["backdoor", "trojan", "poisoning", "data poisoning", "supply chain", "hidden trigger", "clean-label"]),
    ("鲁棒性认证与验证", ["certified robustness", "randomized smoothing", "formal verification", "lipschitz", "provable", "bound", "verification method"]),
    ("模型安全与隐私攻击", ["model extraction", "model stealing", "inference attack", "gradient inversion", "model inversion", "membership inference", "privacy attack"]),
    ("LLM安全评估", ["llm safety", "safety evaluation", "red teaming", "safety benchmark", "safety alignment", "harmful", "bias", "llm security", "llm vulnerability"]),
    ("其他安全", []),
]

subcat_rules_4 = [
    ("预训练数据与方法", ["pretraining", "pre-training", "data mixture", "corpus", "web data", "data curation", "pretraining data", "data selection", "tokenomics", "language model pretraining"]),
    ("参数高效微调", ["lora", "peft", "adapter", "prefix tuning", "parameter efficient", "low-rank", "ia3", "prompt tuning"]),
    ("全参数微调与SFT", ["fine-tuning", "finetuning", "supervised fine-tuning", "sft", "instruction tuning", "instruction following", "full fine-tuning"]),
    ("持续学习与模型更新", ["continual learning", "catastrophic forgetting", "lifelong", "sequential learning", "knowledge retention", "model update", "incremental"]),
    ("训练效率与稳定性", ["training efficiency", "training stability", "loss spike", "gradient clipping", "batch size", "learning rate schedule", "warmup", "mixed precision", "distributed training", "parallelism", "throughput"]),
    ("数据增强与合成", ["data augmentation", "synthetic data", "data generation for training", "curriculum", "data quality", "deduplication"]),
    ("其他训练", []),
]


def assign_subcats(papers_meta, cat_papers, rules):
    """
    Assign each paper to a subcat using first-match on keywords.
    papers_meta: list of paper dicts from index.json (have 't', 'k' fields)
    cat_papers: list of dicts from cat_X.json (have 'ab' field)
    rules: list of (name, keywords); last entry is catch-all (empty keywords)
    Returns list of {"name": ..., "paper_indices": [...]}
    """
    assert len(papers_meta) == len(cat_papers), (
        f"Length mismatch: {len(papers_meta)} papers vs {len(cat_papers)} in cat file"
    )

    catchall_name = rules[-1][0]
    buckets = {name: [] for name, _ in rules}

    for i, (meta, ab_entry) in enumerate(zip(papers_meta, cat_papers)):
        title = meta.get("t", "")
        keywords = meta.get("k", "")
        abstract = ab_entry.get("ab", "")
        text = (title + " " + keywords + " " + abstract).lower()

        assigned = False
        for name, kws in rules[:-1]:  # skip catch-all in first pass
            for kw in kws:
                if kw.lower() in text:
                    buckets[name].append(i)
                    assigned = True
                    break
            if assigned:
                break

        if not assigned:
            buckets[catchall_name].append(i)

    # Build result list, preserving order from rules
    result = []
    for name, _ in rules:
        indices = buckets[name]
        # Always include the catch-all even if empty
        if indices or name == catchall_name:
            result.append({"name": name, "paper_indices": indices})

    return result


def merge_tiny_subcats(cat_entry, min_count=5):
    """Merge subcats with <min_count papers into the last (catch-all) subcat."""
    if "subcats" not in cat_entry:
        return []

    subcats = cat_entry["subcats"]
    if len(subcats) <= 1:
        return []

    catchall = subcats[-1]
    merges = []
    to_remove = []

    for i, sc in enumerate(subcats[:-1]):  # don't touch the catch-all itself
        if len(sc["paper_indices"]) < min_count:
            merges.append((sc["name"], len(sc["paper_indices"])))
            catchall["paper_indices"].extend(sc["paper_indices"])
            to_remove.append(i)

    # Remove tiny subcats in reverse order to preserve indices
    for i in reversed(to_remove):
        subcats.pop(i)

    return merges


def verify_subcats(cat_entry, cat_idx):
    """Verify that subcat paper_indices sum equals category count and no duplicates."""
    if "subcats" not in cat_entry:
        return True

    all_indices = []
    for sc in cat_entry["subcats"]:
        all_indices.extend(sc["paper_indices"])

    total = len(all_indices)
    expected = cat_entry["count"]

    if total != expected:
        print(f"  ERROR Cat {cat_idx} '{cat_entry['name']}': subcat total={total}, expected={expected}")
        return False

    if len(set(all_indices)) != total:
        print(f"  ERROR Cat {cat_idx} '{cat_entry['name']}': duplicate indices detected")
        return False

    return True


def print_distribution(cat_entry, cat_idx):
    if "subcats" not in cat_entry:
        return
    print(f"\nCat {cat_idx}: {cat_entry['name']} (total={cat_entry['count']})")
    for sc in cat_entry["subcats"]:
        n = len(sc["paper_indices"])
        pct = n / cat_entry["count"] * 100
        print(f"  {sc['name']}: {n} ({pct:.0f}%)")


def load_cat_json(cat_idx):
    path = os.path.join(DATA_DIR, f"cat_{cat_idx}.json")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main():
    index_path = os.path.join(DATA_DIR, "index.json")
    with open(index_path, encoding="utf-8") as f:
        idx = json.load(f)

    # ── Step 1: Redo specific categories with new rules ────────────────────

    redo_configs = [
        (35, subcat_rules_35, "LLM评测与基准"),
        (6,  subcat_rules_6,  "多模态大模型"),
        (7,  subcat_rules_7,  "AI安全与攻防"),
        (4,  subcat_rules_4,  "LLM训练与预训练"),
    ]

    for cat_idx, rules, desc in redo_configs:
        cat_entry = idx[cat_idx]
        print(f"\n=== Redoing Cat {cat_idx}: {cat_entry['name']} ===")

        cat_papers = load_cat_json(cat_idx)
        new_subcats = assign_subcats(cat_entry["papers"], cat_papers, rules)
        cat_entry["subcats"] = new_subcats

        print("After redo (before tiny-merge):")
        for sc in new_subcats:
            print(f"  {sc['name']}: {len(sc['paper_indices'])}")

    # ── Step 2: Merge tiny subcats (<5) in ALL categories ─────────────────

    print("\n=== Merging tiny subcats (<5 papers) across all categories ===")
    any_merged = False
    for i, cat_entry in enumerate(idx):
        if "subcats" in cat_entry:
            merges = merge_tiny_subcats(cat_entry, min_count=5)
            if merges:
                any_merged = True
                catchall = cat_entry["subcats"][-1]["name"]
                for name, count in merges:
                    print(f"  Cat {i} '{cat_entry['name']}': merged '{name}' ({count} papers) -> '{catchall}'")

    if not any_merged:
        print("  (no tiny subcats found)")

    # ── Step 3: Verify and print final distributions ───────────────────────

    print("\n=== Final distributions for all categories with subcats ===")
    all_ok = True
    for i, cat_entry in enumerate(idx):
        if "subcats" in cat_entry:
            ok = verify_subcats(cat_entry, i)
            if not ok:
                all_ok = False
            print_distribution(cat_entry, i)

    if all_ok:
        print("\nAll subcategory totals verified OK.")
    else:
        print("\nWARNING: Some subcategory totals do not match!")
        return

    # ── Step 4: Save updated index.json ───────────────────────────────────

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, separators=(",", ":"))
    print(f"\nSaved updated index.json to {index_path}")


if __name__ == "__main__":
    main()
