# Prognostic Research Sample Size Tool

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A rigorous, professional-grade toolkit for calculating minimum sample sizes in clinical prognostic research. Designed for data scientists, statisticians, and clinical researchers, this application implements validated statistical methods for **Prediction Model Development**, **External Validation**, **Prognostic Factor Studies**, and **Model Updating**.

🔗 **Live Demo:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

---

## 🚀 Key Features

*   **Comprehensive Methodological Coverage:**
    *   **Development:** Riley et al. analytical approach (C5), Simulation-based sizing (C6), Bayesian Assurance (C7).
    *   **Validation:** AUC precision (D8), Tailored validation sizing (D9), Simulation-based validation (D10), Updating/Recalibration (D11).
    *   **Power Analysis:** Logistic Power (B3), Cox PH Power (B4).
    *   **Quick Tools:** EPV Rules (A1), Prevalence Precision (A2).
*   **Academically Rigorous:**
    *   Strict adherence to established statistical literature (Riley et al. 2019/2020, Hanley & McNeil 1982, Hsieh 1989).
    *   Logic verified against R packages: `pmsampsize`, `presize`, `pmvalsampsize`, and `sampsizeval`.
*   **Bilingual Support:** Fully localized for **English** and **Vietnamese** (with partial Korean support), making it accessible to a wider research community.
*   **Professional UI/UX:**
    *   Built with [Streamlit](https://streamlit.io/) for a responsive, interactive experience.
    *   **Sensitivity Analysis Mode:** Batch processing for ranges of parameters (e.g., varying outcome prevalence or $R^2$).
    *   **Reporting:** Auto-generation of detailed Markdown/HTML reports and CSV exports.

---

## 🧮 Method Catalog

The application is structured into four primary modules:

### A. Quick / Basic Tools
| Method | Description | Use Case |
| :--- | :--- | :--- |
| **A1: EPV/EPP Rules** | Heuristic based on Events Per Variable (e.g., 10, 20). | Preliminary feasibility checks only. |
| **A2: Baseline Risk Precision** | Sample size for estimating prevalence with a target CI width (Wilson score). | Epidemiology/Descriptive studies. |

### B. Prognostic Factors (Power Analysis)
| Method | Description | Source / Reference |
| :--- | :--- | :--- |
| **B3: Logistic Power** | Hsieh's formula for detecting Odds Ratios in binary outcomes. | **Hsieh et al. (1998)** |
| **B4: Cox Power** | Schoenfeld's formula for detecting Hazard Ratios in time-to-event analysis. | **Schoenfeld (1983)** |

### C. Prediction Model Development (Recommended)
| Method | Description | Key Features |
| :--- | :--- | :--- |
| **C5: Riley et al. (Analytical)** | **Gold Standard** for multivariable model development. Ensures shrinkage control ($S \ge 0.9$), small optimism, and precise intercept. | Replicates `pmsampsize` package. |
| **C6: Dev Simulation** | Variable-specific simulation for complex design matrices. | Handles non-linearity & interactions. |
| **C7: Bayesian Assurance** | MCMC-based simulation to guarantee probability of success. | For Bayesian workflows. |

### D. Validation & Updating
| Method | Description | Source / Reference |
| :--- | :--- | :--- |
| **D8: AUC Precision** | Calculates N for a target CI width of the AUC (C-statistic). | **Hanley & McNeil (1982)** / `presize` |
| **D9: External Validation** | "Tailored" sizing for O/E, Calibration Slope, and AUC targets. | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: Val Simulation** | Simulation-based validation planning using LP distributions. | **Snell et al. (2021)** |
| **D11: Updating** | Sample size for Recalibration (Intercept/Slope) stability. | **Van Calster et al.** |

---

## 🛠 Installation & Local Usage

To run the application locally on your machine:

### Prerequisites
*   Python 3.9 or higher.
*   Git.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nguyenminh2301/pmsample.git
    cd pmsample
    ```

2.  **Create a virtual environment (Optional but Recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    streamlit run pmsampsize_app/app.py
    ```

The app will open in your default browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
pmsampsize_app/
├── app.py                  # Main entry point
├── methods/                # Individual method implementations (modules)
│   ├── a1_epv.py
│   ├── b3_hsieh.py
│   ├── c5_riley.py
│   └── ...
├── utils/                  # Utility functions
│   ├── common.py           # Shared calculations
│   ├── i18n.py             # Translation aggregator
│   └── locales/            # Localization files (En, Vi, Ko)
└── requirements.txt        # Python dependencies
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for:
*   Bug fixes.
*   New sample size methods.
*   Translation improvements.

---

## 📜 License & Disclaimer

**License:** MIT License.

**Disclaimer:** This tool is intended for research and educational purposes. While statistically rigorous, users are responsible for the inputs provided and the clinical interpretation of the results. Authors are not liable for decisions made based on this software.

---

**Maintained by:** Minh Nguyen (minhnt@ump.edu.vn)
