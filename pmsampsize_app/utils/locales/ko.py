KO = {
        "title": "예후 연구 표본 크기 도구",
        "sidebar_title": "설정",
        "language": "언어 / Language",
        "mode": "방법 선택",
        "mode_riley": "방법 1: Riley 등 (분석적)",
        "mode_bayes": "방법 2: 베이지안 보증 (시뮬레이션)",
        "mode_single": "단일 시나리오",
        "mode_batch": "민감도 분석 (범위)",
        "method1_tab": "방법 1 (Riley)",
        "method2_tab": "방법 2 (Bayesian)",
        "nav_title": "탐색",
        "nav_readme": "상세 문서 (README)",
        "nav_intro": "소개 및 공식",
        "nav_calc": "표본 크기 계산기",
        "intro_heading": "환영합니다",
        "intro_text": "이 도구는 이분형 결과가 있는 임상 예측 모델 개발에 필요한 최소 표본 크기를 계산하는 데 도움을 줍니다.",
        "formula_heading": "수학적 프레임워크 (방법 1)",
        "formula_intro": "방법 1은 Riley 등이 제공한 폐쇄형 솔루션을 사용하고, 방법 2는 베이지안 MCMC 시뮬레이션을 사용합니다.",
        "sens_guide_title": "💡 민감도 분석(배치 모드) 사용법",
        "sens_guide_text": """
        - **범위**: `min-max` 형식으로 입력 (예: `0.05-0.10`). 단계가 자동으로 생성됩니다.
        - **특정 값**: 쉼표로 구분된 목록 입력 (예: `0.05, 0.10, 0.15`).
        """,
        "detail_view": "시나리오별 상세 계산 보기",
        "footer_refs": "참고문헌: Riley et al. (2018, 2020), BayesAssurance.",
        "calc_btn": "계산하기",
        "results": "결과",
        "sanity": "건전성 심사 (EPV 규칙)",
        "download_csv": "CSV 다운로드",
        "download_report": "전체 보고서 다운로드",
        "error_p": "유병률은 0과 1 사이여야 합니다.",
        "error_auc": "AUC는 0.5와 1 사이여야 합니다.",
        "error_parse": "입력을 구문 분석할 수 없습니다.",
        "riley_inputs": "입력 파라미터 (Riley)",
        "prevalence": "결과 유병률 (이벤트 발생률)",
        "prevalence_help": "이벤트가 발생한 참가자의 비율 (0 < p < 1).",
        "parameters": "예측 변수 파라미터 수 (df)",
        "parameters_help": "총 자유도 (절편 제외).",
        "shrinkage": "목표 글로벌 수축 (S)",
        "shrinkage_help": "희망하는 수축 계수 (기본값 0.9).",
        "perf_measure": "예상 성능",
        "perf_auc": "AUC (C-통계량)",
        "perf_r2": "Cox-Snell R-제곱",
        "perf_cons": "보수적 점수 (최대 R2의 15%)",
        "bayes_inputs": "시뮬레이션 설정 (베이지안 보증)",
        "dgm_settings": "데이터 생성 매커니즘",
        "sim_settings": "시뮬레이션 및 MCMC",
        "eval_settings": "평가 기준",
        "n_candidates": "후보 표본 크기 (쉼표로 구분)",
        "n_candidates_help": "테스트할 N 값 목록, 예: 500, 1000, 1500.",
        "correlation": "예측 변수 상관관계 (rho)",
        "n_sims": "N당 시뮬레이션 횟수",
        "assurance_threshold": "보증 임계값 (목표 확률)",
        "run_simulation": "베이지안 시뮬레이션 실행",
        "simulation_running": "시뮬레이션 실행 중... 시간이 걸릴 수 있습니다.",
        "assurance_result": "보증 분석",
        "mode_dev_sim": "방법 6: 개발 시뮬레이션 (빈도주의)",
        "method6_tab": "방법 6 (시뮬레이션)",
        "dev_sim_intro": "모델 개발을 위한 시뮬레이션 기반 표본 크기 (samplesizedev와 유사한 빈도주의 접근법).",
        "dev_mode_simple": "모드 A: 단순 (AUC 기반)",
        "dev_mode_custom": "모드 B: 사용자 정의 DGM",
        "target_auc": "목표 평균 AUC (C-통계량)",
        "target_auc_help": "알고리즘이 이 AUC를 달성하기 위한 베타 계수를 찾습니다.",
        "criteria_settings": "성능 기준 (통과/실패)",
        "crit_slope_mean": "평균 교정 기울기 >= 0.9",
        "crit_slope_ci": "Pr(0.9 <= 기울기 <= 1.1) >= 80%",
        "crit_auc": "평균 AUC >= 목표",
        "audit_trail": "RNG 감사 추적 (JSON)",
        "future_methods": "향후 버전에서 제공 예정...",
        "method_quick_tab": "A. 신속 / 기본",
        "quick_mode_epv": "A1: EPV / EPP 규칙 (경험적)",
        "quick_mode_risk": "A2: 기본 위험 정밀도 (CI 너비)",
        "target_epv": "목표 파라미터당 이벤트 수 (EPP)",
        "target_epv_help": "일반적인 경험적 수치는 10, 15, 20입니다. EPP가 EPV보다 선호됩니다.",
        "epv_warning_title": "⚠️ 중요 경고",
        "epv_warning_text": "EPV/EPP는 대략적인 경험적 규칙입니다. 교정, 판별을 보장하거나 낙관주의를 방지하지 않습니다. 변수 선택 및 비선형 항에 민감합니다.",
        "ci_level": "신뢰 수준",
        "ci_half_width": "목표 반-너비 (오차 한계)",
        "ci_method": "CI 방법",
        "ci_method_wilson": "Wilson Score (권장)",
        "ci_method_wald": "Wald (단순)",
        "ci_method_cp": "Clopper-Pearson (보수적)",
        "risk_help": "특정 정밀도로 이벤트 발생률 p를 추정하기 위한 N을 계산합니다. 예측 모델 성능을 보장하지 않습니다.",
        "title_b3": "B3: 로지스틱 검정력 (Hsieh)",
        "title_b4": "B4: Cox 검정력 (Schoenfeld)",
        "interpretation": "결과 해석",
        "d8_assumptions": "**가정**: Hanley & McNeil (1982) 분산 근사치를 사용합니다. AUC에 대해 대칭적 정규 분포를 가정합니다.",
        "d8_mode_n_to_width": "N으로부터 CI 너비 계산",
        "d8_mode_width_to_n": "CI 너비로부터 필요한 N 계산",
        "d8_opt_settings": "고급 최적화 설정",
        "d8_practical_rounding": "실용적인 정수 반올림 표시",
        "d8_n_input": "표본 크기 (N)",
        "d8_width_input": "CI 너비 (합계)",
        "d8_opt_bound": "탐색 상한선",
        "d8_opt_tol": "허용 오차",
        "title_d8": "D8: AUC 정밀도 (Hanley-McNeil)",
        "d8_desc": "희망하는 정밀도(CI 너비)로 AUC를 추정하기 위한 표본 크기를 계산합니다.",
        "auc_expected": "예상 AUC (C-통계량)",
        "formulas_header": "📚 공식 및 기술적 세부 사항",
        "title_d9": "D9: 외부 검증 (맞춤형)",
        "common_inputs": "공통 파라미터",
        "search_placeholder": "방법 검색...",
        "settings": "설정",
        "footer_copyright": "© 2026 Prognostic Research Sample Size Tool. 학술/연구용 전용.",
        "footer_author": "저자 및 유지관리: Minh Nguyen (minhnt@ump.edu.vn)",
        "footer_disclaimer": "면책 조항: 임상적 보증 없음. 사용자는 결과 검증 및 해석에 대한 책임이 있습니다.",

        "intro_complete_md": """
### Welcome

This app helps clinicians and researchers plan minimum sample size for prognostic research, including:
* Prognostic factor studies (power to detect associations),
* Clinical prediction model development (risk prediction), and
* Model validation / updating (external validation, recalibration).

It is designed for binary outcomes (e.g., event vs no event) and, for some modules, time-to-event outcomes (Cox PH).

Source code (download): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)

### Getting started (for new users)

#### 1. Clarify your study goal
* Are you testing a single prognostic factor (association)?
* Are you building a prediction model?
* Are you validating an existing model in a new population?

#### 2. Estimate the event rate $p$ (or event fraction for survival)
* Prefer local hospital data (best).
* If uncertain, enter a range and run a sensitivity analysis.

#### 3. Count model complexity correctly (parameters / df)
Use parameters (degrees of freedom), not just "number of variables."
* Binary predictor: 1 df
* Categorical with $L$ levels: $L-1$ df
* Spline (RCS with $K$ knots): $K-1$ df
* Interaction: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. Choose a method from the catalog below
* Use **"Quick tools"** for rough planning only.
* Use **Riley / simulation / assurance** when you are developing a prediction model.

---

### When to use this app (and when not to)

**Use this app when you are:**
* Planning retrospective or prospective cohort studies in prognosis/prediction
* Developing or validating risk prediction models
* Estimating sample size for precision (CI width) of prevalence or AUC
* Designing external validation with calibration and discrimination targets

**Do NOT use this app as the primary tool when you are:**
* Designing randomized controlled trials (use RCT-specific power/sample size methods)
* Planning diagnostic accuracy studies for sensitivity/specificity without prediction modeling
* Expecting a single "correct" number: sample size planning requires assumptions and should include sensitivity analyses

---

### Available Methods (Overview)

#### A. Quick / Basic (fast, approximate)

**A1 — Rules of Thumb (EPV/EPP) (heuristic)**
* **Use when:** you need a quick sanity check on whether events are "roughly sufficient" for a planned model size.
* **Do not use when:** model includes splines/interactions/variable selection, or event rate is low—EPV/EPP does not guarantee good calibration or low optimism.
* **Key inputs:** event rate $p$, number of parameters $P$ (df), target EPP (e.g., 10/15/20)
* **Core output:** required events $E=t \\cdot P$, required sample size $N=\\lceil E/p \\rceil$
* **Strengths:** extremely simple; good for early feasibility
* **Weaknesses:** can be misleading; not performance-based

**A2 — Baseline Risk Precision (CI width for prevalence)**
* **Use when:** your goal is to estimate the event rate $p$ with a desired CI half-width (e.g., ±2%).
* **Do not use when:** you want prediction model performance guarantees (AUC/calibration slope).
* **Key inputs:** expected $p$, CI method (Wilson recommended), confidence level, target half-width $d$
* **Core output:** minimum $N$ such that CI half-width $\\le d$
* **Strengths:** direct precision target; transparent assumptions
* **Weaknesses:** about prevalence only, not model performance

#### B. Prognostic factor (power) (association-focused, not prediction model sizing)

**B3 — Logistic OR Power (Hsieh)**
* **Use when:** you want power to detect a target odds ratio (OR) for a prognostic factor in logistic regression.
* **Do not use when:** your primary goal is prediction model development (calibration/discrimination), not hypothesis testing.
* **Key inputs:** baseline risk $p_0$, target OR, alpha, power, exposure prevalence (binary) or SD (continuous), optional $R^2$ with covariates
* **Core output:** required $N$ (and implied events) to detect the OR
* **Strengths:** classic power framework for association
* **Weaknesses:** does not address prediction model performance; sensitive to input assumptions

**B4 — Cox HR Power (Schoenfeld)**
* **Use when:** time-to-event outcome; you want power to detect a hazard ratio (HR) under Cox PH.
* **Do not use when:** PH assumption likely violated, or event fraction is highly uncertain and cannot be reasonably estimated.
* **Key inputs:** HR, alpha, power, allocation proportion (binary) or SD (continuous), expected event fraction during follow-up
* **Core output:** required number of events; convert to $N$ using event fraction
* **Strengths:** widely accepted; event-based planning is intuitive
* **Weaknesses:** depends strongly on event fraction and follow-up/censoring assumptions

#### C. Prediction model development (recommended for risk model building)

**C5 — Riley et al. (Analytical; pmsampsize-like)**
* **Use when:** developing a multivariable prediction model; you want to control overfitting and ensure adequate precision.
* **Do not use when:** you cannot provide reasonable assumptions for prevalence and anticipated model performance (AUC or $R^2$); in that case, use sensitivity analysis or simulation.
* **Key inputs:** event rate $p$, parameters $P$ (df), target shrinkage (e.g., 0.90), anticipated model performance (AUC or Cox–Snell $R^2$)
* **Core output:** minimum $N$ meeting multiple criteria (overfitting control + precision)
* **Strengths:** principled, performance-aware, widely cited
* **Weaknesses:** depends on performance assumptions; requires careful df counting

**C6 — Development Simulation (Frequentist; samplesizedev/custom DGM)**
* **Use when:** you prefer "simulate what you will do," especially with nonlinearity/interactions and custom data structures.
* **Do not use when:** you cannot specify a plausible data-generating mechanism (DGM) or you need results instantly (compute-intensive).
* **Key inputs:** candidate $N$ grid, DGM assumptions (predictor distributions/correlations/effects), performance targets (e.g., calibration slope range, AUC threshold), simulation replicates, seed
* **Core output:** smallest $N$ achieving targets with acceptable probability/precision
* **Strengths:** flexible; aligns with complex modeling
* **Weaknesses:** assumptions-heavy; computational cost

**C7 — Bayesian Assurance (MCMC)**
* **Use when:** the final model will be estimated with Bayesian MCMC, and you want sample size based on assurance (probability of meeting posterior performance/precision targets).
* **Do not use when:** priors cannot be justified or computation budget is limited.
* **Key inputs:** DGM, priors, candidate $N$, MCMC settings, assurance threshold (e.g., 80%/90%), performance/precision targets
* **Core output:** minimal $N$ meeting assurance threshold
* **Strengths:** coherent for Bayesian workflows; directly targets posterior criteria
* **Weaknesses:** computationally intensive; requires prior specification

#### D. Validation / Updating (for existing models)

**D8 — AUC Precision (Hanley–McNeil / presize)**
* **Use when:** your validation goal is precision of AUC (CI width).
* **Do not use when:** calibration (slope/CITL) is the primary concern—this method targets AUC only.
* **Key inputs:** expected AUC, prevalence or case-control ratio, confidence level, target CI width
* **Core output:** minimum $N$ to achieve desired AUC CI width
* **Strengths:** simple; quick planning for discrimination precision
* **Weaknesses:** approximate variance; ignores calibration

**D9 — External Validation (Tailored; pmvalsampsize / sampsizeval)**
* **Use when:** you want validation sizing targeting multiple performance measures (calibration + discrimination), often requiring assumptions about the LP distribution.
* **Do not use when:** you cannot justify LP distribution assumptions or expected performance.
* **Key inputs:** prevalence, expected AUC, calibration slope/CITL targets, CI widths or SE targets, LP distribution assumptions
* **Core output:** recommended $N$ meeting precision criteria across measures
* **Strengths:** tailored; calibration-aware
* **Weaknesses:** requires additional assumptions; more complex

**D10 — External Validation (Simulation; LP-based)**
* **Use when:** you can specify/estimate the distribution of the linear predictor (LP) in the target validation population and want simulation-based precision planning.
* **Do not use when:** LP distribution is unknown and cannot be approximated.
* **Key inputs:** LP distribution (normal/beta/empirical), miscalibration parameters, CI width targets for metrics, replicates, seed
* **Core output:** minimal $N$ achieving precision targets under simulation
* **Strengths:** very flexible; matches "simulate what you expect"
* **Weaknesses:** assumptions-heavy; computational cost

**D11 — Updating / Recalibration (intercept/slope)**
* **Use when:** you will recalibrate an existing model (update intercept and/or slope) and need adequate precision.
* **Do not use when:** you are developing a brand-new model (use C5–C7).
* **Key inputs:** updating type (intercept only vs intercept+slope), event rate, precision targets
* **Core output:** $N$ sufficient for stable updating
* **Strengths:** practical for real-world deployment
* **Weaknesses:** depends on local case-mix and model transportability assumptions

---

#### disclaimer

No clinical warranty; users are responsible for validation and interpretation. Always document assumptions and run sensitivity analyses.

#### Contact

Author & Maintenance: Minh Nguyen (minhnt@ump.edu.vn)
""",

        "a2_content_md": """
### 이것은 무엇입니까

이 모듈은 **원하는 정밀도**(신뢰 구간(CI) 반폭 또는 오차 한계로 표현됨)로 **기본 위험 / 사건 발생률**(p)(즉, 결과의 유병률)을 추정하는 데 필요한 **최소 표본 크기(n)**를 추정합니다.

다음과 같은 경우에 유용합니다:
* 지정된 정밀도로 코호트 내 결과 유병률 설명,
* 타당성 계획 및 기본 위험 보고,
* 교정 관련 계획 지원 (예: calibration-in-the-large는 사건 발생률에 의존).

**중요한 제한 사항:** 이 계산은 예측 모델 성능(AUC, 교정 기울기, 낙관주의)을 **보장하지 않습니다**. 오직 (p) 추정의 정밀도만을 목표로 합니다.

---

### 입력 값 (의미)

1. **결과 유병률 / 사건 발생률** (p)
   대상 모집단에서 예상되는 사건 비율 (예: 0.10).
   * 알 수 없는 경우, 타당한 범위를 고려하여 민감도 분석을 실행하십시오.
   * 유병률 정밀도에 대해 보수적인 "최악의 경우"를 원한다면 (p=0.50)을 사용하십시오 (분산 최대화).

2. **목표 반폭 (오차 한계)** (d)
   CI가 대략 다음과 같도록 하는 원하는 정밀도:
   $p \pm d$
   예: (d = 0.01, 0.02, 0.03) (즉, ±1%, ±2%, ±3%).

3. **신뢰 수준** (1-$\\alpha$)
   일반적인 값: 0.95 또는 0.99.

4. **CI 방법**
* **Wilson score (권장):** Wald보다 커버리지가 좋으며, 특히 (p)가 0이나 1에 가깝거나 표본 크기가 적당할 때 좋습니다.
* **Wald (정규 근사):** 간단한 폐쇄형이지만 (n)이 작거나 (p)가 극단적일 때 성능이 떨어질 수 있습니다.
* **Clopper–Pearson (정확):** 보수적입니다 (종종 더 넓은 CI를 산출하므로 더 큰 (n)이 필요함).

---

### 핵심 계산 (원리)

$X \sim \\text{Binomial}(n,p)$, $\hat p = X/n$이라고 합시다. 목표는 선택한 CI 방법이 다음을 산출하도록 하는 가장 작은 (n)을 찾는 것입니다:
$$
\\frac{\\text{Upper}(n) - \\text{Lower}(n)}{2} \le d
$$

#### A) Wald (폐쇄형 근사)
$$ n \\approx \\frac{z^2 p(1-p)}{d^2} $$
**참고:** 빠르지만 (n)이 작거나 (p)가 극단적일 때는 권장되지 않습니다.

#### B) Wilson score 구간 (권장)
Wilson score 구간 공식을 사용합니다.

#### C) Clopper–Pearson “정확” 구간
Beta 분위수를 사용합니다. 보수적인 방법입니다.

---

### 실용적인 기본값

* **신뢰 수준:** 95%가 표준입니다.
* **반폭 (d):** ±0.01 ~ ±0.03 (1%–3%)이 일반적인 목표입니다.
* **방법:** Wilson이 강력한 기본값입니다.

### 주요 참고 문헌
1. **Wilson EB.** Probable inference... *JASA.* 1927.
2. **Newcombe RG.** Two-sided confidence intervals... *Stat Med.* 1998.
""",

        "b3_content_md": """
### Purpose (what this method is)

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

## Statistical model and parameters

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

## Inputs (what each value means)

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
### What this method is

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
R^2_{CS} = 1-\\exp\\left(\\frac{2}{n}(\\ell_0-\\ell_1)\\right),
$$
where $\\ell_0$ is the intercept-only log-likelihood and $\\ell_1$ is the model log-likelihood.

For binary outcomes, $R^2_{CS}$ cannot reach 1. Its maximum depends on the outcome prevalence:
$$
\\ell_0 = n\\Big[p\\ln(p) + (1-p)\\ln(1-p)\\Big],
$$
$$
R^2_{CS,\\max}=1-\\exp\\left(\\frac{2\\ell_0}{n}\\right)
=1-\\exp\\Big(2[p\\ln(p) + (1-p)\\ln(1-p)]\\Big).
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
\\frac{P}{(S-1)\\ln\\left(1-\\frac{R^2_{CS}}{S}\\right)}
\\right\\rceil.
$$

### Criterion 2 — Limit optimism in ($R^2$) (default absolute difference 0.05)

This criterion targets a small absolute difference (default $\\delta=0.05$) between apparent and adjusted **Nagelkerke** ($R^2$). The required shrinkage implied by this constraint is:
$$
S_{\\delta}=\\frac{R^2_{CS}}{R^2_{CS}+\\delta R^2_{CS,\\max}}.
$$
Then:
$$
n_2=\\left\\lceil
\\frac{P}{(S_{\\delta}-1)\\ln\\left(1-\\frac{R^2_{CS}}{S_{\\delta}}\\right)}
\\right\\rceil.
$$

### Criterion 3 — Precise estimation of the overall outcome risk (intercept)

This targets precision of the **average outcome risk** ($p$) (baseline risk) within ($\\pm d$) on the probability scale (default $d=0.05$ at 95% CI):
$$
n_3=\\left\\lceil
\\left(\\frac{z_{1-\\alpha/2}}{d}\\right)^2 p(1-p)
\\right\\rceil,
\\quad \\text{default } z_{0.975}=1.96,; d=0.05.
$$

### Final recommendation

$$
n_{\\min}=\\max(n_1,n_2,n_3),\\qquad
E = n_{\\min}p,\\qquad
EPP=\\frac{E}{P}.
$$

---

## Practical guidance (typical choices)

* **Shrinkage (S)**: use **0.90** as a standard target; consider **0.95** if you want stronger overfitting control or if the model is complex.
* **$\\delta=0.05$** for Criterion 2: commonly kept at the default.
* **Intercept precision (d=0.05)**: default corresponds to estimating baseline risk within ±5%. If baseline risk must be estimated more precisely, you would need a smaller ($d$) (larger ($n$)).
* **Anticipated ($R^2_{CS}$)**:

  * Prefer **optimism-adjusted** values from related studies (or apparent values from external validation data).
  * If only AUC is available, use the published AUC→$R^2_{CS}$ approximation method.
  * If neither is available, the **15% of $R^2_{CS,\\max}$** option is a conservative fallback for exploratory planning—always run sensitivity analyses.

---

## Key references (2–5)

1. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: PART II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
2. Riley RD, Ensor J, Snell KIE, et al. *Calculating the sample size required for developing a clinical prediction model.* BMJ. 2020.
3. Riley RD, Van Calster B, Collins GS. *A note on estimating the Cox–Snell ($R^2$) from a reported C statistic (AUROC) to inform sample size calculations for developing a prediction model with a binary outcome.* Statistics in Medicine. 2021.
4. Harrell FE Jr, Lee KL, Mark DB. *Multivariable prognostic models: issues in developing models, evaluating assumptions and adequacy, and measuring and reducing errors.* Statistics in Medicine. 1996.
""",
}
