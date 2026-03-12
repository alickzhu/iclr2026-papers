# ICLR 2026 论文智能分类与热点分析报告

> 基于 Haiku 模型对 3488 篇论文逐篇阅读标题+摘要后动态分类
> 再由 Opus 模型合并相似类别，形成35个研究方向
> 生成日期: 2026-03-12

## 一、整体概览

| 指标 | 数值 |
|---|---|
| 总论文数 | 3488 |
| Oral 论文 | 144 |
| 平均评分 | 5.40 |
| AI分类方向数 | 35 |

## 二、热门方向排行

| 排名 | 方向 | 论文数 | 占比 | 平均分 | Oral数 | 热度 |
|---|---|---|---|---|---|---|
| 2 | **LLM推理与思维链** | 383 | 11.0% | 5.37 | 12 | 🔥🔥🔥 |
| 3 | **扩散模型与Flow Matching** | 212 | 6.1% | 5.54 | 8 | 🔥🔥🔥 |
| 4 | **LLM Agent与工具使用** | 202 | 5.8% | 5.42 | 15 | 🔥🔥 |
| 5 | **LLM推理加速与压缩** | 153 | 4.4% | 5.39 | 4 | 🔥🔥 |
| 6 | **LLM训练与预训练** | 152 | 4.4% | 5.43 | 4 | 🔥🔥 |
| 7 | **3D生成与重建** | 141 | 4.0% | 5.66 | 8 | 🔥🔥 |
| 8 | **多模态大模型** | 133 | 3.8% | 5.46 | 2 | 🔥🔥 |
| 9 | **AI安全与攻防** | 118 | 3.4% | 5.18 | 3 | 🔥 |
| 10 | **视觉理解与检测** | 116 | 3.3% | 5.28 | 3 | 🔥 |
| 11 | **强化学习** | 106 | 3.0% | 5.53 | 4 | 🔥 |
| 12 | **视频生成与编辑** | 92 | 2.6% | 5.58 | 5 | 🔥 |
| 13 | **图像生成与编辑** | 87 | 2.5% | 5.56 | 5 | 🔥 |
| 14 | **RLHF与对齐** | 85 | 2.4% | 5.48 | 5 | 🔥 |
| 15 | **表征学习与自监督** | 82 | 2.4% | 5.43 | 3 | 🔥 |
| 16 | **隐私与联邦学习** | 82 | 2.4% | 5.33 | 3 |  |
| 17 | **语音与音频** | 67 | 1.9% | 5.45 | 6 |  |
| 18 | **检索增强与知识** | 58 | 1.7% | 5.28 | 2 |  |
| 19 | **数据集与评测** | 45 | 1.3% | 5.41 | 3 |  |
| 20 | **测试时计算与Scaling** | 39 | 1.1% | 5.82 | 4 |  |
| 21 | **医学AI** | 36 | 1.0% | 5.11 | 0 |  |
| 22 | **自然语言处理** | 34 | 1.0% | 5.04 | 2 |  |
| 23 | **公平性与偏见** | 34 | 1.0% | 5.39 | 1 |  |
| 24 | **代码生成与验证** | 32 | 0.9% | 5.34 | 2 |  |
| 25 | **架构创新** | 31 | 0.9% | 5.33 | 3 |  |
| 26 | **长上下文与记忆** | 29 | 0.8% | 5.40 | 2 |  |
| 27 | **科学计算与AI4Science** | 24 | 0.7% | 5.03 | 0 |  |
| 28 | **优化与学习理论** | 23 | 0.7% | 4.91 | 0 |  |
| 29 | **机器人与具身智能** | 22 | 0.6% | 5.45 | 0 |  |
| 30 | **上下文学习与提示** | 21 | 0.6% | 5.16 | 1 |  |
| 31 | **模型可解释性** | 21 | 0.6% | 5.29 | 0 |  |
| 32 | **水印与版权保护** | 18 | 0.5% | 5.33 | 3 |  |
| 33 | **图学习与GNN** | 10 | 0.3% | 5.22 | 0 |  |
| 34 | **合成数据与数据增强** | 9 | 0.3% | 5.50 | 1 |  |
| 35 | **时间序列与预测** | 7 | 0.2% | 5.33 | 0 |  |

## 三、高质量方向排行 (按平均评分)

| 排名 | 方向 | 平均分 | 论文数 | Oral占比 |
|---|---|---|---|---|
| 1 | 测试时计算与Scaling | 5.82 | 39 | 10.3% |
| 2 | 3D生成与重建 | 5.66 | 141 | 5.7% |
| 3 | 视频生成与编辑 | 5.58 | 92 | 5.4% |
| 4 | 图像生成与编辑 | 5.56 | 87 | 5.7% |
| 5 | 扩散模型与Flow Matching | 5.54 | 212 | 3.8% |
| 6 | 强化学习 | 5.53 | 106 | 3.8% |
| 7 | RLHF与对齐 | 5.48 | 85 | 5.9% |
| 8 | 多模态大模型 | 5.46 | 133 | 1.5% |
| 9 | 语音与音频 | 5.45 | 67 | 9.0% |
| 10 | 机器人与具身智能 | 5.45 | 22 | 0.0% |
| 11 | 表征学习与自监督 | 5.43 | 82 | 3.7% |
| 12 | LLM训练与预训练 | 5.43 | 152 | 2.6% |
| 13 | LLM Agent与工具使用 | 5.42 | 202 | 7.4% |
| 14 | 数据集与评测 | 5.41 | 45 | 6.7% |
| 15 | 长上下文与记忆 | 5.40 | 29 | 6.9% |
| 16 | LLM推理加速与压缩 | 5.39 | 153 | 2.6% |
| 17 | 公平性与偏见 | 5.39 | 34 | 2.9% |
| 18 | LLM推理与思维链 | 5.37 | 383 | 3.1% |
| 19 | 代码生成与验证 | 5.34 | 32 | 6.2% |
| 20 | 水印与版权保护 | 5.33 | 18 | 16.7% |
| 21 | 隐私与联邦学习 | 5.33 | 82 | 3.7% |
| 22 | 架构创新 | 5.33 | 31 | 9.7% |
| 23 | 模型可解释性 | 5.29 | 21 | 0.0% |
| 24 | 视觉理解与检测 | 5.28 | 116 | 2.6% |
| 25 | 检索增强与知识 | 5.28 | 58 | 3.4% |
| 26 | AI安全与攻防 | 5.18 | 118 | 2.5% |
| 27 | 上下文学习与提示 | 5.16 | 21 | 4.8% |
| 28 | 医学AI | 5.11 | 36 | 0.0% |
| 29 | 自然语言处理 | 5.04 | 34 | 5.9% |
| 30 | 科学计算与AI4Science | 5.03 | 24 | 0.0% |
| 31 | 优化与学习理论 | 4.91 | 23 | 0.0% |

## 四、各方向详细分析与代表论文

### LLM推理与思维链
**383篇** | 平均分 5.37 | Oral 12篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | **Oral** | Generative Universal Verifier as Multimodal Meta-Reasoner | [link](https://openreview.net/forum?id=DM0Y0oL33T) |
| 7.5 | **Oral** | Reasoning with Sampling: Your Base Model is Smarter Than You Think | [link](https://openreview.net/forum?id=Vsgq2ldr4K) |
| 7.3 | Poster | Nemotron-CC-Math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset | [link](https://openreview.net/forum?id=rhPnkTKfMy) |
| 7.0 | Poster | SimpleTIR: End-to-End Reinforcement Learning for Multi-Turn Tool-Integrated Reasoning | [link](https://openreview.net/forum?id=EplNy91Xqh) |
| 7.0 | Poster | Efficient Reasoning with Balanced Thinking | [link](https://openreview.net/forum?id=cJseWJJ5IM) |

### 扩散模型与Flow Matching
**212篇** | 平均分 5.54 | Oral 8篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | Fast-dLLM: Training-free Acceleration of Diffusion LLM by Enabling KV Cache and Parallel Decoding | [link](https://openreview.net/forum?id=3Z3Is6hnOT) |
| 7.0 | **Oral** | GLASS Flows: Efficient Inference for Reward Alignment of Flow and Diffusion Models | [link](https://openreview.net/forum?id=vH7OAPZ2dR) |
| 7.0 | **Oral** | Let Features Decide Their Own Solvers: Hybrid Feature Caching for Diffusion Transformers | [link](https://openreview.net/forum?id=URbsHlTK8c) |
| 7.0 | **Oral** | Partition Generative Modeling: Masked Modeling Without Masks | [link](https://openreview.net/forum?id=vEh1ceS154) |
| 7.0 | Poster | Diagnosing and Improving Diffusion Models by Estimating Optimal Loss Value | [link](https://openreview.net/forum?id=X7JfjLKKLQ) |

### LLM Agent与工具使用
**202篇** | 平均分 5.42 | Oral 15篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | **Oral** | Gaia2: Benchmarking LLM Agents on Dynamic and  Asynchronous Environments | [link](https://openreview.net/forum?id=9gw03JpKK4) |
| 7.3 | Poster | Improving Human-AI Coordination through Online Adversarial Training and Generative Models | [link](https://openreview.net/forum?id=AeehNfbHqD) |
| 7.3 | **Oral** | In-The-Flow Agentic System Optimization for Effective Planning and Tool Use | [link](https://openreview.net/forum?id=Mf5AleTUVK) |
| 7.3 | Poster | Multimodal Policy Internalization for Conversational Agents | [link](https://openreview.net/forum?id=fSE0rUngCX) |
| 7.3 | Poster | FutureX: An Advanced Live Benchmark for LLM Agents in Future Prediction | [link](https://openreview.net/forum?id=z28PLIEj6l) |

### LLM推理加速与压缩
**153篇** | 平均分 5.39 | Oral 4篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel | [link](https://openreview.net/forum?id=c5mdo1hWrs) |
| 7.0 | Poster | Exploring the Limits of Sub-Billion Language Model Reasoners with Open Training Recipes | [link](https://openreview.net/forum?id=GMlZt4fZSY) |
| 7.0 | Poster | ParoQuant: Pairwise Rotation Quantization for Efficient Reasoning LLM Inference | [link](https://openreview.net/forum?id=1USeVjsKau) |
| 6.8 | Poster | Quantized Visual Geometry Grounded Transformer | [link](https://openreview.net/forum?id=Xzcllrc6gb) |
| 6.7 | Poster | MoBE: Mixture-of-Basis-Experts for Compressing MoE-based LLMs | [link](https://openreview.net/forum?id=8RV6H50OSf) |

### LLM训练与预训练
**152篇** | 平均分 5.43 | Oral 4篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | CoDA: Agentic Systems for Collaborative Data Visualization | [link](https://openreview.net/forum?id=M4RKeHIAxw) |
| 7.3 | Poster | LLM Pretraining with Continuous Concepts | [link](https://openreview.net/forum?id=wTGcb3DxOn) |
| 7.0 | Poster | MemGen: Weaving Generative Latent Memory for Self-Evolving Agents | [link](https://openreview.net/forum?id=vI56m4Iu4e) |
| 7.0 | **Oral** | Common Corpus: The Largest Collection of Ethical Data for LLM Pre-Training | [link](https://openreview.net/forum?id=0wSlFpMsGb) |
| 7.0 | Poster | CMT: Mid-Training for Efficient Learning of Consistency, Mean Flow, and Flow-Map Models | [link](https://openreview.net/forum?id=2B8GkGTgmY) |

### 3D生成与重建
**141篇** | 平均分 5.66 | Oral 8篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | Poster | $\pi^3$: Permutation-Equivariant Visual Geometry Learning | [link](https://openreview.net/forum?id=DTQIjngDta) |
| 8.0 | **Oral** | Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator | [link](https://openreview.net/forum?id=kI27Niy4xY) |
| 7.0 | **Oral** | Depth Anything 3: Recovering the Visual Space from Any Views | [link](https://openreview.net/forum?id=yirunib8l8) |
| 7.0 | Poster | 3DGEER: 3D Gaussian Rendering Made Exact and Efficient for Generic Cameras | [link](https://openreview.net/forum?id=4voMNlRWI7) |
| 7.0 | Poster | Mono4DGS-HDR: High Dynamic Range 4D Gaussian Splatting from Alternating-exposure Monocular Videos | [link](https://openreview.net/forum?id=9ZrjgzlAuh) |

### 多模态大模型
**133篇** | 平均分 5.46 | Oral 2篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | SAM-Veteran: An MLLM-Based Human-like SAM Agent for Reasoning Segmentation | [link](https://openreview.net/forum?id=oN55r8iJJW) |
| 7.0 | Poster | Towards Physically Executable 3D Gaussian for Embodied Navigation | [link](https://openreview.net/forum?id=HB6KvsqcAn) |
| 7.0 | Poster | SAM 3: Segment Anything with Concepts | [link](https://openreview.net/forum?id=r35clVtGzw) |
| 6.7 | **Oral** | Multimodal Aligned Semantic Knowledge for Unpaired Image-text Matching | [link](https://openreview.net/forum?id=d3CISVVO6v) |
| 6.7 | Poster | JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence | [link](https://openreview.net/forum?id=N4BB09TXad) |

### AI安全与攻防
**118篇** | 平均分 5.18 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | AlphaSteer: Learning Refusal Steering with Principled Null-Space Constraint | [link](https://openreview.net/forum?id=1vvbzAqdTe) |
| 6.7 | Poster | RedSage: A Cybersecurity Generalist LLM | [link](https://openreview.net/forum?id=W4FAenIrQ2) |
| 6.7 | Poster | Break the Trade-off Between Watermark Strength and Speculative Sampling Efficiency for Language Models | [link](https://openreview.net/forum?id=HA8vzzT6Ax) |
| 6.5 | Poster | Minimax Optimal Adversarial Reinforcement Learning | [link](https://openreview.net/forum?id=QEcSLhfOoQ) |
| 6.5 | **Oral** | Veritas: Generalizable Deepfake Detection via Pattern-Aware Reasoning | [link](https://openreview.net/forum?id=5VXJPS1HoM) |

### 视觉理解与检测
**116篇** | 平均分 5.28 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | InclusiveVidPose: Bridging the Pose Estimation Gap for Individuals with Limb Deficiencies in Video-Based Motion | [link](https://openreview.net/forum?id=SyQqXAdWUq) |
| 7.3 | Poster | MTVCraft: Tokenizing 4D Motion for Arbitrary Character Animation | [link](https://openreview.net/forum?id=m7AQM9H6wa) |
| 7.0 | Poster | Human-Object Interaction via Automatically Designed VLM-Guided Motion Policy | [link](https://openreview.net/forum?id=LfkPlFTfe0) |
| 7.0 | Poster | Point2RBox-v3: Self-Bootstrapping from Point Annotations via Integrated Pseudo-Label Refinement and Utilization | [link](https://openreview.net/forum?id=9vlS8PSGG7) |
| 7.0 | Poster | TOUCH: Text-guided Controllable Generation of Free-Form Hand-Object Interactions | [link](https://openreview.net/forum?id=4VW9HVCRw0) |

### 强化学习
**106篇** | 平均分 5.53 | Oral 4篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | Poster | Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data | [link](https://openreview.net/forum?id=oBXfPyi47m) |
| 7.5 | **Oral** | TD-JEPA: Latent-predictive Representations for Zero-Shot Reinforcement Learning | [link](https://openreview.net/forum?id=SzXDuBN8M1) |
| 7.3 | Poster | Safe Exploration via Policy Priors | [link](https://openreview.net/forum?id=JC8xYAADHL) |
| 7.3 | **Oral** | Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling | [link](https://openreview.net/forum?id=lTaPtGiUUc) |
| 7.0 | **Oral** | Mean Flow Policy with Instantaneous Velocity Constraint for One-step Action Generation | [link](https://openreview.net/forum?id=mIeKe74W43) |

### 视频生成与编辑
**92篇** | 平均分 5.58 | Oral 5篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | Self-Forcing++: Towards Minute-Scale High-Quality Video Generation | [link](https://openreview.net/forum?id=DzvPiqh23f) |
| 7.0 | **Oral** | Instilling an Active Mind in Avatars via Cognitive Simulation | [link](https://openreview.net/forum?id=80JylHgQn1) |
| 7.0 | Poster | EgoTwin: Dreaming Body and View in First Person | [link](https://openreview.net/forum?id=QFJkvv3zMi) |
| 7.0 | Poster | MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation | [link](https://openreview.net/forum?id=0hy9kJ1ULB) |
| 6.8 | Poster | QVGen: Pushing the Limit of Quantized Video Generative Models | [link](https://openreview.net/forum?id=XJXZXuTj11) |

### 图像生成与编辑
**87篇** | 平均分 5.56 | Oral 5篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.5 | **Oral** | Quotient-Space Diffusion Model | [link](https://openreview.net/forum?id=3JPAkwSVc4) |
| 7.5 | Poster | FullPart: Generating each 3D Part at Full Resolution | [link](https://openreview.net/forum?id=QlRlE7a1p4) |
| 7.5 | Poster | TEMPFLOW-GRPO: WHEN TIMING MATTERS FOR GRPO IN FLOW MODELS | [link](https://openreview.net/forum?id=7mCo3R3Wyn) |
| 7.3 | Poster | Does FLUX Already Know How to Perform Physically Plausible Image Composition? | [link](https://openreview.net/forum?id=DcVg87ibK9) |
| 7.3 | **Oral** | DiffusionNFT: Online Diffusion Reinforcement with Forward Process | [link](https://openreview.net/forum?id=VJZ477R89F) |

### RLHF与对齐
**85篇** | 平均分 5.48 | Oral 5篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.5 | Poster | Persona Features Control Emergent Misalignment | [link](https://openreview.net/forum?id=yjrVOxjkDR) |
| 7.0 | Poster | Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability | [link](https://openreview.net/forum?id=ZMzha5gbnF) |
| 6.7 | Poster | Escaping Policy Contraction: Contraction-Aware PPO (CaPPO) for Stable Language Model Fine-Tuning | [link](https://openreview.net/forum?id=vDlkJewkDu) |
| 6.7 | Poster | RECAST: Expanding the Boundaries of LLMs' Complex Instruction Following with Multi-Constraint Data | [link](https://openreview.net/forum?id=90tCp2KszA) |
| 6.5 | Poster | All Roads Lead to Likelihood: The Value of Reinforcement Learning in Fine-Tuning | [link](https://openreview.net/forum?id=sCL5mSTpKm) |

### 表征学习与自监督
**82篇** | 平均分 5.43 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models | [link](https://openreview.net/forum?id=6T3wJQhvc3) |
| 7.0 | **Oral** | Uncover Underlying Correspondence for Robust Multi-view Clustering | [link](https://openreview.net/forum?id=a4S1nQay3b) |
| 7.0 | Poster | Explainable $ K $-means Neural Networks for Multi-view Clustering | [link](https://openreview.net/forum?id=ljM1HTSH9c) |
| 7.0 | Poster | Relationship Alignment for View-aware Multi-view Clustering | [link](https://openreview.net/forum?id=uRA9cT4MK6) |
| 7.0 | Poster | Unified and Efficient Multi-view Clustering from Probabilistic Perspective | [link](https://openreview.net/forum?id=KAGR7Mqu4h) |

### 隐私与联邦学习
**82篇** | 平均分 5.33 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.5 | Poster | Back to Square Roots: An Optimal Bound on the Matrix Factorization Error for Multi-Epoch Differentially Private SGD | [link](https://openreview.net/forum?id=EEr6cADbZx) |
| 7.0 | Poster | Not All Clients Are Equal: Collaborative Model Personalization on Heterogeneous Multi-Modal Clients | [link](https://openreview.net/forum?id=0g5Dk4Qfh0) |
| 6.7 | Poster | INO-SGD: Addressing Utility Imbalance under Individualized Differential Privacy | [link](https://openreview.net/forum?id=HMapYMkcrl) |
| 6.5 | Poster | Contextual Similarity Distillation: Ensemble Uncertainties with a Single Model | [link](https://openreview.net/forum?id=arms7s9dDK) |
| 6.5 | **Oral** | Differentially Private Domain Discovery | [link](https://openreview.net/forum?id=yBpzF8hp3J) |

### 语音与音频
**67篇** | 平均分 5.45 | Oral 6篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | Poster | Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition | [link](https://openreview.net/forum?id=sSbEEHNEsL) |
| 7.5 | Poster | StableToken: A Noise-Robust Semantic Speech Tokenizer for Resilient SpeechLLMs | [link](https://openreview.net/forum?id=17DNmdQ9aU) |
| 7.0 | Poster | AVoCaDO: An Audiovisual Video Captioner Driven by Temporal Orchestration | [link](https://openreview.net/forum?id=vjEl1PuIDE) |
| 7.0 | Poster | AudioX: A Unified Framework for Anything-to-Audio Generation | [link](https://openreview.net/forum?id=qjJWxK3yWo) |
| 6.8 | Poster | AudioTrust: Benchmarking The Multifaceted Trustworthiness of Audio Large Language Models | [link](https://openreview.net/forum?id=E823AY0taq) |

### 检索增强与知识
**58篇** | 平均分 5.28 | Oral 2篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | **Oral** | MetaEmbed: Scaling Multimodal Retrieval at Test-Time with Flexible Late Interaction | [link](https://openreview.net/forum?id=yKDqg9HwZX) |
| 6.7 | Poster | KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unlearning | [link](https://openreview.net/forum?id=znnA2Opw6v) |
| 6.5 | Poster | OSCAR: Online Soft Compression for RAG | [link](https://openreview.net/forum?id=ideKAUWvFE) |
| 6.5 | **Oral** | Revela: Dense Retriever Learning via Language Modeling | [link](https://openreview.net/forum?id=e7pAjJZJWb) |
| 6.5 | Poster | CaReBench: A Fine-grained Benchmark for Video Captioning and Retrieval | [link](https://openreview.net/forum?id=OZtGhb9x7C) |

### 数据集与评测
**45篇** | 平均分 5.41 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | MCPMark: A Benchmark for Stress-Testing Realistic and Comprehensive MCP Use | [link](https://openreview.net/forum?id=uobROwBsJm) |
| 7.0 | Poster | AutoBio: A Simulation and Benchmark for Robotic Automation in Digital Biology Laboratory | [link](https://openreview.net/forum?id=UUE6HEtjhu) |
| 7.0 | Poster | RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Generalist Robots | [link](https://openreview.net/forum?id=tQJYKwc3n4) |
| 6.7 | Poster | DISCO: Diversifying Sample Condensation for Accelerating Model Evaluation | [link](https://openreview.net/forum?id=SoOgBHa3dZ) |
| 6.7 | **Oral** | CounselBench: A Large-Scale Expert Evaluation and Adversarial Benchmarking of Large Language Models in Mental Health Question Answering | [link](https://openreview.net/forum?id=8MBYRZHVWT) |

### 测试时计算与Scaling
**39篇** | 平均分 5.82 | Oral 4篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 8.0 | Poster | Scaling with Collapse: Efficient and Predictable Training of LLM Families | [link](https://openreview.net/forum?id=3YKeB9R1g9) |
| 7.5 | **Oral** | Pre-training under infinite compute | [link](https://openreview.net/forum?id=ck0aZTAnwK) |
| 7.5 | **Oral** | The Art of Scaling Reinforcement Learning Compute for LLMs | [link](https://openreview.net/forum?id=FMjeC9Msws) |
| 7.3 | **Oral** | In-Place Test-Time Training | [link](https://openreview.net/forum?id=dTWfCLSoyl) |
| 7.0 | Poster | Test-Time Alignment for Large Language Models via Textual Model Predictive Control | [link](https://openreview.net/forum?id=DsS3xRPSs5) |

### 医学AI
**36篇** | 平均分 5.11 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.5 | Poster | Fusing Pixels and Genes: Spatially-Aware Learning in Computational Pathology | [link](https://openreview.net/forum?id=uVXO6gzVzj) |
| 6.5 | Poster | Mixture of Mini Experts: Overcoming the Linear Layer Bottleneck in Multiple Instance Learning | [link](https://openreview.net/forum?id=S5Io33pc78) |
| 6.0 | Poster | ASMIL: Attention-Stabilized Multiple Instance Learning for Whole-Slide Imaging | [link](https://openreview.net/forum?id=CYmjrbQRyM) |
| 6.0 | Poster | ProstaTD: Bridging Surgical Triplet from Classification to Fully Supervised Detection | [link](https://openreview.net/forum?id=0NkXZ98BjJ) |
| 6.0 | Poster | From Medical Records to Diagnostic Dialogues: A Clinical-Grounded Approach and Dataset for Psychiatric Comorbidity | [link](https://openreview.net/forum?id=sWWAZVHtke) |

### 自然语言处理
**34篇** | 平均分 5.04 | Oral 2篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.5 | **Oral** | Overthinking Reduction with Decoupled Rewards and Curriculum Data Scheduling | [link](https://openreview.net/forum?id=kdeiRledV6) |
| 6.0 | Poster | From Utterance to Vividity: Training Expressive Subtitle Translation LLM via Adaptive Local Preference Optimization | [link](https://openreview.net/forum?id=d3ABURcHk3) |
| 6.0 | **Oral** | LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning | [link](https://openreview.net/forum?id=JWx4DI2N8k) |
| 6.0 | Poster | A High Quality Dataset and Reliable Evaluation for Interleaved Image-Text Generation | [link](https://openreview.net/forum?id=qBORZkk28r) |
| 6.0 | Poster | ClarifyVC: Clarifying Ambiguous Commands in Vehicle Control with a Hybrid Data Augmentation Pipeline | [link](https://openreview.net/forum?id=afO3vnSNsS) |

### 公平性与偏见
**34篇** | 平均分 5.39 | Oral 1篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | Adaptive Social Learning via Mode Policy Optimization for Language Agents | [link](https://openreview.net/forum?id=GG7YQnsdhp) |
| 7.0 | Poster | Fair Decision Utility in Human-AI Collaboration: Interpretable Confidence Adjustment for Humans with Cognitive Disparities | [link](https://openreview.net/forum?id=hqq6GyYISN) |
| 6.5 | **Oral** | Steering the Herd: A Framework for LLM-based Control of Social Learning | [link](https://openreview.net/forum?id=RtS4UqSmNt) |
| 6.5 | Poster | Fair in Mind, Fair in Action? A Synchronous Benchmark for Understanding and Generation in UMLLMs | [link](https://openreview.net/forum?id=NYphgYTloq) |
| 6.5 | Poster | Private Rate-Constrained Optimization with Applications to Fair Learning | [link](https://openreview.net/forum?id=mex3rvs2KX) |

### 代码生成与验证
**32篇** | 平均分 5.34 | Oral 2篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.5 | **Oral** | EditBench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits | [link](https://openreview.net/forum?id=FtL9eEmU6v) |
| 6.0 | **Oral** | Mastering Sparse CUDA Generation through Pretrained Models and Deep Reinforcement Learning | [link](https://openreview.net/forum?id=VdLEaGPYWT) |
| 6.0 | Poster | Code World Models for General Game Playing | [link](https://openreview.net/forum?id=1UoB7IWiku) |
| 6.0 | Poster | AtlasKV: Augmenting LLMs with Billion-Scale Knowledge Graphs in 20GB VRAM | [link](https://openreview.net/forum?id=6i1jVAYbHs) |
| 6.0 | Poster | Multi-Head Low-Rank Attention | [link](https://openreview.net/forum?id=vBJKZ19XGY) |

### 架构创新
**31篇** | 平均分 5.33 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | **Oral** | Mamba-3: Improved Sequence Modeling using State Space Principles | [link](https://openreview.net/forum?id=HwCvaJOiCj) |
| 6.7 | **Oral** | Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss | [link](https://openreview.net/forum?id=MpeyjgWbKt) |
| 6.7 | Poster | Log-Linear Attention | [link](https://openreview.net/forum?id=mOJgZWkXKW) |
| 6.5 | Poster | Guiding Mixture-of-Experts with Temporal Multimodal Interactions | [link](https://openreview.net/forum?id=qF9WJxvHX8) |
| 6.5 | **Oral** | MrRoPE: Mixed-radix Rotary Position Embedding | [link](https://openreview.net/forum?id=1J63FJYJKg) |

### 长上下文与记忆
**29篇** | 平均分 5.40 | Oral 2篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.5 | Poster | UltraMemV2: Memory Networks Scaling to 120B Parameters with Superior Long-Context Learning | [link](https://openreview.net/forum?id=QWuXU0qNX0) |
| 6.5 | Poster | Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation | [link](https://openreview.net/forum?id=DgkWFPZMPp) |
| 6.0 | **Oral** | Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training | [link](https://openreview.net/forum?id=MS9nWFY7LG) |
| 6.0 | Poster | SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models | [link](https://openreview.net/forum?id=83F6YF4Hz6) |
| 6.0 | Poster | SoLoPO: Unlocking Long-Context Capabilities in LLMs via Short-to-Long Preference Optimization | [link](https://openreview.net/forum?id=iiBjaiikJG) |

### 科学计算与AI4Science
**24篇** | 平均分 5.03 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.3 | Poster | THEMIS: Towards Holistic Evaluation of MLLMs for Scientific Paper Fraud Forensics | [link](https://openreview.net/forum?id=y3UkklvoW9) |
| 6.0 | Poster | TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning | [link](https://openreview.net/forum?id=rJv2byEWA3) |
| 6.0 | Poster | PRISMM-Bench: A Benchmark of Peer-Review Grounded Multimodal Inconsistencies | [link](https://openreview.net/forum?id=mjkGXdgm4T) |
| 6.0 | Poster | CHAMMI-75: pre-training multi-channel models with heterogeneous microscopy images | [link](https://openreview.net/forum?id=SLjqdj3LPk) |
| 6.0 | Poster | PepBenchmark: A Standardized Benchmark for Peptide Machine Learning | [link](https://openreview.net/forum?id=NskQgtSdll) |

### 优化与学习理论
**23篇** | 平均分 4.91 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.0 | Poster | Generalization Below the Edge of Stability: The Role of Data Geometry | [link](https://openreview.net/forum?id=zVmS7G6Dyi) |
| 6.0 | Poster | Separable Neural Networks: Approximation Theory, NTK Regime, and Preconditioned Gradient Descent | [link](https://openreview.net/forum?id=FlcMckO6x5) |
| 5.7 | Poster | Rewarding Doubt: A Reinforcement Learning Approach to Calibrated Confidence Expression of Large Language Models | [link](https://openreview.net/forum?id=yResLmrVO1) |
| 5.5 | Poster | BED-LLM: Intelligent Information Gathering with LLMs and Bayesian Experimental Design | [link](https://openreview.net/forum?id=qyylZMLYT8) |
| 5.5 | Poster | Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin | [link](https://openreview.net/forum?id=c5TFhCJ6fs) |

### 机器人与具身智能
**22篇** | 平均分 5.45 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.5 | Poster | AnyTouch 2: General Optical Tactile Representation Learning For Dynamic Tactile Perception | [link](https://openreview.net/forum?id=ndilONnABZ) |
| 6.0 | Poster | Empowering Multi-Robot Cooperation via Sequential World Models | [link](https://openreview.net/forum?id=IvUM6UwYCJ) |
| 6.0 | Poster | Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control | [link](https://openreview.net/forum?id=NEOTsyyYH7) |
| 6.0 | Poster | Online Navigation Refinement: Achieving Lane-Level Guidance by Associating Standard-Definition and Online Perception Maps | [link](https://openreview.net/forum?id=epbzV3FLcI) |
| 6.0 | Poster | SpatialHand: Generative Object Manipulation from 3D Prespective | [link](https://openreview.net/forum?id=VpsqfCac2B) |

### 上下文学习与提示
**21篇** | 平均分 5.16 | Oral 1篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.4 | Poster | Transformers Learn Latent Mixture Models In-Context via Mirror Descent | [link](https://openreview.net/forum?id=SHidElLSVt) |
| 6.0 | Poster | Zero-Shot Adaptation of Behavioral Foundation Models to Unseen Dynamics | [link](https://openreview.net/forum?id=dBDBg4WF4F) |
| 6.0 | Poster | COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dynamics | [link](https://openreview.net/forum?id=afV4qzquBN) |
| 6.0 | **Oral** | GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning | [link](https://openreview.net/forum?id=RQm2KQTM5r) |
| 5.6 | Poster | Multimodal Prompt Optimization: Why Not Leverage Multiple Modalities for MLLMs | [link](https://openreview.net/forum?id=M5MfDi4gJO) |

### 模型可解释性
**21篇** | 平均分 5.29 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | Poster | Using cognitive models to reveal value trade-offs in language models | [link](https://openreview.net/forum?id=nM2QhvybwI) |
| 7.0 | Poster | Command-V: Training-Free Representation Finetuning Transfer | [link](https://openreview.net/forum?id=oRYzpI3cmJ) |
| 6.5 | Poster | Spectral Attention Steering for Prompt Highlighting | [link](https://openreview.net/forum?id=XfLvGIFmAN) |
| 6.0 | Poster | Activation Steering with a Feedback Controller | [link](https://openreview.net/forum?id=vzkEX2SwFD) |
| 6.0 | Poster | LatentQA: Teaching LLMs to Decode Activations Into Natural Language | [link](https://openreview.net/forum?id=niUroX9EOd) |

### 水印与版权保护
**18篇** | 平均分 5.33 | Oral 3篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.5 | **Oral** | Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models | [link](https://openreview.net/forum?id=2eAGrunxVz) |
| 7.0 | Poster | LLMs Can Hide Text in Other Text of the Same Length | [link](https://openreview.net/forum?id=VbTLgEUocp) |
| 7.0 | Poster | PMark: Towards Robust and Distortion-free Semantic-level Watermarking with Channel Constraints | [link](https://openreview.net/forum?id=EhDgP69DJG) |
| 6.5 | **Oral** | LLM Fingerprinting via Semantically Conditioned Watermarks | [link](https://openreview.net/forum?id=t38nZqqi3Z) |
| 6.0 | **Oral** | Every Language Model Has a Forgery-Resistant Signature | [link](https://openreview.net/forum?id=vLFqOoMBol) |

### 图学习与GNN
**10篇** | 平均分 5.22 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.5 | Poster | Learning from Algorithm Feedback: One-Shot SAT Solver Guidance with GNNs | [link](https://openreview.net/forum?id=NfWrLOKnfk) |
| 5.5 | Poster | Full-Graph vs. Mini-Batch Training: Comprehensive Analysis from a Batch Size and Fan-Out Size Perspective | [link](https://openreview.net/forum?id=ZSfgsh43vT) |
| 5.5 | Poster | DHG-Bench: A Comprehensive Benchmark for Deep Hypergraph Learning | [link](https://openreview.net/forum?id=lhsb1ChUDF) |
| 5.3 | Poster | Fair Graph Machine Learning under Adversarial Missingness Processes | [link](https://openreview.net/forum?id=WgZJCnb8lJ) |
| 5.3 | Poster | GDGB: A Benchmark for Generative Dynamic Text-Attributed Graph Learning | [link](https://openreview.net/forum?id=5UFUHUC5qP) |

### 合成数据与数据增强
**9篇** | 平均分 5.50 | Oral 1篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 7.0 | **Oral** | Neon: Negative Extrapolation From Self-Training Improves Image Generation | [link](https://openreview.net/forum?id=kpLRYtPGt3) |
| 6.7 | Poster | Reformulation for Pretraining Data Augmentation | [link](https://openreview.net/forum?id=dIOYpj9K8P) |
| 6.0 | Poster | TrainRef: Curating Data with Label Distribution and Minimal Reference for Accurate Prediction and Reliable Confidence | [link](https://openreview.net/forum?id=jSs8CDsF0A) |
| 5.3 | Poster | GneissWeb: Preparing High Quality Data for LLMs at Scale | [link](https://openreview.net/forum?id=NRWUAo075J) |
| 5.3 | Poster | Matched Data, Better Models: Target Aligned Data Filtering with Sparse Features | [link](https://openreview.net/forum?id=cgmo3v18sx) |

### 时间序列与预测
**7篇** | 平均分 5.33 | Oral 0篇

**代表论文：**

| 评分 | 类型 | 标题 | 链接 |
|---|---|---|---|
| 6.0 | Poster | CTBench: Cryptocurrency Time Series Generation Benchmark | [link](https://openreview.net/forum?id=RzT2sombPD) |
| 6.0 | Poster | PYRREGULAR: A Unified Framework for Irregular Time Series, with Classification Benchmarks | [link](https://openreview.net/forum?id=qetBM8nLkf) |
| 6.0 | Poster | Conditionally Whitened Generative Models for Probabilistic Time Series Forecasting | [link](https://openreview.net/forum?id=GG01lCopSK) |
| 5.3 | Poster | Are Global Dependencies Necessary? Scalable Time Series Forecasting via Local Cross-Variate Modeling | [link](https://openreview.net/forum?id=CNVL194fO5) |
| 5.0 | Poster | TEDM: Time Series Forecasting with Elucidated Diffusion Models | [link](https://openreview.net/forum?id=kQee8MObMc) |

## 五、核心洞察与趋势

### 🔥 ICLR 2026 五大最热方向

1. **LLM推理与思维链 (383篇, 11.0%)** — 绝对霸主地位。test-time scaling、RLVR、efficient reasoning是核心子方向。社区从"让模型更大"彻底转向"让模型更会思考"。

2. **扩散模型与Flow Matching (212篇, 6.1%)** — 生成模型的理论基石。Flow Matching正在成为新的主流范式，discrete diffusion将扩散推向文本领域。

3. **LLM Agent (202篇, 5.8%)** — Agent从概念走向落地。GUI Agent、Web Agent、Research Agent、多Agent协作是主要赛道。

4. **LLM训练与预训练 (152篇, 4.4%)** — Scaling law、数据工程、训练稳定性受到高度关注。

5. **LLM推理加速 (153篇, 4.4%)** — KV Cache优化、量化、投机解码、视觉token剪枝等实用方向。

### ⭐ 最高质量方向（审稿分最高）

Haiku的语义分类揭示了一些通过关键词匹配难以发现的高质量方向：
- **测试时计算与Scaling** — 小而精的方向，Oral比例极高
- **3D生成与重建** — Gaussian Splatting带动了整个方向的繁荣
- **视频生成** — 顶级工作集中，Oral占比突出
- **语音与音频** — Speech LLM是新亮点

### 🆕 Haiku发现的新兴趋势

通过AI模型阅读每篇论文摘要，我们发现了一些仅靠关键词难以捕捉的新趋势：

1. **RLVR (RL from Verifiable Rewards)** — 结合RL和可验证奖励训练LLM推理，是DeepSeek-R1思路的学术化
2. **Visual Token Pruning/Optimization** — 多模态模型中视觉token的高效处理
3. **Research Agent** — AI辅助科研的自动化Agent
4. **Discrete Diffusion for Text** — 打破扩散模型的连续性限制
5. **Machine Unlearning** — 隐私合规驱动的新方向
6. **AI-Generated Text Detection** — 检测AI生成内容的方向快速增长
7. **World Models for Planning** — 连接生成模型和规划的桥梁

### 📚 学习路线建议

**NLP/LLM方向：**
- 必看：LLM推理(重点test-time scaling和RLVR)、Agent落地
- 关注：RLHF对齐、长上下文、代码生成
- 了解：RAG、可解释性

**生成模型方向：**
- 必看：Flow Matching理论、视频生成
- 关注：3D生成(Gaussian Splatting)、Discrete Diffusion
- 了解：图像编辑、跨模态生成

**多模态方向：**
- 必看：多模态LLM架构、多模态推理
- 关注：视觉理解、语音LLM
- 了解：视频理解、空间推理

**找新方向：**
- 推荐：Test-time Scaling、RLVR、Discrete Diffusion、Machine Unlearning、Research Agent

## 六、Top 30 必读论文

| # | 评分 | 类型 | 方向 | 标题 | 链接 |
|---|---|---|---|---|---|
| 1 | 8.0 | Oral | LLM Agent与工具使用 | Gaia2: Benchmarking LLM Agents on Dynamic and  Asynchronous Environments | [link](https://openreview.net/forum?id=9gw03JpKK4) |
| 2 | 8.0 | Oral | LLM推理与思维链 | Generative Universal Verifier as Multimodal Meta-Reasoner | [link](https://openreview.net/forum?id=DM0Y0oL33T) |
| 3 | 8.0 | Oral | 3D生成与重建 | Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator | [link](https://openreview.net/forum?id=kI27Niy4xY) |
| 4 | 8.0 | Poster | 强化学习 | Efficient Reinforcement Learning by Guiding World Models with Non-Curated Data | [link](https://openreview.net/forum?id=oBXfPyi47m) |
| 5 | 8.0 | Poster | 测试时计算与Scaling | Scaling with Collapse: Efficient and Predictable Training of LLM Families | [link](https://openreview.net/forum?id=3YKeB9R1g9) |
| 6 | 8.0 | Poster | 语音与音频 | Pay Attention to CTC: Fast and Robust Pseudo-Labelling for Unified Speech Recognition | [link](https://openreview.net/forum?id=sSbEEHNEsL) |
| 7 | 8.0 | Poster | 3D生成与重建 | $\pi^3$: Permutation-Equivariant Visual Geometry Learning | [link](https://openreview.net/forum?id=DTQIjngDta) |
| 8 | 7.5 | Oral | 强化学习 | TD-JEPA: Latent-predictive Representations for Zero-Shot Reinforcement Learning | [link](https://openreview.net/forum?id=SzXDuBN8M1) |
| 9 | 7.5 | Oral | LLM推理与思维链 | Reasoning with Sampling: Your Base Model is Smarter Than You Think | [link](https://openreview.net/forum?id=Vsgq2ldr4K) |
| 10 | 7.5 | Oral | 代码生成与验证 | EditBench: Evaluating LLM Abilities to Perform Real-World Instructed Code Edits | [link](https://openreview.net/forum?id=FtL9eEmU6v) |
| 11 | 7.5 | Oral | 测试时计算与Scaling | Pre-training under infinite compute | [link](https://openreview.net/forum?id=ck0aZTAnwK) |
| 12 | 7.5 | Oral | 测试时计算与Scaling | The Art of Scaling Reinforcement Learning Compute for LLMs | [link](https://openreview.net/forum?id=FMjeC9Msws) |
| 13 | 7.5 | Oral | 图像生成与编辑 | Quotient-Space Diffusion Model | [link](https://openreview.net/forum?id=3JPAkwSVc4) |
| 14 | 7.5 | Oral | 水印与版权保护 | Spherical Watermark: Encryption-Free, Lossless Watermarking for Diffusion Models | [link](https://openreview.net/forum?id=2eAGrunxVz) |
| 15 | 7.5 | Poster | RLHF与对齐 | Persona Features Control Emergent Misalignment | [link](https://openreview.net/forum?id=yjrVOxjkDR) |
| 16 | 7.5 | Poster | 隐私与联邦学习 | Back to Square Roots: An Optimal Bound on the Matrix Factorization Error for Multi-Epoch Differentially Private SGD | [link](https://openreview.net/forum?id=EEr6cADbZx) |
| 17 | 7.5 | Poster | 语音与音频 | StableToken: A Noise-Robust Semantic Speech Tokenizer for Resilient SpeechLLMs | [link](https://openreview.net/forum?id=17DNmdQ9aU) |
| 18 | 7.5 | Poster | 图像生成与编辑 | FullPart: Generating each 3D Part at Full Resolution | [link](https://openreview.net/forum?id=QlRlE7a1p4) |
| 19 | 7.5 | Poster | 图像生成与编辑 | TEMPFLOW-GRPO: WHEN TIMING MATTERS FOR GRPO IN FLOW MODELS | [link](https://openreview.net/forum?id=7mCo3R3Wyn) |
| 20 | 7.3 | Oral | 强化学习 | Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling | [link](https://openreview.net/forum?id=lTaPtGiUUc) |
| 21 | 7.3 | Oral | LLM Agent与工具使用 | In-The-Flow Agentic System Optimization for Effective Planning and Tool Use | [link](https://openreview.net/forum?id=Mf5AleTUVK) |
| 22 | 7.3 | Oral | 图像生成与编辑 | DiffusionNFT: Online Diffusion Reinforcement with Forward Process | [link](https://openreview.net/forum?id=VJZ477R89F) |
| 23 | 7.3 | Poster | 强化学习 | Safe Exploration via Policy Priors | [link](https://openreview.net/forum?id=JC8xYAADHL) |
| 24 | 7.3 | Poster | LLM Agent与工具使用 | Improving Human-AI Coordination through Online Adversarial Training and Generative Models | [link](https://openreview.net/forum?id=AeehNfbHqD) |
| 25 | 7.3 | Poster | LLM Agent与工具使用 | Multimodal Policy Internalization for Conversational Agents | [link](https://openreview.net/forum?id=fSE0rUngCX) |
| 26 | 7.3 | Poster | LLM Agent与工具使用 | FutureX: An Advanced Live Benchmark for LLM Agents in Future Prediction | [link](https://openreview.net/forum?id=z28PLIEj6l) |
| 27 | 7.3 | Poster | LLM Agent与工具使用 | Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces | [link](https://openreview.net/forum?id=a7Qa4CcHak) |
| 28 | 7.3 | Poster | LLM Agent与工具使用 | Virtual Community: An Open World for Humans, Robots, and Society | [link](https://openreview.net/forum?id=Qo0OZZoTLh) |
| 29 | 7.3 | Poster | LLM推理与思维链 | Nemotron-CC-Math: A 133 Billion-Token-Scale High Quality Math Pretraining Dataset | [link](https://openreview.net/forum?id=rhPnkTKfMy) |
| 30 | 7.3 | Poster | 视觉理解与检测 | InclusiveVidPose: Bridging the Pose Estimation Gap for Individuals with Limb Deficiencies in Video-Based Motion | [link](https://openreview.net/forum?id=SyQqXAdWUq) |