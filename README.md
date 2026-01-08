# Minimum Sample Size Estimation for Prognostic Research

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A toolkit designed for calculating minimum sample sizes in clinical prognostic research. Developed for data scientists, statisticians, and clinical researchers, this application implements validated statistical methods for **Prediction Model Development**, **External Validation**, **Prognostic Factor Studies**, and **Model Updating**.

🔗 **Live Application:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **Note**: Partial support for Chinese, Japanese, French, and German added via AI. Please contact the app admin for any questions.

---

## 1. Overview and Purpose

This application provides a suite of tools to address the complex requirements of sample size planning in medical research. Unlike basic power calculators, this tool focuses on the specific nuances of *prognostic modeling*, where the goal is often accurate estimation of risk (calibration and discrimination) rather than simple hypothesis testing.

### Key Capabilities

* **Methodological Rigor**: Implements algorithms strictly adhering to peer-reviewed statistical literature (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Validation**: Core calculations have been verified against established R packages (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) to ensure accuracy.
* **Bilingual Ecosystem**: Fully localized for English and Vietnamese, facilitating international collaboration.
* **Sensitivity Analysis**: Integrated batch processing allows researchers to evaluate how sample size requirements vary across a range of assumptions (e.g., varying prevalence or anticipated $R^2$).

---

## 2. Methodology Catalog

The application is structured into four primary modules, each targeting a specific phase of the research lifecycle.

### A. Preliminary Feasibility Assessment

| Method                                      | Description                                                                                                                 | Application Scenarios                                                                                                                                              |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A1: Events Per Variable (EPV/EPP)** | A heuristic approach based on the ratio of events to candidate predictor parameters.                                        | *Feasibility checks only.* **Not recommended as the primary justification** for a protocol due to its inability to account for overfitting or calibration. |
| **A2: Precision of Baseline Risk**    | Estimates the sample size required to estimate the outcome prevalence with a specified Confidence Interval (CI) half-width. | Descriptive epidemiology; planning calibration-in-the-large.                                                                                                       |

### B. Prognostic Factor Studies (Association)

| Method                                  | Description                                                                                                                      | Reference                     |
| :-------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :---------------------------- |
| **B3: Logistic Regression Power** | Calculates sample size to detect a target Odds Ratio (OR) for a specific predictor, adjusting for covariance with other factors. | **Hsieh et al. (1998)** |
| **B4: Cox Regression Power**      | Calculates the number of events required to detect a target Hazard Ratio (HR) in survival analysis.                              | **Schoenfeld (1983)**   |

### C. Prediction Model Development (Recommended)

This is the core module for developing new clinical prediction models.

| Method                                    | Description                                                                                          | Key Objectives                                                                                                                              |
| :---------------------------------------- | :--------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **C5: Analytical Approach (Riley)** | **The Gold Standard.** Closed-form solution for multivariable model development.               | 1. Limit global shrinkage ($S \ge 0.9$).`<br>`2. Limit optimism in apparent performance.`<br>`3. Precise estimation of the intercept. |
| **C6: Simulation-Based Design**     | Simulates specific Data Generating Mechanisms (DGM) to estimate requirements for complex models.     | Non-linear terms, complex interactions, specific correlation structures.                                                                    |
| **C7: Bayesian Assurance**          | MCMC-based simulation to determine sample size with a guaranteed probability of success (Assurance). | Bayesian model development.                                                                                                                 |

### D. Validation and Updating

Tools for planning external validation of existing models.

| Method                                   | Description                                                                                         | Reference                                         |
| :--------------------------------------- | :-------------------------------------------------------------------------------------------------- | :------------------------------------------------ |
| **D8: AUC Precision**              | Calculates N to achieve a specific Confidence Interval width for the AUC (C-statistic).             | **Hanley & McNeil (1982)**                  |
| **D9: Tailored Validation Sizing** | Calculates N to ensure precise estimation of O/E ratio, Calibration Slope, and AUC.                 | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: Validation Simulation**     | Simulation-based planning using the distribution of the Linear Predictor (LP).                      | **Snell et al. (2021)**                     |
| **D11: Model Updating**            | Sample size required to update (recalibrate) an existing model (Intercept/Slope) for a new setting. | **Van Calster et al.**                      |

---

## 3. Installation and Local Execution

To deploy this application within your own infrastructure:

### Prerequisites

* Python 3.9+
* Git

### Deployment Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/nguyenminh2301/pmsample.git
   cd pmsample
   ```
2. **Environment Setup**
   It is highly recommended to use a virtual environment.

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Launch Application**

   ```bash
   streamlit run pmsampsize_app/app.py
   ```

---

## 4. Disclaimer and Liability

**For Academic and Research Use Only.**

This software is an implementation of statistical methods published in peer-reviewed literature. While every effort has been made to ensure the accuracy of the algorithms, the authors and maintainers assume no liability for the design or results of any study based on this tool.

* **User Responsibility**: Users are responsible for verifying the input parameters and interpreting the results within the context of their specific clinical domain.
* **No Clinical Warranty**: This tool does not provide medical advice.

---

**Author & Maintainer:**
Minh Nguyen (minhnt@ump.edu.vn)
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
