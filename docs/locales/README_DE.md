# Stichprobenberechnung für Prognostische Forschung (Prognostic Research Sample Size Tool)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Ein Toolkit zur Berechnung der minimalen Stichprobengröße in der klinischen Prognoseforschung. Diese Anwendung wurde für Datenwissenschaftler, Statistiker und klinische Forscher entwickelt und implementiert validierte statistische Methoden für **Vorhersagemodell-Entwicklung**, **Externe Validierung**, **Prognosefaktor-Studien** und **Modellaktualisierung**.

🔗 **Zur App:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **Hinweis**: Inhalte in Chinesisch, Japanisch, Französisch und Deutsch wurden teilweise durch KI übersetzt. Bei Fragen wenden Sie sich bitte an den App-Administrator.

---

## 1. Überblick und Zweck

Diese Anwendung bietet eine Reihe von Tools, um den komplexen Anforderungen der Stichprobenplanung in der medizinischen Forschung gerecht zu werden. Im Gegensatz zu einfachen Power-Rechnern konzentriert sich dieses Tool auf die spezifischen Nuancen der *prognostischen Modellierung*, bei der das Ziel oft eine genaue Risikoschätzung (Kalibrierung und Diskriminierung) statt eines einfachen Hypothesentests ist.

### Hauptfunktionen

* **Methodische Strenge**: Implementiert Algorithmen, die strikt der begutachteten statistischen Literatur folgen (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Validierung**: Die Kernberechnungen wurden mit renommierten R-Paketen (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) abgeglichen, um die Genauigkeit sicherzustellen.
* **Mehrsprachige Unterstützung**: Volle Unterstützung für Englisch und Vietnamesisch sowie teilweise Unterstützung für Chinesisch, Japanisch, Französisch und Deutsch, was die internationale Zusammenarbeit erleichtert.
* **Sensitivitätsanalyse**: Die integrierte Stapelverarbeitung ermöglicht es Forschern zu bewerten, wie die Stichprobenanforderungen über eine Reihe von Annahmen (z. B. variierende Prävalenz oder erwartetes $R^2$) variieren.

---

## 2. Methodenkatalog

Die Anwendung ist nun hierarchisch strukturiert (Kategorie A: Binäre Ergebnisse).

### A. Binäre Ergebnisse (Binary Outcomes)

#### A1. Schnellüberprüfungen (Quick Checks)

| Methode | Beschreibung | Ziel |
| :--- | :--- | :--- |
| **A1.1: Ereignisse pro Variable (EPV)** | Faustregel-Heuristik. | Machbarkeitsprüfung. |
| **A1.2: Präzision des Basisrisikos** | Schätzung der Prävalenz mit einer bestimmten KI-Breite. | Deskriptive Epidemiologie. |

#### A2. Prognosefaktoren (Prognostic Factors)

| Methode | Beschreibung | Ziel |
| :--- | :--- | :--- |
| **A2.1: Logistische Power (Hsieh)** | Power zur Erkennung einer Odds Ratio (OR). | Assoziationsstudien. |
| **A2.2: Cox Power (Schoenfeld)** | Power zur Erkennung einer Hazard Ratio (HR). | Überlebensanalyse. |

#### A3. Modellentwicklung (Prediction Model Development)

| Methode | Beschreibung | Ziel |
| :--- | :--- | :--- |
| **A3.1: Analytischer Ansatz (Riley)** | **Empfohlen.** Anpassung von Schrumpfung, Optimismus und Präzision. | Entwicklung neuer Modelle. |
| **A3.2: Simulationsdesign** | Simulation spezifischer DGMs für komplexe Szenarien. | Entwicklung (Komplex). |
| **A3.3: Bayes'sche Assurance** | MCMC-Simulation für garantierte Erfolgswahrscheinlichkeit. | Bayes'sche Entwicklung. |

#### A4. Validierung / Aktualisierung (Validation / Updating)

| Methode | Beschreibung | Ziel |
| :--- | :--- | :--- |
| **A4.1: AUC Präzision** | KI-Breite für AUC (C-Statistik). | Validierung (Diskriminierung). |
| **A4.2: Externe Validierung** | Präzision für O/E, Kalibrierungssteigung und AUC. | Validierung (Vollständig). |
| **A4.3: Validierungssimulation** | Simulation basierend auf LP-Verteilung. | Validierung (Simulation). |
| **A4.4: Modellaktualisierung** | Stichprobengröße zur Neukalibrierung (Intercept/Slope). | Modell-Updating. |

---

## 3. Installation und lokale Ausführung

So stellen Sie diese Anwendung in Ihrer eigenen Infrastruktur bereit:

### Voraussetzungen

* Python 3.9+
* Git

### Bereitstellungsschritte

1. **Repository klonen (Clone)**

   ```bash
   git clone https://github.com/nguyenminh2301/pmsample.git
   cd pmsample
   ```

2. **Umgebungseinrichtung**
   Es wird dringend empfohlen, eine virtuelle Umgebung (virtual environment) zu verwenden.

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Abhängigkeiten installieren**

   ```bash
   pip install -r requirements.txt
   ```

4. **Anwendung starten**

   ```bash
   streamlit run pmsampsize_app/app.py
   ```

---

## 5. Zitation

Wenn Sie dieses Tool in Ihrer Forschung verwenden, zitieren Sie es bitte wie folgt:

> Nguyen, M. (2025). Prognostic Research Sample Size Tool (Version 1.0) [Software]. Available at https://pmsample.streamlit.app/

Oder verwenden Sie den BibTeX-Eintrag:

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

## 4. Haftungsausschluss

**Nur für akademische und Forschungszwecke.**

Diese Software ist eine Implementierung statistischer Methoden, die in begutachteter Literatur veröffentlicht wurden. Obwohl alle Anstrengungen unternommen wurden, um die Genauigkeit der Algorithmen sicherzustellen, übernehmen die Autoren und Betreuer keine Haftung für das Design oder die Ergebnisse einer Studie, die auf diesem Tool basiert.

* **Benutzerverantwortung**: Benutzer sind dafür verantwortlich, die Eingabeparameter zu überprüfen und die Ergebnisse im Kontext ihrer spezifischen klinischen Domäne zu interpretieren.
* **Keine medizinische Garantie**: Dieses Tool bietet keine medizinische Beratung.

---

**Autor & Betreuung:**
Minh Nguyen (minhnt@ump.edu.vn)
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
(Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam)
