# *Prognostic Research Sample Size Tool*

A rigorous, bilingual (Vietnamese/English) toolkit for calculating sample sizes in prognostic research (model development, validation, and prognostic factors).

## 🚀 Features

* **Comprehensive Methods**: Covers 9+ statistical methods across 4 domains (Quick Tools, Prognostic Factors, Model Development, Validation).
* **Academically Rigorous**:
  * Replicates logic from validated R packages (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`).
  * Verified against package examples and original papers (Riley et al., Hanley-McNeil, Hsieh, etc.).
* **Bilingual Interface**: Full English and Vietnamese support (including formulas and warnings).
* **Modern UI**:
  * Sidebar Tree Navigation.
  * Theme Support (Coder, Light, Dark).
  * Scenario Grid Generation for Sensitivity Analysis.
* **Reporting**: Export results to CSV and generating Markdown/HTML reports.

## 🧮 Method Catalog

### A. Quick / Basic Tools

* **A1: Rules of Thumb (EPV/EPP)**
  * Simple calculation based on Events Per Variable (10, 20, etc.).
* **A2: Baseline Risk Precision**
  * Estimating overall prevalence with desired Confidence Interval width.

### B. Prognostic Factors (Power)

* **B3: Logistic Regression Power (Hsieh)**
  * Sample size for detecting Odds Ratios in binary outcomes.
* **B4: Cox Regression Power (Schoenfeld)**
  * Sample size (Events) for detecting Hazard Ratios in survival analysis.

### C. Prediction Model Development

* **C5: Riley et al. (Analytical)** ⭐️
  * The "Gold Standard" for multivariable prediction models (Binary/Survival).
  * Ensures shrinkage < 0.9, precise R-squared, and precise intercept.
  * Matches `pmsampsize` R package logic.
* **C6: Development Simulation**
  * Simulation-based approach for specific data generation mechanisms.
* **C7: Bayesian Aassurance**
  * MCMC-based simulation to guarantee probability of success (Bayesian Assurance).

### D. Validation & Updating

* **D8: AUC Precision (Hanley-McNeil)** ⭐️
  * Calculate N to achieve a specific Confidence Interval width for AUC.
  * Exact replica of R package `presize::prec_auc` (v0.3.9).
* **D9: External Validation (Tailored)** ⭐️
  * External validation sizing using:
    * **Riley/Archer (`pmvalsampsize`)**: Precision of O/E, Slope, C.
    * **Pavlou (`sampsizeval`)**: SE targets.
* **D10: Ext. Validation (Simulation)** ⭐️
  *   Simulation-based sizing based on LP distribution and miscalibration.
  *   Replicates logic from **Snell et al. (2021)** and accompanying R code (`gscollins1973/External-validation-sample-size`).
  *   Supports C-stat, Calibration Slope, and ln(O/E) targets.

## 🛠 Installation & Usage

### Option 1: One-Click (Windows)

Double-click **`start_app.bat`**. This script sets up the environment and launches the app automatically.

### Option 2: Manual (Python)

```bash
# 1. Clone repo
git clone <repo-url>
cd pmsampsize_app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run App
streamlit run app.py
```

## 📚 Logic & Validation

This application prioritizes accuracy. We strictly replicate established R packages:

| Method               | Source R Package                    | Status      | Notes                                                            |
| :------------------- | :---------------------------------- | :---------- | :--------------------------------------------------------------- |
| **C5 (Riley)** | `pmsampsize`                      | ✅ Verified | Validated against 1M simulation runs for$R^2_{CS}$ conversion. |
| **D8 (AUC)**   | `presize` (v0.3.9)                | ✅ Verified | Validated against unit tests and manual formulae.                |
| **D9 (Val)**   | `pmvalsampsize` & `sampsizeval` | ✅ Verified | Uses numerical integration for precise LP parameters.            |

## ⚠️ Disclaimer

**For academic and research use only.**
This tool is provided "as is" without warranty of any kind. Users are responsible for validating results and interpreting them in the context of their specific clinical scenarios.

---

**Author**: Minh Nguyen (minhnt@ump.edu.vn)
