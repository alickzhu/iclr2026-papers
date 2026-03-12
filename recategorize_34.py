#!/usr/bin/env python3
"""
Recategorize papers from cat_34 (其他) into existing and new categories.
Goal: reduce cat_34 from 412 to < 100 papers.
"""

import json
import math
from collections import defaultdict

# ── Load data ──────────────────────────────────────────────────────────────────
with open("data/index.json") as f:
    index = json.load(f)

with open("data/cat_34.json") as f:
    cat34_details = json.load(f)

assert len(index[34]["papers"]) == len(cat34_details), "Mismatch!"
print(f"Loaded {len(cat34_details)} papers from cat_34 (其他)")


# ── Helper: compute avg_rating and oral_count ──────────────────────────────────
def recompute(papers):
    ratings = [p["r"] for p in papers if p["r"] is not None]
    avg = round(sum(ratings) / len(ratings), 2) if ratings else 0.0
    oral = len([p for p in papers if p.get("v") and "Oral" in p["v"]])
    return avg, oral


# ── Load all existing cat detail files ────────────────────────────────────────
cat_details = {}
for cat_idx in range(len(index)):
    if cat_idx == 34:
        cat_details[34] = cat34_details
        continue
    fname = f"data/cat_{cat_idx}.json"
    try:
        with open(fname) as f:
            cat_details[cat_idx] = json.load(f)
    except FileNotFoundError:
        cat_details[cat_idx] = []

# Verify sync
for i, cat in enumerate(index):
    if i in cat_details:
        if len(index[i]["papers"]) != len(cat_details[i]):
            print(f"WARNING: cat {i} ({cat['name']}) papers={len(index[i]['papers'])} details={len(cat_details[i])}")


# ── Matching rules ─────────────────────────────────────────────────────────────
def match(text, keywords):
    """Return True if any keyword found in text (case-insensitive)."""
    tl = text.lower()
    for kw in keywords:
        if kw.lower() in tl:
            return True
    return False


# Order matters: first match wins
EXISTING_RULES = [
    # (cat_index, list_of_keywords)
    (0,  ["reasoning", "chain-of-thought", "chain of thought", "cot", " thinking", "logical reasoning",
          "math reasoning", "problem solving", "reward hacking", "inference-time reasoning",
          "step-by-step", "rationale"]),
    (2,  ["agent", "tool use", "tool calling", "agentic", " planning"]),
    (3,  ["speculative decoding", "quantization", "pruning", "compression", "efficient inference",
          "kv cache", "kv-cache"]),
    (4,  ["pre-training", "pretraining", "fine-tuning", "finetuning", "instruction tuning",
          " sft ", "lora", "peft", "continual learning"]),
    (6,  ["multimodal", "vision language", "vlm", "mllm", "visual question", "vqa",
          "image-text", "video-language", "vision-language"]),
    (7,  ["adversarial", " attack", " defense", "robustness", "jailbreak", "backdoor",
          "malware", " security", "certified robustness"]),
    (8,  ["object detection", "segmentation", "visual understanding", "image classification",
          "depth estimation", "optical flow"]),
    (12, ["alignment", " rlhf", "preference learning", "reward model", " dpo ", "safety alignment",
          "value alignment", "constitutional ai"]),
    (14, ["privacy", "federated", "differential privacy", "memorization", "machine unlearning",
          "membership inference"]),
    (19, ["medical", "clinical", "healthcare", "radiology", "pathology", "biomedical", " health "]),
    (20, ["natural language processing", "text classification", "sentiment analysis",
          "named entity", "information extraction", "question answering", "reading comprehension",
          "text understanding", "discourse"]),
    (21, ["fairness", " bias", "discrimination", "social bias", "demographic", "stereotype"]),
    (22, ["code generation", "program synthesis", " software ", "programming", "code repair",
          "code completion", "static analysis", "formal verification"]),
    (26, ["optimization", "convergence", "generalization bound", "pac learning", " sgd ",
          "gradient descent", "learning rate", "loss landscape", "information geometry",
          "optimal transport", "wasserstein", "regret bound", "sample complexity"]),
    (27, ["robot", "embodied", "manipulation", "locomotion", "sim-to-real"]),
    (30, ["watermark", "copyright", "forensic", "image forensics", "deepfake detection",
          "manipulation detection", "image manipulation", "video manipulation"]),
    (31, ["graph neural", " gnn", "graph generation", "molecular graph", "graph learning",
          "knowledge graph", "graph network"]),
    (33, ["time series", "forecasting", "temporal", "sequence prediction"]),
    (35, ["evaluation", "benchmark", "llm judge", "llm-as-a-judge", "contamination", " ranking",
          "leaderboard"]),
    (36, ["neural network theory", "expressivity", "lipschitz", "activation function",
          "neural architecture", "theoretical analysis", "approximation theory",
          "universal approximation", "rademacher"]),
    (37, ["human pose", "pose estimation", "motion capture", "gesture", "skeleton",
          "human body", "action recognition", "3d human", "human reconstruction",
          "point trajectory", "motion generation"]),
    (38, ["model merging", "mixture of experts", "moe", "checkpoint merging",
          "parameter sharing", "looped transformer"]),
    (40, ["scaling law", "learning rate schedule", "pretraining strategy",
          "data mixture", "training dynamics"]),
    # dataset/benchmark last among existing (after LLM eval)
    (17, ["dataset", "benchmark", "annotation"]),
]

# New category rules — indices 41+
NEW_RULES = [
    ("多轮对话与交互",
     ["multi-turn", "dialogue", "conversation", "interactive", "chatbot", "human-ai interaction",
      "conversational"]),
    ("多语言与跨语言",
     ["multilingual", "cross-lingual", "translation", "language confusion",
      "low-resource language", "machine translation", "cross-language"]),
    ("表格与结构化数据",
     ["tabular", "table understanding", "text-to-sql", " sql ", "relational data",
      "structured data", "table qa", "table-to-text"]),
    ("知识编辑与更新",
     ["knowledge editing", "model editing", "knowledge update", "catastrophic forgetting",
      "continual"]),
    ("分词与语言建模",
     ["tokenization", "tokenizer", "subword", "vocabulary", "automata", "transducer",
      "language modeling", "perplexity"]),
    ("LLM可信赖性",
     ["trustworthy", "deception", "honest", "anthropomorphic", "social ai",
      "pluralism", "responsible ai", "sycophancy", "hallucination"]),
    ("图像真实性与取证",
     ["aigc detection", "image forgery", "manipulation localization", "deepfake", "synthetic image"]),
    ("强化学习理论与算法",
     ["reinforcement learning", "reward shaping", "policy gradient", "q-learning",
      "actor-critic", "exploration", "multi-agent", "offline rl", "off-policy"]),
]


# ── Classify all 412 papers ────────────────────────────────────────────────────
assignments = []  # (cat_idx_or_None, paper_obj, detail_obj)

new_cat_papers = defaultdict(list)   # name -> [(paper_obj, detail_obj)]
new_cat_order = [r[0] for r in NEW_RULES]  # preserve order

for i, (paper, detail) in enumerate(zip(index[34]["papers"], cat34_details)):
    # Build text to match against: title + keywords + abstract
    full_text = (
        (paper.get("t") or "") + " " +
        (paper.get("k") or "") + " " +
        (detail.get("ab") or "")
    )

    assigned = None

    # Try existing categories
    for cat_idx, kws in EXISTING_RULES:
        if match(full_text, kws):
            assigned = cat_idx
            break

    if assigned is None:
        # Try new categories
        for name, kws in NEW_RULES:
            if match(full_text, kws):
                new_cat_papers[name].append((paper, detail))
                assigned = name  # string sentinel
                break

    assignments.append((assigned, paper, detail))


# ── Determine which new categories make the cut (>= 8 papers) ─────────────────
qualifying_new = {name for name, papers in new_cat_papers.items() if len(papers) >= 8}
print("\nNew category candidates:")
for name in new_cat_order:
    cnt = len(new_cat_papers[name])
    status = "QUALIFY" if name in qualifying_new else "too few"
    print(f"  {name}: {cnt} papers  [{status}]")

# Papers in non-qualifying new cats go back to 其他
# Re-process assignments:
final_kept_34 = []
final_kept_34_details = []
moves_to_existing = defaultdict(list)  # cat_idx -> [(paper, detail)]
moves_to_new = defaultdict(list)       # name -> [(paper, detail)]

for assigned, paper, detail in assignments:
    if assigned is None:
        final_kept_34.append(paper)
        final_kept_34_details.append(detail)
    elif isinstance(assigned, int):
        moves_to_existing[assigned].append((paper, detail))
    else:  # string = new category name
        if assigned in qualifying_new:
            moves_to_new[assigned].append((paper, detail))
        else:
            final_kept_34.append(paper)
            final_kept_34_details.append(detail)

print(f"\nPapers remaining in 其他: {len(final_kept_34)}")
print(f"Papers moved to existing cats: {sum(len(v) for v in moves_to_existing.values())}")
print(f"Papers moved to new cats: {sum(len(v) for v in moves_to_new.values())}")


# ── Update index and detail files ─────────────────────────────────────────────

# 1) Update existing categories
for cat_idx, papers_details in moves_to_existing.items():
    for paper, detail in papers_details:
        index[cat_idx]["papers"].append(paper)
        cat_details[cat_idx].append(detail)
    avg, oral = recompute(index[cat_idx]["papers"])
    index[cat_idx]["count"] = len(index[cat_idx]["papers"])
    index[cat_idx]["avg_rating"] = avg
    index[cat_idx]["oral_count"] = oral

# 2) Update cat_34
index[34]["papers"] = final_kept_34
cat_details[34] = final_kept_34_details
avg34, oral34 = recompute(final_kept_34)
index[34]["count"] = len(final_kept_34)
index[34]["avg_rating"] = avg34
index[34]["oral_count"] = oral34

# 3) Create new categories
new_idx_map = {}
next_idx = 41
for name in new_cat_order:
    if name not in qualifying_new:
        continue
    papers_details = moves_to_new[name]
    papers_list = [p for p, d in papers_details]
    details_list = [d for p, d in papers_details]
    avg, oral = recompute(papers_list)
    new_entry = {
        "name": name,
        "count": len(papers_list),
        "avg_rating": avg,
        "oral_count": oral,
        "hot": False,
        "papers": papers_list,
    }
    index.append(new_entry)
    cat_details[next_idx] = details_list
    new_idx_map[name] = next_idx
    print(f"Created cat_{next_idx}: {name} ({len(papers_list)} papers)")
    next_idx += 1


# ── Write all modified files ───────────────────────────────────────────────────
# Write index.json
with open("data/index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, separators=(",", ":"))
print("\nWrote data/index.json")

# Write cat_34.json
with open("data/cat_34.json", "w", encoding="utf-8") as f:
    json.dump(cat34_details if False else final_kept_34_details, f, ensure_ascii=False, separators=(",", ":"))
print("Wrote data/cat_34.json")

# Write modified existing cat files
for cat_idx in moves_to_existing:
    fname = f"data/cat_{cat_idx}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(cat_details[cat_idx], f, ensure_ascii=False, separators=(",", ":"))
    print(f"Wrote {fname}")

# Write new cat files
for name, nidx in new_idx_map.items():
    fname = f"data/cat_{nidx}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(cat_details[nidx], f, ensure_ascii=False, separators=(",", ":"))
    print(f"Wrote {fname}")


# ── Verification ───────────────────────────────────────────────────────────────
print("\n=== Final Category Distribution ===")
for i, cat in enumerate(index):
    flag = " *** MODIFIED ***" if i == 34 or i in moves_to_existing or (i >= 41) else ""
    print(f"{i:2d}. {cat['name']:40s} {cat['count']:4d}{flag}")

print(f"\ncat_34 (其他) count: {index[34]['count']}")
assert index[34]["count"] < 100, f"FAIL: 其他 still has {index[34]['count']} papers!"
print("SUCCESS: 其他 < 100 papers!")

# Sanity check sync
print("\n=== Sync Check ===")
all_ok = True
for i, cat in enumerate(index):
    if i in cat_details:
        if len(cat["papers"]) != len(cat_details[i]):
            print(f"MISMATCH cat {i}: papers={len(cat['papers'])} details={len(cat_details[i])}")
            all_ok = False
if all_ok:
    print("All categories in sync.")
