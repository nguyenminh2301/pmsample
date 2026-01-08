EN = {
        "title": "Prognostic Research Sample Size Tool",
        "sidebar_title": "Configuration",
        "language": "Language / Ngôn ngữ",
        "mode": "Method Selection",
        "mode_riley": "Method C5: Riley et al. (Analytical)",
        "mode_bayes": "Method C6: Bayesian Assurance (Simulation)",
        "mode_single": "Single Scenario",
        "mode_batch": "Sensitivity Analysis (Ranges)",
        "method1_tab": "Method C5 (Riley)",
        "method2_tab": "Method C6 (Bayesian)",
        "nav_title": "Navigation",
        "nav_readme": "Documentation (README)",
        "nav_intro": "Introduction & Formulas",
        "nav_calc": "Sample Size Calculator",
        "intro_heading": "Welcome",
        "intro_text": "This tool helps researchers calculate the minimum sample size required for developing a clinical prediction model with a binary outcome.",
        "formula_heading": "Mathematical Framework (Method C5)",
        "formula_intro": "Method C5 uses the closed-form solutions provided by Riley et al., while Method C6 uses Bayesian MCMC simulation.",
        "sens_guide_title": "💡 How to use Sensitivity Analysis (Batch Mode)",
        "sens_guide_text": """
        - **Ranges**: Enter `min-max` (e.g., `0.05-0.10`). The app will generate steps automatically.
        - **Specific Values**: Enter comma-separated lists (e.g., `0.05, 0.10, 0.15`).
        """,
        "detail_view": "View Detailed Calculation for Scenario",
        "footer_refs": "References: Riley et al. (2018, 2020), BayesAssurance.",
        "calc_btn": "Calculate",
        "results": "Results",
        "sanity": "Sanity Check (EPV Rules)",
        "download_csv": "Download CSV",
        "download_report": "Download Full Report",
        "error_p": "Prevalence must be between 0 and 1.",
        "error_auc": "AUC must be between 0.5 and 1.",
        "error_parse": "Could not parse input.",
        
        # Riley specific
        "riley_inputs": "Input Parameters (Riley)",
        "prevalence": "Outcome Prevalence (Event Rate)",
        "prevalence_help": "Proportion of participants with the event (0 < p < 1).",
        "parameters": "Number of Predictor Parameters (df)",
        "parameters_help": "Total degrees of freedom (excluding intercept).",
        "shrinkage": "Target Global Shrinkage (S)",
        "shrinkage_help": "Desired shrinkage factor (default 0.9).",
        "perf_measure": "Anticipated Performance",
        "perf_auc": "AUC (C-statistic)",
        "perf_r2": "Cox-Snell R-squared",
        "perf_cons": "Conservative (15% of Max R2)",
        
        # Bayesian specific 
        "perf_cons_help": "Conservative (15% of Max R2)",
        "perf_auc_help": "Anticipated AUC (C-statistic)",
        "perf_r2_help": "Anticipated Cox-Snell R-squared",
        "perf_cons_help": "Conservative (15% of Max R2)",
        # Bayesian specific
        "bayes_inputs": "Simulation Settings (Bayesian Assurance)",
        "dgm_settings": "Data Generating Mechanism",
        "sim_settings": "Simulation & MCMC",
        "eval_settings": "Evaluation Criteria",
        "n_candidates": "Candidate Sample Sizes (comma separated)",
        "n_candidates_help": "List of N values to test, e.g., 500, 1000, 1500.",
        "correlation": "Predictor Correlation (rho)",
        "n_sims": "Number of Simulations per N",
        "assurance_threshold": "Assurance Threshold (Target Probability)",
        "run_simulation": "Run Bayesian Simulation",
        "simulation_running": "Running Simulations... This may take a while.",
        "assurance_result": "Assurance Analysis",
        
        # Method 6 (Dev Sim)
        "mode_dev_sim": "Method 6: Development Simulation (Freq)",
        "method6_tab": "Method 6 (Simulation)",
        "dev_sim_intro": "Simulation-based sample size for model development (frequentist approach similar to `samplesizedev`).",
        "dev_mode_simple": "Mode A: Simple (AUC-driven)",
        "dev_mode_custom": "Mode B: Custom DGM",
        "target_auc": "Target Mean AUC (C-statistic)",
        "target_auc_help": "Algorithm will find Beta coefficients to achieve this AUC.",
        "criteria_settings": "Performance Criteria (Pass/Fail)",
        "crit_slope_mean": "Mean Calibration Slope >= 0.9",
        "crit_slope_ci": "Pr(0.9 <= Slope <= 1.1) >= 80%",
        "crit_auc": "Mean AUC >= Target",
        "audit_trail": "RNG Audit Trail (JSON)",
        "future_methods": "Coming in future versions...",
        
        # Quick Methods
        "method_quick_tab": "A. Quick / Basic",
        "quick_mode_epv": "A1: EPV / EPP Rule (Heuristic)",
        "quick_mode_risk": "A2: Baseline Risk Precision (CI Width)",
        "target_epv": "Target Events Per Parameter (EPP)",
        "target_epv_help": "Common heuristic values are 10, 15, 20. EPP is preferred over EPV.",
        "epv_warning_title": "⚠️ Important Warning",
        "epv_warning_text": "EPV/EPP is a rough heuristic. It does not guarantee calibration, discrimination, or prevent optimism. It is sensitive to variable selection and non-linear terms.",
        "ci_level": "Confidence Level",
        "ci_half_width": "Target Half-Width (Margin of Error)",
        "ci_method": "CI Method",
        "ci_method_wilson": "Wilson Score (Recommended)",
        "ci_method_wald": "Wald (Simple)",
        "ci_method_cp": "Clopper-Pearson (Conservative)",
        "risk_help": "Calculates N to estimate the event rate p with a specific precision. Does not ensure prediction model performance.",
        
        # Power Methods (B)
        "title_b3": "B3: Logistic Power (Hsieh)",
        "title_b4": "B4: Cox Power (Schoenfeld)",
        "interpretation": "Interpretation",
        
        # UI Basics
        "d8_assumptions": "**Assumptions**: Uses Hanley & McNeil (1982) variance approximation. Symmetric Normal assumption for AUC. Numerical optimization to find N.",
        "d8_mode_n_to_width": "Compute CI width from N",
        "d8_mode_width_to_n": "Compute required N from CI width",
        "d8_opt_settings": "Advanced Optimizer Settings",
        "d8_practical_rounding": "Show Practical Integer Rounding",
        "d8_n_input": "Sample Size (N)",
        "d8_width_input": "CI Width (Total)",
        "d8_opt_bound": "Search Upper Limit",
        "d8_opt_tol": "Tolerance",
        
        # Validations (D)
        "title_d8": "D8: AUC Precision (Hanley-McNeil)",
        "d8_desc": "Calculate sample size for estimating AUC with desired precision (CI width).",
        "auc_expected": "Expected AUC (C-statistic)",
        "formulas_header": "📚 Formulas & Technical Details",
        "d8_assumptions": "**Assumptions**: Uses Hanley & McNeil (1982) variance approximation. Symmetric Normal assumption for AUC. Numerical optimization to find N.",
        "d8_mode_n_to_width": "Calculate CI Width from N",
        "d8_mode_width_to_n": "Calculate N from CI Width",
        "d8_opt_settings": "Advanced Optimizer Settings",
        "d8_practical_rounding": "Show Practical Rounding",
        "d8_n_input": "Sample Size (N)",
        "d8_width_input": "CI Width (Total)",
        "d8_opt_bound": "Search Upper Limit",
        "d8_opt_tol": "Tolerance",
        
        # D9
        "title_d9": "D9: External Validation (Tailored)",
        "common_inputs": "Common Parameters",
        
        # UI Basics
        "search_placeholder": "Search methods...",
        "settings": "Settings",
        
        # Footer
        "footer_copyright": "© 2026 Prognostic Research Sample Size Tool. For academic/research only.",
        "footer_author": "Author & Maintenance: Minh Nguyen (minhnt@ump.edu.vn)",
        "footer_disclaimer": "Disclaimer: No clinical warranty; users are responsible for validation and interpretation.",

        "intro_complete_md": """
### Welcome

This app helps clinicians and researchers plan minimum sample size for prognostic research, including:
* Prognostic factor studies (power to detect associations),
* Clinical prediction model development (risk prediction), and
* Model validation / updating (external validation, recalibration).

It is designed for binary outcomes (e.g., event vs no event) and, for some modules, time-to-event outcomes (Cox PH).

Source code (download): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
or [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)    

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
### What this is

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
## C6: Development Simulation (Frequentist; custom DGM)

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

Choose the **smallest** (N) that passes.

---

# Inputs in the app (where to find them, typical values)

### 1) Outcome prevalence / event rate (p)

**What it is:** expected proportion of events in the development cohort.
**Where to get it:** local hospital incidence/prevalence (best), registry data, or prior studies in similar settings.
**Typical planning ranges:** 5%–15% are common in many clinical contexts (but vary widely).
**Tip:** If uncertain, run **sensitivity analysis** over a plausible range.

### 2) Number of predictor parameters (df) (P)

**What it is:** total degrees of freedom (excluding intercept), including:

* categorical dummies,
* spline bases,
* interactions,
* any additional engineered terms.
  **Where to get it:** your *final* planned model specification (TRIPOD-style pre-specification).
  **Typical values:** 10–30 df are common; higher requires stronger evidence and larger samples.

### 3) Target mean AUC (Mode A)

**What it is:** expected discrimination on new data (optimism-adjusted).
**Where to get it:** prior models in similar populations, pilot data, or published AUCs (prefer externally validated AUC).
**Typical values:** 0.70–0.85 are common; >0.90 is unusual and often optimistic.

### 4) Candidate sample sizes (N)

Provide a grid (e.g., 1000, 1500, 2000, 3000, 5000).
**Tip:** include a smaller and larger value to ensure the pass/fail threshold is crossed.

### 5) Number of simulations per (N): (R)

**Interpretation:** Monte Carlo replications.

* Demo: (R \\approx 200) (fast, higher Monte Carlo error)
* Final: (R \\ge 1000) (more stable)
  Monte Carlo standard error for a pass probability (\\hat{p}) is:
  [
  \\mathrm{MCSE}=\\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{R}}.
  ]
  Example: if (\\hat{p}=0.8) and (R=200), MCSE ≈ 0.028.

### 6) Performance criteria (Pass/Fail)

* **Mean calibration slope ≥ 0.9**
  (typical overfitting control threshold)
* **Pr(0.9 ≤ slope ≤ 1.1) ≥ 80%**
  (typical “acceptable calibration” probability threshold)
* **Mean AUC ≥ target**
  (discrimination target)

**Where to get thresholds:** practice guidelines, prior studies, and what is clinically acceptable.
**Common conventions:** slope range 0.90–1.10 and assurance 0.80 are frequently used for planning; use 0.90 assurance for higher certainty.

---

# Strengths and weaknesses

**Strengths**

* Flexible: accommodates correlations, non-linear terms, and realistic modeling choices.
* Directly targets new-data performance and calibration behavior.
* Naturally supports sensitivity analyses.

**Weaknesses**

* Results depend on DGM assumptions (garbage in → garbage out).
* Computationally intensive.
* Must simulate the full intended modeling pipeline; otherwise results can be misleading.

---

## Key references (2–5)

1. Pavlou M, Ambler G, Seaman SR, et al. *How to develop a more accurate risk prediction model when there are few events.* BMJ. 2015.
2. Riley RD, Snell KIE, Ensor J, et al. *Minimum sample size required for developing a multivariable prediction model: Part II—binary and time-to-event outcomes.* Statistics in Medicine. 2019.
3. Pavlou M, et al. *Methodology and software for simulation-based sample size calculation in prediction modeling* (sampsize development/related work). Statistics in Medicine. 2021.
4. Steyerberg EW. *Clinical Prediction Models: A Practical Approach to Development, Validation, and Updating.* 2nd ed. Springer. 2019.
""",
    "c7_content_md": """
## C7: Bayesian Assurance (MCMC)

### What this method is
**Bayesian assurance** is a simulation-based approach to sample size planning for **Bayesian model development** (here: Bayesian logistic regression for a binary outcome).  
Instead of targeting "power" (frequentist), assurance targets the **unconditional probability** that your study will meet **pre-specified success criteria** (e.g., calibration and discrimination thresholds, and/or posterior precision).

In plain terms:
> "If we repeat the whole study many times (data generation + Bayesian MCMC fitting), what is the probability that the fitted model will be good enough?"

---

### When to use
Use C7 when:
- Your final analysis is **Bayesian** and will be estimated by **MCMC**.
- You want sample size chosen to achieve **a target probability of success** (e.g., ≥80% or ≥90%).
- You can specify reasonable assumptions for:
  - event rate in your hospital cohort,
  - predictor correlation structure and distributions,
  - plausible effect sizes (from local pilot data or literature),
  - priors for regression coefficients.

### When NOT to use (or use with caution)
Avoid relying on C7 alone when:
- You cannot justify priors or a plausible **data-generating mechanism (DGM)**.
- You do not have the compute budget (MCMC is slow; results can be sensitive to MCMC settings).
- Your real development pipeline includes substantial data-adaptive steps (feature selection, heavy tuning) that you are **not** simulating.
- Data are clustered/multicenter but the DGM ignores clustering (may underestimate required N).

---

## Core model and DGM

### Bayesian logistic regression (analysis model)
\[
Y_i \sim \\text{Bernoulli}(\\pi_i), \\qquad
\\text{logit}(\\pi_i)=\\beta_0 + \\sum_{j=1}^{P}\\beta_j f_j(X_{ij})
\]
- \(P\) = number of predictor parameters (degrees of freedom; **exclude intercept**).
- \(f_j(\\cdot)\) represents your coding choices (linear term, dummies, spline bases, interactions).

**Example priors (typical weakly informative defaults):**
\[
\\beta_j \sim \\mathcal{N}(0,\\sigma_\\beta^2),\\quad \\sigma_\\beta \\in [1, 2.5],
\\qquad \\beta_0 \sim \\mathcal{N}(0, 5^2)
\]
(Your app may use fixed priors; users should run sensitivity analyses over plausible priors.)

### DGM for predictors (example equicorrelation)
If the app uses a single correlation parameter \\(\\rho\\) (equicorrelation):
\[
\\mathrm{Corr}(X_j, X_k)=\\rho \\quad (j\\neq k),
\\qquad
\\Sigma_{jk}=
\\begin{cases}
1,& j=k\\\\
\\rho,& j\\neq k
\\end{cases}
\]
Predictors are then generated from a correlated mechanism (e.g., Gaussian copula / multivariate normal core), and transformed into continuous/binary predictors as needed.

### Setting the event rate
The intercept (or a calibration constant) is chosen so that the marginal event rate matches the target prevalence:
\[
\\mathbb{E}[\\pi_i]=p
\]
This is typically solved numerically using Monte Carlo draws of \(X\).

---

## What "assurance" means (key formula)
Let:
- \\(\\theta\\) denote the "true" parameters under the DGM (effect sizes, correlation structure, etc.).
- \\(y\\) denote the observed dataset of size \\(N\\).
- \\(S(y)\\) be a **success indicator** that equals 1 if performance/precision criteria are met.

**Assurance at sample size \\(N\\):**
\[
\\mathcal{A}(N)=\\Pr(\\text{Success at }N)
=\\mathbb{E}_{\\theta}\\left[\\mathbb{E}_{y\\mid \\theta,N}\\left\\{S(y)\\right\\}\\right]
\]

**Monte Carlo estimate used in the app (for each candidate \\(N\\)):**
\[
\\widehat{\\mathcal{A}}(N)=\\frac{1}{R}\\sum_{r=1}^{R} S\\!\\left(y^{(r)}\right)
\]
where each replicate \\(r\\) simulates a dataset, fits the Bayesian model with MCMC, and evaluates success criteria.

Monte Carlo standard error (helpful for interpreting stability):
\[
\\mathrm{MCSE}\\left(\\widehat{\\mathcal{A}}(N)\\right)
=\\sqrt{\\frac{\\widehat{\\mathcal{A}}(N)\\left[1-\\widehat{\\mathcal{A}}(N)\\right]}{R}}
\]

**Decision rule:**
Choose the smallest \\(N\\) such that:
\[
\\widehat{\\mathcal{A}}(N)\\ge \\mathcal{A}_\\text{target}
\]
(e.g., 0.80 or 0.90).

---

## Success criteria (typical examples)
Your app may implement one or more of the following (user-selectable):
- **Calibration slope** in an acceptable range:
  \[
  0.90 \le b \le 1.10
  \]
  where \\(b\\) is estimated from a calibration model on validation/test data:
  \[
  \\text{logit}(Y)=a + b\\cdot \\text{logit}(\\widehat{p})
  \]
- **Discrimination** threshold:
  \[
  \\mathrm{AUC} \\ge 0.75 \\;(\\text{or your chosen target})
  \]
- **Posterior precision** target, e.g. 95% credible interval width for calibration slope:
  \[
  \\mathrm{Width}\\left(\\text{CrI}_{95\\%}(b)\\right) \\le w
  \\quad (\\text{e.g., } w=0.20)
  \]

---

## Input guide (where to find values; typical choices)

### 1) Outcome prevalence (event rate) \\(p\\)
**Where to get it:** local hospital cohort/registry; recent retrospective data.  
**Typical planning ranges:** 0.05–0.15 are common in many clinical settings, but use your disease context.  
**Tip:** If uncertain, run a sensitivity analysis over a plausible range.

### 2) Number of predictor parameters (df) \\(P\\)
**Where to get it:** your finalized model specification (count **parameters**, not variables).  
Include dummies, spline bases, interactions. Exclude intercept.  
**Typical range:** 10–30 df is common; larger df demands much larger \\(N\\) and stronger prior justification.

### 3) Predictor correlation \\(\\rho\\)
**Where to get it:** estimate from pilot/hospital data (correlation matrix of candidate predictors).  
If unknown, use sensitivity analysis (e.g., \\(\\rho=0, 0.1, 0.3\\)).  
**Typical:** mild-to-moderate correlations (0–0.3) are common; higher correlations increase instability and may increase required \\(N\\).

### 4) Candidate sample sizes \\(N\\)
Choose a grid wide enough to cross the pass/fail boundary (e.g., 500, 1000, 1500, 2000, …).  
Start from feasibility constraints (available charts/records) and expand upward.

### 5) Number of simulations per \\(N\\) (replicates) \\(R\\)
- **Demo:** 50–200 (fast; higher MC error)  
- **Final planning:** ≥500–1000 (more stable assurance estimate)  
Use MCSE to judge stability.

### 6) Assurance threshold \\(\\mathcal{A}_\\text{target}\\)
- **0.80**: common for feasibility-driven planning  
- **0.90**: preferred when you want higher confidence in meeting criteria

---

## Strengths and weaknesses
**Strengths**
- Fully aligned with Bayesian workflows; directly targets **posterior** success/precision.
- Flexible: accommodates complex DGM, correlations, and performance-based criteria.
- Can incorporate prior knowledge and realistically handle rare events with regularizing priors.

**Weaknesses**
- Computationally intensive; results can depend on MCMC settings and convergence.
- Sensitive to DGM and prior assumptions → requires sensitivity analyses.
- Must simulate the actual planned pipeline to avoid under/over-estimation.

---

## Key references (2–5)
1) O'Hagan A. Assurance in clinical trial design. *Pharmaceutical Statistics.* 2005.  
2) Pan J, Banerjee S. bayesassurance: An R Package for Calculating Sample Size and Bayesian Assurance. *The R Journal.* 2023.  
3) Gelman A, Jakulin A, Pittau MG, Su Y-S. A weakly informative default prior distribution for logistic and other regression models. *The Annals of Applied Statistics.* 2008.  
4) Sahu SK, Smith TMF. Bayesian methods of sample size determination. *Statistical Methodology / related Bayesian SSD literature.* 2006.
""",
        # Email & Reporting
        "report_header": "Report & Downloads",
        "btn_download_report": "Download Report (Text)",
        "btn_download_html": "Download Report (Formatted HTML)",
        "btn_download_csv": "Download Results (CSV)",
        "report_title": "Sample Size Calculation Report",
        "footer_text": "For research purposes only. Please verify with a statistician.",
        "email_header": "Email Results",
        "email_to": "Recipient Email",
        "email_send_btn": "Send Email",
        "email_success": "Email sent successfully!",
        "email_error": "Error sending email:",
        "email_settings": "Email Settings (SMTP)",
        "email_sender": "Your Email",
        "email_password": "App Password",
        "email_subject_default": "Sample Size Analysis Results",
}
