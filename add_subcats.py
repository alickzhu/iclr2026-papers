#!/usr/bin/env python3
"""Script to add subcategories to large categories in index.json"""

import json

# Load index.json
with open('/home/v-qinglinzhu/code/read_paper/iclr/data/index.json') as f:
    DATA = json.load(f)

# Subcategory definitions: (cat_idx, subcat_list)
# Each subcat: (name, keywords_list)  -- empty list = catch-all
SUBCATS_DEFS = {
    0: [  # LLM推理与思维链
        ("数学与逻辑推理", ["math", "mathematics", "arithmetic", "logic", "symbolic", "theorem", "proof", "gsm", "aime", "competition", "olympiad"]),
        ("代码推理与程序合成", ["code", "programming", "program", "software", "execution", "python", "algorithm"]),
        ("推理过程与验证", ["process reward", "step-by-step", "verification", "verifier", "critique", "prm", "outcome reward", "orm", "reward hacking", "reasoning faithfulness", "faithful"]),
        ("思维链方法", ["chain-of-thought", "cot", "scratchpad", "rationale", "thought", "deliberate", "tree of thought", "beam search reasoning", "monte carlo"]),
        ("推理可靠性与幻觉", ["hallucination", "factual", "reliability", "consistency", "confabulation", "sycophancy", "calibration"]),
        ("多步规划与搜索", ["planning", "search", "mcts", "tree search", "beam", "lookahead", "backtracking", "explore"]),
        ("其他推理", []),  # catch-all
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


def assign_subcat(text, subcats_def):
    """Assign a paper to a subcat based on text matching. Returns subcat index."""
    text_lower = text.lower()
    for si, (name, keywords) in enumerate(subcats_def):
        if not keywords:  # catch-all
            return si
        for kw in keywords:
            if kw in text_lower:
                return si
    return len(subcats_def) - 1  # fallback to last (catch-all)


# Process each large category
for cat_idx, subcats_def in SUBCATS_DEFS.items():
    cat = DATA[cat_idx]
    print(f"\nProcessing Cat {cat_idx}: {cat['name']} ({cat['count']} papers)")

    # Load detail data for this category
    with open(f'/home/v-qinglinzhu/code/read_paper/iclr/data/cat_{cat_idx}.json') as f:
        detail_data = json.load(f)

    # Initialize subcat paper indices
    subcat_indices = [[] for _ in subcats_def]

    # Assign each paper to a subcat
    for pi, paper in enumerate(cat['papers']):
        # Combine keywords from index + abstract from detail
        k_text = paper.get('k', '') or ''
        ab_text = detail_data[pi].get('ab', '') if pi < len(detail_data) else ''
        t_text = paper.get('t', '') or ''
        combined = (k_text + ' ' + ab_text + ' ' + t_text)

        si = assign_subcat(combined, subcats_def)
        subcat_indices[si].append(pi)

    # Build subcats list, remove empty ones (but always keep catch-all if it has papers)
    subcats = []
    for si, (name, keywords) in enumerate(subcats_def):
        if subcat_indices[si]:  # only include non-empty subcats
            subcats.append({
                "name": name,
                "paper_indices": subcat_indices[si]
            })
            print(f"  {name}: {len(subcat_indices[si])} papers")
        else:
            print(f"  {name}: 0 papers (skipped)")

    # Only add subcats if there are meaningful groups (more than just catch-all)
    non_catchall = [sc for sc in subcats if sc['name'] not in ('其他推理', '其他扩散', '其他Agent', '其他加速', '其他训练', '其他多模态', '其他安全', '其他对齐', '其他评测')]
    if len(non_catchall) > 0:
        cat['subcats'] = subcats
        print(f"  -> Added {len(subcats)} subcats")
    else:
        print(f"  -> No meaningful subcats, skipping")

# Save updated index.json
with open('/home/v-qinglinzhu/code/read_paper/iclr/data/index.json', 'w', encoding='utf-8') as f:
    json.dump(DATA, f, ensure_ascii=False, separators=(',', ':'))

print("\nDone! index.json updated.")
