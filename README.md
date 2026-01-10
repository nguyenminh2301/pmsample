# Prognosis Model Sample Size Toolkit (Prognosis-N)

> *A toolkit for Development, Validation, and Updating of Clinical Prediction Models.*

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

* **Methodological**: Implements algorithms strictly adhering to peer-reviewed statistical literature (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Validation**: Core calculations have been verified against established R packages (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) to ensure accuracy.
* **Bilingual Ecosystem**: Fully localized for English and Vietnamese, facilitating international collaboration.
* **Sensitivity Analysis**: Integrated batch processing allows researchers to evaluate how sample size requirements vary across a range of assumptions (e.g., varying prevalence or anticipated $R^2$).

---

## 2. Methodology Catalog

The application is structured into four primary modules, each targeting a specific phase of the research lifecycle.

### A. Binary Outcomes

#### Subgroup A1: Quick Checks

| Method                                  | Description                                       |
| :-------------------------------------- | :------------------------------------------------ |
| **A1.1: Rules of Thumb (EPV)**    | Heuristic check (events per variable).            |
| **A1.2: Baseline Risk Precision** | Sample size for estimating prevalence (CI width). |

#### Subgroup A2: Prognostic Factors

| Method                                 | Description                                   |
| :------------------------------------- | :-------------------------------------------- |
| **A2.1: Logistic Power (Hsieh)** | Power to detect an OR for a single predictor. |
| **A2.2: Cox Power (Schoenfeld)** | Power to detect a HR for a single predictor.  |

#### Subgroup A3: Model Development (Prediction)

| Method                                    | Description                                                                   |
| :---------------------------------------- | :---------------------------------------------------------------------------- |
| **A3.1: Riley et al. (Analytical)** | **Gold Standard.** Development sample size for overfitting & precision. |
| **A3.2: Development Simulation**    | Simulation-based planning for complex models (DGM).                           |
| **A3.3: Bayesian Assurance**        | MCMC-based assurance for Bayesian models.                                     |

#### Subgroup A4: Validation / Updating

| Method                                         | Description                                                    |
| :--------------------------------------------- | :------------------------------------------------------------- |
| **A4.1: AUC Precision**                  | Sample size for AUC CI width (Hanley-McNeil).                  |
| **A4.2: External Validation (Tailored)** | Target calibration and discrimination precision (Riley/Snell). |
| **A4.3: Ext. Validation (Simulation)**   | Simulation-based validation planning (LP distribution).        |
| **A4.4: Model Updating**                 | Sample size for recalibrating intercept/slope.                 |

### B. Continuous Outcomes

| Method                                  | Description                                          |
| :-------------------------------------- | :--------------------------------------------------- |
| **B1: Green's Rule**              | Heuristic for linear regression (50 + 8k).           |
| **B2: Riley et al. (Continuous)** | Analytical method for linear regression (residuals). |

### C. Survival Outcomes

| Method                                | Description                                       |
| :------------------------------------ | :------------------------------------------------ |
| **C1: Riley et al. (Survival)** | Analytical method for Cox models (time-to-event). |

---

## 3. Installation and Local Execution

To deploy this application within your own infrastructure:

**Repositories:**

* **GitLab (Primary)**: [`gitlab.com/minhthiennguyen/pmsample`](https://gitlab.com/minhthiennguyen/pmsample.git)
* **GitHub (Mirror)**: [`github.com/nguyenminh2301/pmsample`](https://github.com/nguyenminh2301/pmsample.git)

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

## 5. Citation

If you use this tool in your research, please cite it as follows:

> Nguyen, Minh. (2025). Prognostic Research Sample Size Tool (Version 1.0) [Software]. Available at https://pmsample.streamlit.app/

Or use the BibTeX entry:

```bibtex
@software{nguyen2025pmsample,
  author = {Nguyen, Minh},
  title = {Prognostic Research Sample Size Tool},
  year = {2025},
  url = {https://pmsample.streamlit.app/},
  version = {1.0}
}
```

---

**Author & Maintainer:**
Minh Nguyen MPH (Mr/ He/ him)
email: minhnt@ump.edu.vn
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
