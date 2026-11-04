# 基于实例去重的云数据中心 Overlay 数字孪生等效建模
# Cloud Data Center Overlay Digital Twin Simulation Based on Instance Deduplication
# Эквивалентное моделирование цифрового двойника Overlay для облачных дата-центров на основе дедупликации экземпляров

---

## 🔄 实时文档同步 / Real-time Document Synchronization / Синхронизация документов
> **[CN] 💡 提示：** 本项目的最新学术进展、修改日志及详细文档已同步至飞书，请点击以下链接查看实时更新：  
> 👉 **[飞书实时同步文档](https://scnysyqbipqq.feishu.cn/docx/Peh1dJfU5oKA5Oxo3rtc4VqEnad)**  
> 
> **[EN] 💡 Notice:** The latest academic progress, modification logs, and detailed documentation of this project have been synchronized to Feishu. Please click the link below for real-time updates:  
> 👉 **[Feishu Live Document](https://scnysyqbipqq.feishu.cn/docx/Peh1dJfU5oKA5Oxo3rtc4VqEnad)**  
> 
> **[RU] 💡 Примечание:** Последние научные достижения, журналы изменений и подробная документация по этому проекту синхронизированы в Feishu. Перейдите по ссылке ниже для получения обновлений в реальном времени:  
> 👉 **[Синхронизированный документ Feishu](https://scnysyqbipqq.feishu.cn/docx/Peh1dJfU5oKA5Oxo3rtc4VqEnad)**  

---

## 📌 摘要 / Abstract / Аннотация

**[CN]** 随着基于大语言模型（LLM）的意图驱动网络（IBN）在云数据中心的快速发展，数字孪生已成为验证网络意图、防止 LLM 产生配置幻觉的关键沙盒。本文提出了一种面向 Overlay 逻辑层的轻量化数字孪生建模方法。通过对分布式散落在多台 Leaf 交换机上的虚拟路由转发（VRF）与桥接域（BD）实例进行“逻辑去重”，成功将数字孪生网络的状态空间复杂度从 \(O(N^2+T \cdot N)\) 降至 O(T)。多维蒙特卡洛模拟实验表明：在保障验证完全等效的前提下，本方法在包含 100 台 Leaf 交换机及 300 个租户的超大规模网络场景下实现了高达 **61.78 倍的资源空间压缩**。

**[EN]** With the rapid evolution of Intent-Driven Networks (IBN) powered by Large Language Models (LLMs) in cloud data centers, digital twins have emerged as a critical sandbox to verify network intents and prevent LLM hallucinations. This paper proposes a lightweight digital twin modeling method oriented toward the Overlay logical layer. By performing "logical deduplication" on Virtual Routing and Forwarding (VRF) and Bridge Domain (BD) instances, the twin state space complexity is theoretically reduced from \(O(N^2 + T \cdot N)\) to O(T). Multi-dimensional Monte Carlo simulations demonstrate up to a **61.78-fold resource space compression** in a large-scale network scenario featuring 100 Leaf switches and 300 tenants.

**[RU]** С быстрым развитием сетей, управляемых намерениями (IBN) на базе больших языковых моделей (LLM) в облачных дата-центрах, цифровые двойники стали важнейшей песочницей для проверки сетевых намерений и предотвращения галлюцинаций конфигурации LLM. В данной работе предлагается легковесный метод моделирования цифрового двойника, ориентированный на логический уровень Overlay. За счет выполнения «логической дедупликации» экземпляров VRF и BD, распределенных по нескольким коммутаторам Leaf, сложность пространства состояний сети цифрового двойника теоретически снижается с \(O(N^2 + T \cdot N)\) до O(T). Многомерное моделирование методом Монте-Карло показывает, что при обеспечении полной эквивалентности верификации данный метод позволяет достичь до **61,78-кратного сжатия ресурсного пространства** в крупномасштабном сетевом сценарии со 100 коммутаторами Leaf и 300 арендаторами.

---

## 📁 仓库文件结构 / Repository Structure / Структура репозитория

```text
├── overlay_dt_simulation.py    # 仿真核心 Python 脚本 / Core simulation script / Основной скрипт симуляции
├── requirements.txt             # 环境基础依赖包 / Minimal dependencies / Минимальные зависимости среды
├── Инструкция на русском языке.pdf # 俄罗斯语说明 / Russian manual / Инструкция на русском
├── 示意图.svg                   # 架构对比图 (SVG) / Architecture diagram / Схема архитектуры
└── readme.md                   # 本说明文档 / Repository documentation / Этот документ
```

---

## 🛠️ 快速开始与复现 / Quick Start & Replication / Быстрый запуск и репликация

### 1. 环境准备 / Environment Setup / Настройка среды
```bash
pip install -r requirments.txt
```

### 2. 运行仿真 / Execution / Запуск симуляции
```bash
python overlay_dt_simulation.py
```
运行脚本后，系统会在终端打印出实验截面数据表（TABLE I），并在当前目录下自动保存高清学术对比曲线图 `fig2_simulation_results.png`。  
After running, the script outputs `TABLE I` in the terminal and automatically saves the high-res figure `fig2_simulation_results.png` in the current directory.  
После запуска скрипт выведет `TABLE I` в терминале и автоматически сохранит график высокого разрешения `fig2_simulation_results.png` в текущем каталоге.

---

## 🚀 路线图 / Development Roadmap / План развития

- [x] **Phase 1**: 数学模型验证与蒙特卡洛随机模拟核心底座完成。 / Mathematical verification & Core Monte Carlo simulation base completed. / Математическая верификация и база симуляции Монте-Карло завершены.
- [ ] **Phase 2**: 开源现网配置解析器与 Underlay 到 Overlay 的自动化映射翻译流水线。 / Open-sourcing the automated configuration parser and Underlay-to-Overlay mapping translation pipelines. / Открытие исходного кода парсера конфигурации и конвейера трансляции Underlay-в-Overlay.
- [ ] **Phase 3**: 融合基于 RunOS 级 SDN 控制器动态状态同步器。 / RunOS SDN controller-level state synchronizer integration. / Интеграция синхронизатора состояний динамического контроллера SDN уровня RunOS.
