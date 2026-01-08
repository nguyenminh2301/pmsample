# 预后研究样本量计算器 (Prognostic Research Sample Size Tool)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

这是一款用于计算临床预后研究最小样本量的工具包。专为数据科学家、统计学家和临床研究人员设计，本应用实现了经过验证的统计方法，用于 **预测模型开发**、**外部验证**、**预后因素研究** 和 **模型更新**。

🔗 **访问应用:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **注意**: 本应用的中文、日文、法文、德文部分内容由 AI 辅助翻译完成。如有任何疑问，请联系应用管理员。

---

## 1. 概述与目的

本应用提供了一套工具来解决医学研究中样本量规划的复杂要求。与基本的功效计算器不同，本工具专注于 *预后建模* 的具体细节，其目标通常是精确估计风险（校准和区分度），而不仅仅是单纯的假设检验。

### 主要功能

* **方法论严谨性**: 算法严格遵循同行评审的统计文献 (Riley et al., Hanley & McNeil, Hsieh, et al.)。
* **验证**: 核心计算已与权威的 R 包 (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) 进行对照，以确准确性。
* **多语言支持**: 支持英语、越南语，并部分支持中文、日文、法文、德文，促进国际合作。
* **敏感性分析**: 集成批处理功能，允许研究人员评估在各种假设（例如：变化的患病率或预期的 $R^2$）下样本量要求的变化。

---

## 2. 方法目录

本应用分为四个主要模块，每个模块针对研究周期的特定阶段。

### A. 初步可行性评估

| 方法 | 描述 | 应用场景 |
| :--- | :--- | :--- |
| **A1: 每变量事件数 (EPV/EPP)** | 基于事件数与候选预测参数之比的经验法则。 | *仅用于可行性检查。* **不建议作为研究方案的主要依据**，因为它未考虑过拟合或校准。 |
| **A2: 基线风险精度** | 估计以指定置信区间 (CI) 宽度估计患病率所需的样本量。 | 描述性流行病学；规划整体校准 (calibration-in-the-large)。 |

### B. 预后因素研究 (关联性)

| 方法 | 描述 | 参考 |
| :--- | :--- | :--- |
| **B3: Logistic 回归功效** | 计算检测特定预测变量的目标比数比 (OR) 所需的样本量，并在调整与其他因素的协方差后进行修正。 | **Hsieh et al. (1998)** |
| **B4: Cox 回归功效** | 计算生存分析中检测目标风险比 (HR) 所需的事件数。 | **Schoenfeld (1983)** |

### C. 预测模型开发 (推荐)

这是构建新临床预测模型的核心模块。

| 方法 | 描述 | 主要目标 |
| :--- | :--- | :--- |
| **C5: 解析法 (Riley)** | **金标准。** 多变量模型开发的闭式解。 | 1. 限制全局收缩 (shrinkage $S \ge 0.9$)。<br />2. 限制表观性能的乐观偏差。<br />3. 精确估计截距系数。 |
| **C6: 基于模拟的设计** | 模拟特定的数据生成机制 (DGM) 以估计复杂模型的要求。 | 非线性项、复杂交互作用、特定的相关结构。 |
| **C7: 贝叶斯保证 (Assurance)** | 基于 MCMC 的模拟，以确定具有保证成功概率 (Assurance) 的样本量。 | 贝叶斯模型开发。 |

### D. 验证与更新

用于规划现有模型的外部验证的工具。

| 方法 | 描述 | 参考 |
| :--- | :--- | :--- |
| **D8: AUC 精度** | 计算 N 以达到 AUC (C-statistic) 的特定置信区间宽度。 | **Hanley & McNeil (1982)** |
| **D9: 定制验证规模** | 计算 N 以确精确估计 O/E 比、校准斜率 (Calibration Slope) 和 AUC。 | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: 验证模拟** | 使用线性预测器 (LP) 分布的基于模拟的规划。 | **Snell et al. (2021)** |
| **D11: 模型更新** | 更新 (重新校准) 现有模型 (截距/斜率) 以适应新环境所需的样本量。 | **Van Calster et al.** |

---

## 3. 安装与本地运行

要在您自己的基础设施上部署此应用程序：

### 先决条件

* Python 3.9 或更高版本
* Git

### 部署步骤

1. **克隆仓库 (Clone)**

   ```bash
   git clone https://github.com/nguyenminh2301/pmsample.git
   cd pmsample
   ```

2. **环境设置**
   建议使用虚拟环境 (virtual environment)。

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **安装依赖**

   ```bash
   pip install -r requirements.txt
   ```

4. **启动应用**

   ```bash
   streamlit run pmsampsize_app/app.py
   ```

---

## 4. 免责声明

**仅供学术和研究使用。**

本软件是同行评审文献中发表的统计方法的实现。尽管已尽一切努力确保算法的准确性，但作者和维护者不对基于此工具的任何研究的设计或结果承担责任。

* **用户责任**: 用户负责验证输入参数并在其特定的临床背景下解释结果。
* **无医疗保证**: 本工具不提供医疗建议。

---

**作者与维护:**
Minh Nguyen (minhnt@ump.edu.vn)
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
(Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam)
