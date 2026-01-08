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

Die Anwendung ist in vier Hauptmodule unterteilt, die jeweils auf eine bestimmte Phase des Forschungszyklus abzielen.

### A. Vorläufige Machbarkeitsbewertung

| Methode | Beschreibung | Anwendungsszenarien |
| :--- | :--- | :--- |
| **A1: Ereignisse pro Variable (EPV/EPP)** | Eine Faustregel basierend auf dem Verhältnis von Ereignissen zu Kandidaten-Prädiktorparametern. | *Nur zur Machbarkeitsprüfung.* **Nicht als Hauptbegründung** für ein Protokoll empfohlen, da Überanpassung oder Kalibrierung nicht berücksichtigt werden. |
| **A2: Präzision des Basisrisikos** | Schätzt die benötigte Stichprobengröße, um die Prävalenz mit einer angegebenen Konfidenzintervall (KI) Breite zu schätzen. | Deskriptive Epidemiologie; Planung der Gesamtkalibrierung (calibration-in-the-large). |

### B. Prognosefaktor-Studien (Assoziation)

| Methode | Beschreibung | Referenz |
| :--- | :--- | :--- |
| **B3: Logistische Regression Power** | Berechnet die Stichprobengröße, um eine Ziel-Odds Ratio (OR) für einen bestimmten Prädiktor zu erkennen, angepasst an die Kovarianz mit anderen Faktoren. | **Hsieh et al. (1998)** |
| **B4: Cox Regression Power** | Berechnet die Anzahl der Ereignisse, die erforderlich sind, um eine Ziel-Hazard Ratio (HR) in der Überlebensanalyse zu erkennen. | **Schoenfeld (1983)** |

### C. Entwicklung von Vorhersagemodellen (Empfohlen)

Dies ist das Kernmodul zum Aufbau neuer klinischer Vorhersagemodelle.

| Methode | Beschreibung | Hauptziele |
| :--- | :--- | :--- |
| **C5: Analytischer Ansatz (Riley)** | **Der Goldstandard.** Geschlossene Lösung für die Entwicklung multivariater Modelle. | 1. Begrenzung der globalen Schrumpfung (shrinkage $S \ge 0.9$).<br />2. Begrenzung des Optimismus in der scheinbaren Leistung.<br />3. Präzise Schätzung des Interzepts. |
| **C6: Simulationsbasiertes Design** | Simuliert spezifische Datengenerierungsmechanismen (DGM), um Anforderungen für komplexe Modelle abzuschätzen. | Nichtlineare Terme, komplexe Interaktionen, spezifische Korrelationsstrukturen. |
| **C7: Bayes'sche Assurance** | MCMC-basierte Simulation zur Bestimmung der Stichprobengröße mit einer garantierten Erfolgswahrscheinlichkeit (Assurance). | Entwicklung Bayes'scher Modelle. |

### D. Validierung und Aktualisierung

Tools zur Planung der externen Validierung bestehender Modelle.

| Methode | Beschreibung | Referenz |
| :--- | :--- | :--- |
| **D8: AUC Präzision** | Berechnet N, um eine bestimmte Konfidenzintervallbreite für die AUC (C-Statistik) zu erreichen. | **Hanley & McNeil (1982)** |
| **D9: Maßgeschneiderte Validierungsgröße** | Berechnet N, um eine präzise Schätzung des O/E-Verhältnisses, der Kalibrierungssteigung und der AUC sicherzustellen. | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: Validierungssimulation** | Simulationsbasierte Planung unter Verwendung der Verteilung des linearen Prädiktors (LP). | **Snell et al. (2021)** |
| **D11: Modellaktualisierung** | Erforderliche Stichprobengröße zur Aktualisierung (Neukalibrierung) eines bestehenden Modells (Intercept/Steigung) für eine neue Umgebung. | **Van Calster et al.** |

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
