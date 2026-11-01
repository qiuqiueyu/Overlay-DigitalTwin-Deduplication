# 基于实例去重的云数据中心 Overlay 数字孪生等效建模
# Cloud Data Center Overlay Digital Twin Simulation Based on Instance Deduplication

本仓库包含论文 **《基于实例去重的云数据中心Overlay数字孪生等效建模》** 的核心评估源代码与可视化脚本。
This repository contains the core evaluation source code and visualization scripts for the paper:  
**"Equivalent Modeling of Cloud Data Center Overlay Digital Twin Based on Instance Deduplication"**.

---

## 📌 摘要 / Abstract

**中文：** 随着基于大语言模型（LLM）的意图驱动网络（IBN）在云数据中心的快速发展，数字孪生已成为验证网络意图、防止配置幻觉的关键沙盒。然而，传统基于物理拓扑的 1:1 全量仿真，在面对分布式网关（EVPN-VXLAN）带来的海量物理实例复制时，会导致严重的资源爆炸。

本文提出了一种面向 Overlay 逻辑层的轻量化数字孪生建模方法。该方法对分布式散落在多台 Leaf 交换机上的虚拟路由转发（VRF）与桥接域（BD）实例进行“逻辑去重”，成功将数字孪生网络的状态空间复杂度从 \(O(N^2 + T \cdot N)\) 降至 O(T)。多维蒙特卡洛模拟实验表明：在保障验证完全等效的前提下，本方法在包含 100 台 Leaf 交换机及 300 个租户的超大规模网络场景下实现了高达 **61.78 倍的资源空间压缩**。

**English:** With the rapid evolution of Intent-Driven Networks (IBN) powered by Large Language Models (LLMs) in cloud data centers, digital twins have emerged as a critical sandbox to verify network intents and prevent LLM hallucinations. However, traditional 1:1 full-scale simulation based on Underlay physical topologies suffers from severe resource explosion. 

To achieve second-level closed-loop verification, this paper proposes a lightweight digital twin modeling method oriented toward the Overlay logical layer. By performing "logical deduplication" on Virtual Routing and Forwarding (VRF) and Bridge Domain (BD) instances, the twin state space complexity is theoretically reduced from \(O(N^2 + T \cdot N)\) to O(T). Multi-dimensional Monte Carlo simulations demonstrate up to a **61.78-fold resource space compression** in a large-scale network scenario featuring 100 Leaf switches and 300 tenants.

---

## 📁 仓库结构 / Repository Structure

```text
├── overlay_dt_simulation.py    # 主程序：核心蒙特卡洛仿真与双轴高清学术图表绘制
│                               # Main script: Core Monte Carlo simulation & Dual-Y plotting
├── requirements.txt            # 环境基础依赖包 / Minimal environment dependencies
└── README.md                   # 仓库说明文档 / Repository documentation
```

---

## 🛠️ 快速开始与复现 / Quick Start & Replication

按照以下步骤，您可以轻松复现论文中实验部分的所有数据表（Table 1）与演进趋势图（Figure 2）。
Follow these simple steps to replicate all data tables (Table 1) and figures (Figure 2) presented in the paper.

### 1. 环境准备 / Environment Setup
推荐使用 Python 3.8+ 环境，安装极简的第三方依赖库：
We recommend using Python 3.8+ with minimal environment dependencies:
```bash
pip install -r requirements.txt
```

### 2. 运行仿真 / Execution
直接执行重命名后的核心仿真脚本：
Run the core simulation script:
```bash
python overlay_dt_simulation.py
```

---

## 📊 预期输出 / Expected Outputs

运行脚本后，系统会自动完成以下两项任务：
Upon running the script, the system will automatically:

1. **终端打印数据横截面 / Print Cross-Sectional Data**: 
   控制台将直接打印出 `TABLE I`，其数据与论文第 4 节表 1 的实验测量数据完全一致。
   Output `TABLE I` in your terminal, aligning perfectly with the paper's experimental section.

2. **导出高清学术图表 / Export Academic-Grade Visualization**: 
   在当前目录下自动保存一张 300 DPI 的高质量双 Y 轴曲线对比图 `fig2_simulation_results.png`（对应论文中的图 2）。
   Save a 300 DPI high-resolution dual-axis curve chart named `fig2_simulation_results.png`, visualizing the state space comparison and compression scaling trends.

---

## 🚀 路线图 / Development Roadmap

- [x] **Phase 1**: 数学模型验证与蒙特卡洛随机模拟核心底座完成。 / Mathematical verification & Core Monte Carlo simulation evaluation base.
- [ ] **Phase 2**: 开源现网配置解析器与 Underlay 到 Overlay 的自动化映射翻译流水线。 / Open-sourcing the automated configuration parser and Underlay-to-Overlay mapping translation pipelines.
- [ ] **Phase 3**: 融合基于俄罗斯科学院院士团队研发的 RunOS 级 SDN 控制器动态状态同步器。 / RunOS SDN controller-level state synchronizer integration.

*注：Phase 1 的代码已完全实现并在论文评审期间冻结。Phase 2 和 Phase 3 的功能目前正在积极开发中。*  
*Note: The code for Phase 1 is fully functional and frozen for paper review. Extensions for Phase 2 and 3 are under active development.*
