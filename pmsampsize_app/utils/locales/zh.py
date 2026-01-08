
ZH = {
    "title": "预后研究样本量计算工具 (Prognostic Research Sample Size Tool)",
    "sidebar_title": "配置 (Configuration)",
    "language": "语言 / Language",
    "mode": "方法选择 (Method Selection)",
    "mode_riley": "方法 C5: Riley 等 (解析法)",
    "mode_bayes": "方法 C6: 贝叶斯主要 (模拟)",
    "mode_single": "单一场景 (Single Scenario)",
    "mode_batch": "敏感性分析 (Sensitivity Analysis)",
    "method1_tab": "方法 C5 (Riley)",
    "method2_tab": "方法 C6 (Bayesian)",
    "nav_title": "导航 (Navigation)",
    "nav_readme": "详细文档 (README)",
    "nav_intro": "介绍与公式 (Introduction & Formulas)",
    "nav_calc": "样本量计算器 (Calculator)",
    "intro_heading": "欢迎 (Welcome)",
    "intro_text": "本工具帮助研究人员计算开发二分类结果临床预测模型所需的最小样本量。",
    "formula_heading": "数学框架 (方法 C5)",
    "formula_intro": "方法 C5 使用 Riley 等人提供的解析解，而方法 C6 使用贝叶斯 MCMC 模拟。",
    "sens_guide_title": "💡 如何使用敏感性分析 (批处理模式)",
    "sens_guide_text": """
    - **范围**: 输入 `min-max` (例如 `0.05-0.10`)。应用将自动生成步骤。
    - **特定值**: 输入逗号分隔列表 (例如 `0.05, 0.10, 0.15`)。
    """,
    "detail_view": "查看场景详细计算",
    "footer_refs": "参考文献: Riley et al. (2018, 2020), BayesAssurance.",
    "calc_btn": "计算 (Calculate)",
    "results": "结果 (Results)",
    "sanity": "合理性检查 (Sanity Check - EPV Rules)",
    "download_csv": "下载 CSV",
    "download_report": "下载完整报告",
    "error_p": "患病率必须在 0 和 1 之间。",
    "error_auc": "AUC 必须在 0.5 和 1 之间。",
    "error_parse": "无法解析输入。",
    
    # Riley specific
    "riley_inputs": "输入参数 (Riley)",
    "prevalence": "结果患病率 / 事件发生率 (Outcome Prevalence / Event Rate)",
    "prevalence_help": "参与者发生事件的比例 (0 < p < 1)。",
    "parameters": "预测参数数量 (Number of Predictor Parameters/df)",
    "parameters_help": "总自由度 (不包括截距)。",
    "shrinkage": "目标全局收缩率 (Target Global Shrinkage, S)",
    "shrinkage_help": "期望的收缩因子 (默认 0.9)。",
    "perf_measure": "预期性能 (Anticipated Performance)",
    "perf_auc": "AUC (C-统计量)",
    "perf_r2": "Cox-Snell R-squared",
    "perf_cons": "保守估计 (最大 R2 的 15%)",
    
    # Bayesian specific 
    "perf_cons_help": "保守估计 (最大 R2 的 15%)",
    "perf_auc_help": "预期 AUC (C-统计量)",
    "perf_r2_help": "预期 Cox-Snell R-squared",
    
    # Bayesian specific
    "bayes_inputs": "模拟设置 (贝叶斯保证)",
    "dgm_settings": "数据生成机制 (Data Generating Mechanism)",
    "sim_settings": "模拟与 MCMC (Simulation & MCMC)",
    "eval_settings": "评估标准 (Evaluation Criteria)",
    "n_candidates": "候选样本量 (逗号分隔)",
    "n_candidates_help": "要测试的 N 值列表，例如 500, 1000, 1500。",
    "correlation": "预测因子相关性 (rho)",
    "n_sims": "每个 N 的模拟次数",
    "assurance_threshold": "保证阈值 (目标概率, Assurance Threshold)",
    "run_simulation": "运行贝叶斯模拟",
    "simulation_running": "正在运行模拟... 这可能需要一些时间。",
    "assurance_result": "保证分析 (Assurance Analysis)",
    
    # Method 6 (Dev Sim)
    "mode_dev_sim": "方法 6: 开发模拟 (频率学派)",
    "method6_tab": "方法 6 (模拟)",
    "dev_sim_intro": "基于模拟的模型开发样本量计算 (频率学派方法，类似于 `samplesizedev`)。",
    "dev_mode_simple": "模式 A: 简单 (AUC 驱动)",
    "dev_mode_custom": "模式 B: 自定义 DGM",
    "target_auc": "目标平均 AUC (C-统计量)",
    "target_auc_help": "算法将寻找 Beta 系数以实现此 AUC。",
    "criteria_settings": "性能标准 (通过/失败)",
    "crit_slope_mean": "平均校准斜率 (Calibration Slope) >= 0.9",
    "crit_slope_ci": "Pr(0.9 <= Slope <= 1.1) >= 80%",
    "crit_auc": "平均 AUC >= 目标值",
    "audit_trail": "RNG 审计跟踪 (JSON)",
    "future_methods": "即将推出的版本...",
    
    # Quick Methods
    "method_quick_tab": "A. 快速 / 基础 (Quick / Basic)",
    "quick_mode_epv": "A1: EPV / EPP 规则 (启发式)",
    "quick_mode_risk": "A2: 基线风险精度 (CI 宽度)",
    "target_epv": "目标每参数事件数 (EPP)",
    "target_epv_help": "常见的启发式值为 10, 15, 20。EPP 优于 EPV。",
    "epv_warning_title": "⚠️ 重要警告",
    "epv_warning_text": "EPV/EPP 只是粗略的启发式规则。它不能保证校准、区分度，也不能防止乐观偏差。它对变量选择和非线性项敏感。",
    "ci_level": "置信水平 (Confidence Level)",
    "ci_half_width": "目标半宽 (误差边际, Margin of Error)",
    "ci_method": "CI 方法",
    "ci_method_wilson": "Wilson Score (推荐)",
    "ci_method_wald": "Wald (简单)",
    "ci_method_cp": "Clopper-Pearson (保守)",
    "risk_help": "计算估计特定精度的事件发生率 p 所需的 N。不保证预测模型性能。",
    
    # Power Methods (B)
    "title_b3": "B3: Logistic 功效 (Hsieh)",
    "title_b4": "B4: Cox 功效 (Schoenfeld)",
    "interpretation": "解释 (Interpretation)",
    
    # UI Basics
    "d8_assumptions": "**假设**: 使用 Hanley & McNeil (1982) 方差近似。AUC 对称正态假设。数值优化寻找 N。",
    "d8_mode_n_to_width": "从 N 计算 CI 宽度",
    "d8_mode_width_to_n": "从 CI 宽度计算所需 N",
    "d8_opt_settings": "高级优化器设置",
    "d8_practical_rounding": "显示实际取整",
    "d8_n_input": "样本量 (N)",
    "d8_width_input": "CI 宽度 (总)",
    "d8_opt_bound": "搜索上限",
    "d8_opt_tol": "容差",
    
    # Validations (D)
    "title_d8": "D8: AUC 精度 (Hanley-McNeil)",
    "d8_desc": "计算以所需精度 (CI 宽度) 估计 AUC 的样本量。",
    "auc_expected": "预期 AUC (C-统计量)",
    "formulas_header": "📚 公式与技术细节 (Formulas & Technical Details)",
    "d8_assumptions": "**假设**: 使用 Hanley & McNeil (1982) 方差近似。AUC 对称正态假设。数值优化寻找 N。",
    "d8_mode_n_to_width": "从 N 计算 CI 宽度",
    "d8_mode_width_to_n": "从 CI 宽度计算 N",
    "d8_opt_settings": "高级优化器设置",
    "d8_practical_rounding": "显示实际取整",
    "d8_n_input": "样本量 (N)",
    "d8_width_input": "CI 宽度 (总)",
    "d8_opt_bound": "搜索上限",
    "d8_opt_tol": "容差",
    
    # D9
    "title_d9": "D9: 外部验证 (Tailored)",
    "common_inputs": "通用参数",
    
    # UI Basics
    "search_placeholder": "搜索方法...",
    "settings": "设置 (Settings)",
    
    # Footer
    "footer_copyright": "© 2026 预后研究样本量计算工具。仅供学术/研究使用。",
    "footer_author": "作者与维护: Minh Nguyen (minhnt@ump.edu.vn) - Dept. of Epidemiology, Faculty of Public Health, UMP Ho Chi Minh City",
    "footer_disclaimer": "免责声明: 无临床保证；用户负责验证和解释。",

    "intro_complete_md": """
### 欢迎 (Welcome)

本应用帮助临床医生和研究人员规划预后研究的最小样本量，包括：
* 预后因素研究 (检测关联的功效)，
* 临床预测模型开发 (风险预测)，以及
* 模型验证 / 更新 (外部验证，重新校准)。

它专为二分类结果 (例如：事件 vs 无事件) 设计，部分模块也适用于生存时间结果 (Cox PH)。

源代码 (下载): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
或 [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)    

###以此开始 (新用户)

#### 1. 明确您的研究目标
* 您是在测试单个预后因素 (关联性) 吗？
* 您是在构建预测模型吗？
* 您是在新人群中验证现有模型吗？

#### 2. 估计事件发生率 $p$ (或生存分析的事件分数)
* 首选当地医院数据 (最佳)。
* 如果不确定，请输入一个范围并运行敏感性分析。

#### 3. 正确计算模型复杂性 (参数 / 自由度)
使用参数 (自由度)，而不仅仅是“变量数量”。
* 二分类预测变量: 1 df
* 具有 $L$ 个水平的分类变量: $L-1$ df
* 样条 (具有 $K$ 个节点的 RCS): $K-1$ df
* 交互作用: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. 从下面的目录中选择一种方法
* **"快速工具" (Quick tools)** 仅用于粗略规划。
* 开发预测模型时使用 **Riley / 模拟 / 保证 (Assurance)** 方法。

---

### 何时使用此应用 (以及何时不使用)

**在以下情况下使用此应用:**
* 规划预后/预测方面的回顾性或前瞻性队列研究
* 开发或验证风险预测模型
* 根据流行率或 AUC 的精度 (CI 宽度) 估计样本量
* 设计具有校准和区分度目标的外部验证

**在以下情况下不要将此应用作为主要工具:**
* 设计随机对照试验 (使用 RCT 特定的功效/样本量方法)
* 在没有预测建模的情况下规划敏感性/特异性的诊断准确性研究
* 期望一个单一的“正确”数字：样本量规划需要假设，并且应包括敏感性分析

---

### 可用方法 (概览)

#### A. 快速 / 基础 (快速，近似)

**A1 — 经验法则 (EPV/EPP) (启发式)**
* **适用情况:** 您需要快速检查事件对于计划的模型规模是否“大致足够”。
* **不适用情况:** 模型包含样条/交互作用/变量选择，或事件发生率低——EPV/EPP 不能保证良好的校准或低乐观偏差。
* **主要输入:** 事件发生率 $p$, 参数数量 $P$ (df), 目标 EPP (例如 10/15/20)
* **核心输出:** 所需事件 $E=t \\cdot P$, 所需样本量 $N=\\lceil E/p \\rceil$
* **优点:** 极其简单；适合早期可行性研究
* **缺点:** 可能具有误导性；非基于性能

**A2 — 基线风险精度 (患病率的 CI 宽度)**
* **适用情况:** 您的目标是以所需的 CI 半宽 (例如 ±2%) 估计事件发生率 $p$。
* **不适用情况:** 您想要预测模型性能保证 (AUC/校准斜率)。
* **主要输入:** 预期 $p$, CI 方法 (推荐 Wilson), 置信水平, 目标半宽 $d$
* **核心输出:** 满足 CI 半宽 $\\le d$ 的最小 $N$
* **优点:** 直接的精度目标；假设透明
* **缺点:** 仅关于患病率，而非模型性能

#### B. 预后因素 (功效) (关注关联性，而非预测模型大小)

**B3 — Logistic OR 功效 (Hsieh)**
* **适用情况:** 您希望在 Logistic 回归中检测预后因素的目标比值比 (OR) 的功效。
* **不适用情况:** 您的主要目标是预测模型开发 (校准/区分度)，而不是假设检验。
* **主要输入:** 基线风险 $p_0$, 目标 OR, Alpha, 功效, 暴露患病率 (二分类) 或 SD (连续), 可选的与其他协变量的 $R^2$
* **核心输出:** 检测 OR 所需的 $N$ (及隐含事件数)
* **优点:** 用于关联性的经典功效框架
* **缺点:** 不解决预测模型性能问题；对输入假设敏感

**B4 — Cox HR 功效 (Schoenfeld)**
* **适用情况:** 生存时间结果；您希望在 Cox PH 下检测风险比 (HR) 的功效。
* **不适用情况:** PH 假设可能被违反，或事件分数高度不确定且无法合理估计。
* **主要输入:** HR, Alpha, 功效, 分配比例 (二分类) 或 SD (连续), 随访期间的预期事件分数
* **核心输出:** 所需事件数；使用事件分数转换为 $N$
* **优点:** 广泛接受；基于事件的规划直观
* **缺点:** 强烈依赖于事件分数和随访/删失假设

#### C. 预测模型开发 (推荐用于风险模型构建)

**C5 — Riley 等 (解析法; 类似 pmsampsize)**
* **适用情况:** 开发多变量预测模型；您希望控制过拟合均确保足够的精度。
* **不适用情况:** 您无法提供患病率和预期模型性能 (AUC 或 $R^2$) 的合理假设；在这种情况下，使用敏感性分析或模拟。
* **主要输入:** 事件发生率 $p$, 参数 $P$ (df), 目标收缩率 (例如 0.90), 预期模型性能 (AUC 或 Cox–Snell $R^2$)
* **核心输出:** 满足多个标准的最小 $N$ (过拟合控制 + 精度)
* **优点:** 基于原则，关注性能，被广泛引用
* **缺点:** 依赖于性能假设；需要仔细计算 df

**C6 — 开发模拟 (频率学派; samplesizedev/自定义 DGM)**
* **适用情况:** 您更喜欢“模拟您将要做的事情”，特别是存在非线性/交互作用和自定义数据结构时。
* **不适用情况:** 您无法指定合理的数据生成机制 (DGM) 或您需要即时结果 (计算密集型)。
* **主要输入:** 候选 $N$ 网格, DGM 假设 (预测变量分布/相关性/效应), 性能目标 (例如 校准斜率范围, AUC 阈值), 模拟重复次数, 种子
* **核心输出:** 以可接受的概率/精度达到目标的最小 $N$
* **优点:** 灵活；与复杂建模一致
* **缺点:** 假设繁重；计算成本高

**C7 — 贝叶斯保证 (MCMC)**
* **适用情况:** 最终模型将使用贝叶斯 MCMC 估计，并且您希望基于保证 (满足后验性能/精度目标的概率) 的样本量。
* **不适用情况:** 先验无法证明或计算预算有限。
* **主要输入:** DGM, 先验, 候选 $N$, MCMC 设置, 保证阈值 (例如 80%/90%), 性能/精度目标
* **核心输出:** 满足保证阈值的最小 $N$
* **优点:** 与贝叶斯工作流程一致；直接针对后验标准
* **缺点:** 计算密集型；需要先验规范

#### D. 验证 / 更新 (用于现有模型)

**D8 — AUC 精度 (Hanley–McNeil / presize)**
* **适用情况:** 您的验证目标是 AUC 的精度 (CI 宽度)。
* **不适用情况:** 校准 (斜率/CITL) 是主要关注点——此方法仅针对 AUC。
* **主要输入:** 预期 AUC, 患病率或病例对照比, 置信水平, 目标 CI 宽度
* **核心输出:** 达到所需 AUC CI 宽度的最小 $N$
* **优点:** 简单；用于区分度精度的快速规划
* **缺点:** 近似方差；忽略校准

**D9 — 外部验证 (Tailored; pmvalsampsize / sampsizeval)**
* **适用情况:** 您希望针对多个性能指标 (校准 + 区分度) 进行验证规模确定，通常需要关于 LP 分布的假设。
* **不适用情况:** 您无法证明 LP 分布假设或预期性能。
* **主要输入:** 患病率, 预期 AUC, 校准斜率/CITL 目标, CI 宽度或 SE 目标, LP 分布假设
* **核心输出:** 满足各指标精度标准的推荐 $N$
* **优点:**以此定制；关注校准
* **缺点:** 需要额外假设；更复杂

**D10 — 外部验证 (模拟; 基于 LP)**
* **适用情况:** 您可以指定/估计目标验证人群中线性预测器 (LP) 的分布，并希望进行基于模拟的精度规划。
* **不适用情况:** LP 分布未知且无法近似。
* **主要输入:** LP 分布 (正态/Beta/经验), 误校准参数, 指标的 CI 宽度目标, 重复次数, 种子
* **核心输出:** 模拟下达到精度目标的最小 $N$
* **优点:** 非常灵活；匹配“模拟您的预期”
* **缺点:** 假设繁重；计算成本高

**D11 — 更新 / 重新校准 (截距/斜率)**
* **适用情况:** 您将重新校准现有模型 (更新截距和/或斜率) 并需要足够的精度。
* **不适用情况:** 您正在开发全新的模型 (使用 C5–C7)。
* **主要输入:** 更新类型 (仅截距 vs 截距+斜率), 事件发生率, 精度目标
* **核心输出:** 足以进行稳定更新的 $N$
* **优点:** 实际部署实用
* **缺点:** 依赖于当地病例组合和模型可移植性假设

---

#### 免责声明

无临床保证；用户负责验证和解释。始终记录假设并运行敏感性分析。

#### 联系方式

作者与维护: Minh Nguyen (minhnt@ump.edu.vn)
""",

    "a2_content_md": """
### What this is (English - Technical Details)

This module estimates the **minimum sample size (n)** needed to estimate the **baseline risk / event rate** (p) (i.e., prevalence of the outcome) with a **desired precision**, expressed as a **confidence interval (CI) half-width** (margin of error).

It is useful for:
* describing the outcome prevalence in a cohort with a specified precision,
* planning feasibility and reporting baseline risk,
* supporting calibration-related planning (e.g., calibration-in-the-large relies on the event rate).

**Important limitation:** This calculation **does not** ensure prediction model performance (AUC, calibration slope, optimism). It only targets precision for estimating (p).

---

### Inputs (what they mean)

1. **Outcome prevalence / event rate** (p)
   Expected proportion of events in the target population (e.g., 0.10).
   * If unknown, consider a plausible range and run a sensitivity analysis.
   * If you want a conservative “worst-case” for prevalence precision, use (p=0.50) (maximizes variance).

2. **Target half-width (margin of error)** (d)
   Desired precision such that the CI is approximately:
   $p \pm d$
   Examples: (d = 0.01, 0.02, 0.03) (i.e., ±1%, ±2%, ±3%).

3. **Confidence level** (1-$\\alpha$)
   Typical values: 0.95 or 0.99.

4. **CI Method**
* **Wilson score (recommended):** better coverage than Wald, especially when (p) is near 0 or 1 or sample size is modest.
* **Wald (normal approximation):** simple closed form but can perform poorly for small (n) or extreme (p).
* **Clopper–Pearson (exact):** conservative (often yields wider CIs; thus larger (n)).

---

### Core calculation

Let $X \sim \\text{Binomial}(n,p)$, $\hat p = X/n$. The goal is to find the smallest (n) such that the chosen CI method yields:
$$
\\frac{\\text{Upper}(n) - \\text{Lower}(n)}{2} \le d
$$

#### A) Wald (closed-form approximation)
$$ n \\approx \\frac{z^2 p(1-p)}{d^2} $$
**Note:** Fast but not recommended for small n or extreme p.

#### B) Wilson score interval (recommended)
Uses the Wilson score interval formula to find n. Since the interval depends on the observed count x, we iterate to find the smallest n where the half-width constraint is met for expected outcomes.

#### C) Clopper–Pearson “exact” interval
Uses Beta quantiles to form conservative intervals. Typically yields larger sample sizes.

---

### Practical defaults

* **Confidence level:** 95% is standard.
* **Half-width (d):** ±0.01 to ±0.03 (1%–3%) are common targets.
* **Method:** Wilson is a strong default.

### Key references
1. **Wilson EB.** Probable inference, the law of succession, and statistical inference. *JASA.* 1927.
2. **Newcombe RG.** Two-sided confidence intervals for the single proportion. *Stat Med.* 1998.
""",

    "b3_content_md": """
### Purpose (English - Technical Details)

This module estimates the **minimum sample size** needed to detect an association between a predictor (X) and a **binary outcome** (Y) using **logistic regression**, targeting a specified **odds ratio (OR)**, **two-sided ($\\alpha$)**, and **power**.

This is a **prognostic factor / association-focused** power calculation (testing a regression coefficient), **not** a prediction-model performance method. It does **not** guarantee good calibration or discrimination of a multivariable prediction model.

---

### When to use

Use B3 when:

* You want power to detect a **clinically meaningful OR** for a **single predictor** (binary or continuous) in logistic regression.
* Your primary goal is **hypothesis testing** (is the predictor associated with the outcome?), not building a risk prediction model.

### When NOT to use

Do not use B3 as your main approach when:

* Your goal is **prediction model development** (use Riley/pmsampsize or simulation/assurance methods).
* You plan **data-driven variable selection**, many interactions/splines, or complex machine-learning tuning (power for a single coefficient is not the right target).
* Data are **clustered** (multicenter/ward-level correlation) or strongly dependent without adjusting the design effect.
* You have a **case–control** design with fixed case/control sampling (baseline risks ($p_0$) may not represent the source population).

---

### Statistical model and parameters

Logistic regression model:
$$
\\text{logit}{P(Y=1\\mid X)}=\\beta_0+\\beta_1 X
$$

* For **binary** ($X\\in\\{0,1\\}$):
  $$
  \\mathrm{OR}=\\exp(\\beta_1)
  $$
* For **continuous** ($X$): OR must be defined for a specific change in ($X$), commonly **1 SD increase**.

Hypothesis test:
$$
H_0:\\beta_1=0 \\quad \\text{vs}\\quad H_1:\\beta_1\\neq 0
$$

---

### Inputs (what each value means)

1. **Alpha (two-sided)** ($\\alpha$)
   Common choices: 0.05 (standard), 0.01 (more stringent).

2. **Power** ($1-\\beta$)
   Common choices: 0.80 (standard), 0.90 (more conservative).

3. **Baseline event rate** ($p_0$)

   * For **binary predictor**: ($p_0 = P(Y=1\\mid X=0)$) (event rate in the reference group).
   * For **continuous predictor**: ($p_0$) is typically interpreted as the event rate at the **mean** of ($X$) (after centering).

4. **Target odds ratio** ($\\mathrm{OR}$)
   The smallest OR that is clinically meaningful and worth detecting.

5. **Predictor type**

* **Binary predictor**: requires **prevalence of (X=1)**, denoted ($q=P(X=1)$).
* **Continuous predictor**: typically requires the OR for a **1 SD increase** (or you must convert using SD).

6. **($R^2$) with other covariates**
   ($R^2$) is the squared multiple correlation from regressing ($X$) on other covariates in a multivariable model.

   * If ($X$) is correlated with other predictors, the effective information about ($\\beta_1$) decreases, so the required sample size increases.

---

# Calculation

## Step 1 — Convert OR and baseline risk to ($p_1$) (binary ($X$))

If ($X$) is binary, compute the event rate in the exposed group ($p_1=P(Y=1\\mid X=1)$) from ($p_0$) and OR:

$$
\\text{odds}_0=\\frac{p_0}{1-p_0},\\quad \\text{odds}_1=\\mathrm{OR}\\cdot \\text{odds}_0,\\quad
p_1=\\frac{\\text{odds}_1}{1+\\text{odds}_1}
$$

Overall event rate:
$$
p=(1-q)p_0+q p_1
$$

## Step 2 — Z-scores

Let:
$$
z_{\\alpha}=z_{1-\\alpha/2}, \\qquad z_{\\beta}=z_{1-\\beta}=z_{\\text{power}}
$$

## A) Binary predictor sample size (Hsieh approach)

With ($q=P(X=1)$), ($p_0=P(Y=1\\mid X=0)$), ($p_1=P(Y=1\\mid X=1)$), and ($p$) as above:

$$
n_0=
\\frac{
\\left[
z_{\\alpha}\\sqrt{\\frac{p(1-p)}{q(1-q)}}
+
z_{\\beta}\\sqrt{\\frac{p_1(1-p_1)}{q}+\\frac{p_0(1-p_0)}{1-q}}
\\right]^2
}
{(p_1-p_0)^2}
$$

### Adjustment for correlation with other covariates

If you plan a multivariable model and the predictor of interest ($X$) correlates with other covariates, inflate the sample size using:

$$
n=\\frac{n_0}{1-R^2}
$$

### Expected number of events

$$
E \\approx n\\cdot p
$$

---

## B) Continuous predictor sample size (Hsieh approach)

Assume a logistic model with a continuous predictor ($X$) and define OR for a **1 SD increase** in ($X$), denoted ($\\mathrm{OR}_{SD}$). Let ($p_0$) be the event rate at the mean of ($X$):

$$
n_0=\\frac{(z_{\\alpha}+z_{\\beta})^2}{p_0(1-p_0) [\\log(\\mathrm{OR}_{SD})]^2}
$$

If the user has an OR per 1-unit increase, ($\\mathrm{OR}_{unit}$), and SD of ($X$) is ($\\sigma_X$), convert:
$$
\\log(\\mathrm{OR}_{SD})=\\log(\\mathrm{OR}_{unit})\\cdot \\sigma_X
$$

Then apply the same multivariable correlation inflation:
$$
n=\\frac{n_0}{1-R^2}
$$

---

## Practical guidance: what values to choose (common conventions)

* **($\\alpha$)**: 0.05 (two-sided) is typical; use smaller ($\\alpha$) if multiple testing is expected.
* **Power**: 0.80 is common; 0.90 is preferred when missing the effect would be costly.
* **OR**: choose the **minimum clinically meaningful** OR (often in the 1.2–2.0 range depending on context).
* **Baseline risk ($p_0$)**: use local hospital/cohort data if available; otherwise use literature estimates and run sensitivity analyses.
* **Binary predictor prevalence ($q$)**: use local prevalence; note ($q$) near 0.5 gives the **largest information** (smaller ($n$)); very small/large ($q$) increases required ($n$).
* **($R^2$)**: if uncertain, run a sensitivity range (e.g., 0, 0.1, 0.25, 0.5). Even moderate correlation can inflate ($n$) substantially via ($1/(1-R^2)$).
* **Continuous predictors**: consider standardizing ($X$) to mean 0, SD 1 so ($\\mathrm{OR}_{SD}$) is easy to interpret.

---

## Key references (2–5)

1. Hsieh FY, Bloch DA, Larsen MD. *A simple method of sample size calculation for linear and logistic regression.* Statistics in Medicine. 1998;17(14):1623–1634.
2. Hsieh FY. *Sample size tables for logistic regression.* Statistics in Medicine. 1989;8(7):795–802.
3. Whittemore AS. *Sample size for logistic regression with small response probability.* Journal of the American Statistical Association. 1981;76:27–32.
""",
    "c5_content_md": """
### What this method is (English - Technical Details)

C5 implements the **Riley et al. analytical minimum sample size criteria** for **developing a multivariable clinical prediction model** with a **binary outcome** (logistic regression). The goal is to ensure the development dataset is large enough to:

1. **Limit overfitting** (via a target global shrinkage / calibration slope),
2. Achieve **adequate precision** for model performance (via a bound on optimism in $R^2$), and
3. Estimate the **overall outcome risk** (intercept/baseline risk) with acceptable precision.

This is a **model development** method (not external validation). It is particularly suitable when you plan a **pre-specified model form** (predictors and coding defined in advance) and want a **principled alternative to EPV rules**.

---

### When to use

Use C5 when:

* You are **developing** a new prediction model for a **binary outcome**.
* You can specify (even approximately) the **event rate** and an anticipated **overall model performance** (Cox–Snell $R^2$ or AUC).
* You want to target **low overfitting** (e.g., shrinkage $S \\ge 0.90$) and reasonable precision.

### When NOT to use (or use with caution)

Do not rely on C5 alone when:

* You will do extensive **data-driven variable selection**, multiple interactions/splines, or heavy ML tuning without adjusting the **effective number of parameters (df)**.
* Your data are strongly **clustered** (multicenter) without accounting for design effects.
* The intended modeling approach is not standard logistic regression (e.g., complex ML) unless you map complexity to an appropriate **effective df** or switch to simulation-based sizing.
* You cannot justify any plausible performance input (AUC/$R^2$); in that case run wide sensitivity analyses and consider simulation-based methods.

---

## Key inputs (what each means)

1. **Outcome prevalence / event rate** (p)
   Expected proportion with (Y=1) in the development dataset.

2. **Number of predictor parameters (df)** (P)
   Total degrees of freedom for all candidate predictors **excluding the intercept**.
   Include: dummy variables, spline bases, interactions (and any other basis expansions).

3. **Anticipated performance** (choose one)

* **Cox–Snell ($R^2_{CS}$)**: preferred if available from related prior studies (ideally optimism-adjusted).
* **AUC (C-statistic)**: if $R^2_{CS}$ is unavailable, the tool can approximate $R^2_{CS}$ from AUC and ($p$) using a published approach.
* **Conservative (15% of max $R^2$)**: a fallback when neither AUC nor $R^2$ is available; use with caution.

4. **Target global shrinkage** (S)
   A target for **overall overfitting control** (often interpreted similarly to an expected calibration slope after internal validation).

* Common default: $S = 0.90$ ($\\approx$ 10% shrinkage of predictor effects).
* More conservative: $S = 0.95$ (requires larger sample size).

---

## Core concepts and formulas

### Cox–Snell ($R^2$) and its maximum

Cox–Snell ($R^2$) for a fitted logistic model can be written as:
$$
R^2_{CS} = 1-\\exp!\\left(\\frac{2}{n}(\\ell_0-\\ell_1)\\right),
$$
where (\\ell_0) is the intercept-only log-likelihood and (\\ell_1) is the model log-likelihood.

For binary outcomes, ($R^2_{CS}$) cannot reach 1. Its maximum depends on the outcome prevalence:
$$
\\ell_0 = n\\Big[p\\ln(p) + (1-p)\\ln(1-p)\\Big],
$$
$$
R^2_{CS,\\max}=1-\\exp!\\left(\\frac{2\\ell_0}{n}\\right)
=1-\\exp!\\Big(2[p\\ln(p) + (1-p)\\ln(1-p)]\\Big).
$$

Nagelkerke ($R^2$) rescales Cox–Snell ($R^2$) to ([0,1]):
$$
R^2_{Nag}=\\frac{R^2_{CS}}{R^2_{CS,\\max}}.
$$

---

## The three Riley criteria (binary outcome)

### Criterion 1 — Control overfitting via target shrinkage (S)

Minimum sample size to target global shrinkage (S):
$$
n_1=\\left\\lceil
\\frac{P}{(S-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S}\\right)}
\\right\\rceil.
$$

### Criterion 2 — Limit optimism in ($R^2$) (default absolute difference 0.05)

This criterion targets a small absolute difference (default (\\delta=0.05)) between apparent and adjusted **Nagelkerke** ($R^2$). The required shrinkage implied by this constraint is:
$$
S_{\\delta}=\\frac{R^2_{CS}}{R^2_{CS}+\\delta,R^2_{CS,\\max}}.
$$
Then:
$$
n_2=\\left\\lceil
\\frac{P}{(S_{\\delta}-1),\\ln!\\left(1-\\frac{R^2_{CS}}{S_{\\delta}}\\right)}
\\right\\rceil.
$$

### Criterion 3 — Precise estimation of the overall outcome risk (intercept)

This targets precision of the **average outcome risk** (p) (baseline risk) within (\\pm d) on the probability scale (default (d=0.05) at 95% CI):
$$
n_3=\\left\\lceil
\\left(\\frac{z_{1-\\alpha/2}}{d}\\right)^2 p(1-p)
\\right\\rceil,
\\quad \\text{default } z_{0.975}=1.96,; d=0.05.
$$

### Final recommendation

$$
n_{\\min}=\\max(n_1,n_2,n_3),\\qquad
E = n_{\\min},p,\\qquad
EPP=\\frac{E}{P}.
$$

---

## Practical guidance (typical choices)

* **Shrinkage (S)**: use **0.90** as a standard target; consider **0.95** if you want stronger overfitting control or if the model is complex.
* **(\\delta=0.05)** for Criterion 2: commonly kept at the default.
* **Intercept precision (d=0.05)**: default corresponds to estimating baseline risk within ±5%. If baseline risk must be estimated more precisely, you would need a smaller (d) (larger (n)).
* **Anticipated ($R^2_{CS}$)**:

  * Prefer **optimism-adjusted** values from related studies (or apparent values from external validation data).
  * If only AUC is available, use the published AUC→($R^2_{CS}$) approximation method.
  * If neither is available, the **15% of ($R^2_{CS,\\max}$)** option is a conservative fallback for exploratory planning—always run sensitivity analyses.

---

## Key references (2–5)

1. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: PART II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
2. Riley RD, Ensor J, Snell KIE, et al. *Calculating the sample size required for developing a clinical prediction model.* BMJ. 2020.
3. Riley RD, Van Calster B, Collins GS. *A note on estimating the Cox–Snell ($R^2$) from a reported C statistic (AUROC) to inform sample size calculations for developing a prediction model with a binary outcome.* Statistics in Medicine. 2021.
4. Harrell FE Jr, Lee KL, Mark DB. *Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors.* Statistics in Medicine. 1996.
""",
    "c6_content_md": """
## C6: Development Simulation (Frequentist; custom DGM) (English - Technical Details)

### What this method is

C6 is a **simulation-based sample size planning** approach for **prediction model development** (binary outcome), inspired by the philosophy of **samplesizedev** and broader simulation-based design principles.

Instead of relying on a single analytical formula, C6 asks:

> “If we repeatedly develop the model using the planned approach on datasets of size (N), how often will the model meet pre-specified performance criteria on new data?”

It therefore targets **expected performance** (and/or probability of acceptable performance) under a **data-generating mechanism (DGM)** that represents your anticipated clinical population.

---

## When to use

Use C6 when:

* You want a planning method aligned with “**simulate what you will do**,” especially when:

  * predictors may be correlated,
  * you include non-linear terms or interactions,
  * event rates are modest or uncertain,
  * you want criteria based on **calibration** and **discrimination**.
* You can specify a reasonable DGM using local data or the literature.
* You are comfortable with simulation and want a more flexible alternative to purely analytical sizing.

## When NOT to use (or use with caution)

Avoid relying on C6 alone when:

* You cannot justify a plausible DGM (predictor distribution, correlations, effect sizes).
* You do not have computational budget (simulation can be expensive).
* You plan highly data-adaptive ML pipelines (feature selection, complex tuning) without explicitly simulating the full pipeline (C6 must reflect the actual pipeline to be valid).
* The target population is heterogeneous across hospitals/centers and you are not simulating clustering/case-mix shifts.

---

# Overview of the algorithm

For each candidate sample size (N), simulate (R) development datasets, fit the planned model, evaluate it on “new data,” and summarize performance.

### Step 1 — Choose a DGM

Define how predictors (X) and outcomes (Y) are generated.

Typical binary-outcome DGM:
$$
Y \mid X \sim \\text{Bernoulli}(\\pi), \\qquad
\\pi = \\text{logit}^{-1}(\\eta),
$$
$$
\\eta = \\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_j),
$$
where:

* (P) is the **number of parameters/df** used in the fitted model,
* (f_j(\\cdot)) represent coding choices (linear term, spline basis, dummy coding, etc.).

To achieve a target event rate (p), choose (\\beta_0) so that:
$$
\\mathbb{E}[\\pi] = p.
$$
In practice, (\\beta_0) is found by numerical root-finding using Monte Carlo draws from (X).

### Step 2 — Generate a development dataset

For replicate (r):

* Simulate (X^{(r)}) of size (N) from the chosen predictor distribution (with specified correlations).
* Simulate (Y^{(r)}) from the Bernoulli model above.

### Step 3 — Fit the development model

Fit the planned logistic regression model:
$$
\\widehat{\\eta} = \\widehat{\\beta}*0 + \\sum*{j=1}^{P}\\widehat{\\beta}_j f_j(X_j).
$$
**Important:** Simulation must match your intended development strategy (e.g., penalization, pre-specified terms). If separation/non-convergence occurs, a ridge-penalized fallback is often used (and should be counted and reported).

### Step 4 — Evaluate on new data

Generate an independent test set (size (N_{\\text{test}}), often large such as 5000–10000) from the same DGM and compute:

**(a) Discrimination (AUC / C-statistic)**
$$
\\mathrm{AUC}=\\Pr(\\widehat{\\eta}_1 > \\widehat{\\eta}_0),
$$
the probability that a randomly selected case has a higher predicted risk than a non-case.

**(b) Calibration slope**
Estimate (b) from a calibration model on the test set:
$$
\\text{logit}(Y) = a + b \\cdot \\text{logit}(\\widehat{p}),
$$
or equivalently using the linear predictor:
$$
\\text{logit}(Y) = a + b \\cdot \\widehat{\\eta}.
$$
Here, (b\\approx 1) indicates good calibration; (b<1) suggests overfitting (predictions too extreme).

### Step 5 — Define pass/fail criteria and compute success rates

Across (R) simulations for each (N), compute:

* Mean calibration slope:
  $$
  \\overline{b} = \\frac{1}{R}\\sum_{r=1}^R b^{(r)}.
  $$
* Probability slope is within an acceptable range:
  $$
  \\widehat{\\Pr}(b \\in [L,U]) = \\frac{1}{R}\\sum_{r=1}^R \\mathbf{1}{b^{(r)}\\in[L,U]}.
  $$
* Mean AUC:
  $$
  \\overline{\\mathrm{AUC}}=\\frac{1}{R}\\sum_{r=1}^R \\mathrm{AUC}^{(r)}.
  $$

A candidate (N) is “acceptable” if all selected criteria are met, e.g.:

* (\\overline{b} \\ge 0.90)
* (\\widehat{\\Pr}(0.9 \\le b \\le 1.1) \\ge 0.80)
* (\\overline{\\mathrm{AUC}} \\ge \\mathrm{AUC}_{\\text{target}})

Choose smallest (N) that passes.

---

# Key inputs (where to find, what to pick)

### 1) Event rate (p)

**Where:** local hospital/cohort data; literature default.
**Planning range:** 5%–15% (fluctuates by disease).
**Recommendation:** run sensitivity on plausible range.

### 2) Parameters (df) (P)

**Where:** intended model specification (including dummies, splines, interactions).
**Typical:** 10–30 df common; more df demands much larger N.

### 3) Target AUC (Mode A)

**Where:** similar published models (ideally external validation); pilot data.
**Typical:** 0.70–0.85 common; >0.90 rare/often optimistic.

### 4) Candidates (N)

Choose a range wide enough to see the pass/fail transition (e.g., 1000–5000).

### 5) Simulations per N (R)

* Demo: (R \\approx 200)
* Final: (R \\ge 1000)
  Monte Carlo Error for success probability:
  $$
  \\mathrm{MCSE}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{R}}.
  $$

### 6) Pass/Fail Criteria

* Mean calibration slope ≥ 0.9
* Pr(0.9 ≤ slope ≤ 1.1) ≥ 80%
* Mean AUC ≥ target

**Convention:** slope 0.90-1.10 and 0.80 probability threshold often used for planning; 0.90 for stricter requirements.

---

# Strengths & Weaknesses

**Strengths**

* Flexible (correlation, non-linearity, interactions).
* Targets performance on new data directly, specifically calibration.
* Easy to do sensitivity analysis.

**Weaknesses**

* Strong dependence on DGM assumptions.
* Computationally expensive.
* Must simulate the exact intended pipeline; mismatches lead to invalid N.

---

## Key references (2–5)

1. Pavlou M, Ambler G, Seaman SR, et al. *How to develop a more accurate risk prediction model when there are few events.* BMJ. 2015.
2. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
3. Pavlou M, et al. *Simulation-based sample size calculation for prediction model performance targets* (validation/development methodology). Statistics in Medicine. 2021.
4. Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating.* 2nd ed. Springer. 2019.
""",
    "c7_content_md": """
## C7: Bayesian Assurance (MCMC) (English - Technical Details)

### What this method is
**Bayesian assurance** is a simulation-based sample size planning method for **Bayesian model building** (here: Bayesian logistic regression for binary outcomes).
Unlike "power" (frequentist), assurance targets the **unconditional probability** that the study will yield a **successful outcome** given the priors.

Simply put:
> "If we repeat the full study many times (generate data + fit Bayes via MCMC), what is the probability the model meets requirements?"

---

### When to use
Use C7 when:
- The final analysis will be **Bayesian** estimated via **MCMC**.
- You want to sample size for a target **success probability** (e.g., ≥80% or ≥90%).
- You can make reasonable assumptions about:
  - event rates,
  - predictor correlations,
  - plausible effect sizes (pilot/literature),
  - priors for regression coefficients.

### When NOT to use (or use with caution)
- You are doing frequentist analysis (use C5 or C6).
- Computational resources are very limited (MCMC inside simulation is slow).
- You have no idea about priors.
"""
}
