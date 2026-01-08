
DE = {
    "title": "Stichprobenrechner für Prognoseforschung (Prognostic Research Sample Size Tool)",
    "sidebar_title": "Konfiguration",
    "language": "Sprache / Language",
    "mode": "Methodenauswahl",
    "mode_riley": "Methode C5: Riley et al. (Analytisch)",
    "mode_bayes": "Methode C6: Bayes (Simulation)",
    "mode_single": "Einzelszenario",
    "mode_batch": "Sensitivitätsanalyse",
    "method1_tab": "Methode C5 (Riley)",
    "method2_tab": "Methode C6 (Bayes)",
    "nav_title": "Navigation",
    "nav_readme": "Detaillierte Dokumentation (README)",
    "nav_intro": "Einführung & Formeln",
    "nav_calc": "Stichprobenrechner",
    "intro_heading": "Willkommen",
    "intro_text": "Dieses Tool hilft bei der Berechnung der minimalen Stichprobengröße für die Entwicklung klinischer Vorhersagemodelle für binäre Ergebnisse.",
    "formula_heading": "Mathematischer Rahmen (Methode C5)",
    "formula_intro": "Methode C5 verwendet analytische Lösungen von Riley et al., während Methode C6 Bayes'sche MCMC-Simulationen nutzt.",
    "sens_guide_title": "💡 Anleitung zur Sensitivitätsanalyse (Batch-Modus)",
    "sens_guide_text": """
    - **Bereich**: Geben Sie `min-max` ein (z.B. `0.05-0.10`). Schritte werden automatisch generiert.
    - **Spezifische Werte**: Geben Sie eine kommagetrennte Liste ein (z.B. `0.05, 0.10, 0.15`).
    """,
    "detail_view": "Detaillierte Szenarioberechnung anzeigen",
    "footer_refs": "Referenzen: Riley et al. (2018, 2020), BayesAssurance.",
    "calc_btn": "Berechnen",
    "results": "Ergebnisse",
    "sanity": "Plausibilitätsprüfung (EPV-Regeln)",
    "download_csv": "CSV herunterladen",
    "download_report": "Vollständigen Bericht herunterladen",
    "error_p": "Prävalenz muss zwischen 0 und 1 liegen.",
    "error_auc": "AUC muss zwischen 0.5 und 1 liegen.",
    "error_parse": "Eingabe konnte nicht verarbeitet werden.",
    
    # Riley specific
    "riley_inputs": "Eingabeparameter (Riley)",
    "prevalence": "Ergebnisprävalenz / Ereignisrate",
    "prevalence_help": "Anteil der Teilnehmer mit dem Ereignis (0 < p < 1).",
    "parameters": "Anzahl der Prädiktorparameter (df)",
    "parameters_help": "Gesamtzahl der Freiheitsgrade (ohne Intercept).",
    "shrinkage": "Ziel-Gesamtschrumpfung (Target Shrinkage, S)",
    "shrinkage_help": "Gewünschter Schrumpfungsfaktor (Standard 0.9).",
    "perf_measure": "Erwartete Leistung",
    "perf_auc": "AUC (C-Statistik)",
    "perf_r2": "Cox-Snell R-Quadrat",
    "perf_cons": "Konservativ (15% des max. R2)",
    
    # Bayesian specific 
    "perf_cons_help": "Konservativ (15% des max. R2)",
    "perf_auc_help": "Erwartete AUC (C-Statistik)",
    "perf_r2_help": "Erwartetes Cox-Snell R-Quadrat",
    
    # Bayesian specific
    "bayes_inputs": "Simulationseinstellungen (Bayes'sche Assurance)",
    "dgm_settings": "Datengenerierungsmechanismus (DGM)",
    "sim_settings": "Simulation & MCMC",
    "eval_settings": "Bewertungskriterien",
    "n_candidates": "Kandidaten-Stichprobengrößen (kommagetrennt)",
    "n_candidates_help": "Liste der zu testenden N. Z.B.: 500, 1000, 1500.",
    "correlation": "Prädiktor-Korrelation (rho)",
    "n_sims": "Simulationen pro N",
    "assurance_threshold": "Assurance-Schwellenwert (Zielwahrscheinlichkeit)",
    "run_simulation": "Bayes'sche Simulation starten",
    "simulation_running": "Simulation läuft... Dies kann einige Zeit dauern.",
    "assurance_result": "Assurance-Analyse",
    
    # Method 6 (Dev Sim)
    "mode_dev_sim": "Methode 6: Entwicklungssimulation (Frequentistisch)",
    "method6_tab": "Methode 6 (Simulation)",
    "dev_sim_intro": "Simulationsbasierte Größenbestimmung für die Modellentwicklung (frequentistisch, ähnlich wie `samplesizedev`).",
    "dev_mode_simple": "Modus A: Einfach (AUC-gesteuert)",
    "dev_mode_custom": "Modus B: Benutzerdefinierter DGM",
    "target_auc": "Ziel-Durchschnitts-AUC (C-Statistik)",
    "target_auc_help": "Der Algorithmus sucht nach Beta-Koeffizienten, um diese AUC zu erreichen.",
    "criteria_settings": "Leistungskriterien (Bestanden/Nicht bestanden)",
    "crit_slope_mean": "Mittlere Kalibrierungssteigung >= 0.9",
    "crit_slope_ci": "Pr(0.9 <= Steigung <= 1.1) >= 80%",
    "crit_auc": "Mittlere AUC >= Ziel",
    "audit_trail": "RNG-Audit-Trail (JSON)",
    "future_methods": "Kommt in zukünftigen Versionen...",
    
    # Quick Methods
    "method_quick_tab": "A. Schnell / Basis",
    "quick_mode_epv": "A1: EPV / EPP Regeln (Heuristik)",
    "quick_mode_risk": "A2: Basisrisiko-Präzision (KI-Breite)",
    "target_epv": "Ziel-Ereignisse pro Parameter (EPP)",
    "target_epv_help": "Übliche heuristische Werte sind 10, 15, 20. EPP wird gegenüber EPV bevorzugt.",
    "epv_warning_title": "⚠️ Wichtige Warnung",
    "epv_warning_text": "EPV/EPP sind nur grobe heuristische Regeln. Sie garantieren weder eine gute Kalibrierung/Diskriminierung noch verhindern sie Optimismus-Bias. Sehr empfindlich gegenüber Variablenselektion und nicht-linearen Termen.",
    "ci_level": "Konfidenzniveau",
    "ci_half_width": "Ziel-Halbwertsbreite (Fehlermarge)",
    "ci_method": "KI-Methode",
    "ci_method_wilson": "Wilson Score (Empfohlen)",
    "ci_method_wald": "Wald (Einfach)",
    "ci_method_cp": "Clopper-Pearson (Konservativ)",
    "risk_help": "Berechnet N, um die Ereignisrate p mit einer gegebenen Genauigkeit zu schätzen. Garantiert NICHT die Leistung des Vorhersagemodells.",
    
    # Power Methods (B)
    "title_b3": "B3: Logistische Power (Hsieh)",
    "title_b4": "B4: Cox Power (Schoenfeld)",
    "interpretation": "Interpretation",
    
    # UI Basics
    "d8_assumptions": "**Annahmen**: Verwendet Varianznäherung nach Hanley & McNeil (1982). Nimmt symmetrische Normalität der AUC an. Numerische Optimierung zur Bestimmung von N.",
    "d8_mode_n_to_width": "KI-Breite aus N berechnen",
    "d8_mode_width_to_n": "Benötigtes N aus KI-Breite berechnen",
    "d8_opt_settings": "Erweiterte Optimierer-Einstellungen",
    "d8_practical_rounding": "Praktische Rundung anzeigen",
    "d8_n_input": "Stichprobengröße (N)",
    "d8_width_input": "KI-Breite (Gesamt)",
    "d8_opt_bound": "Suchobergrenze",
    "d8_opt_tol": "Toleranz",
    
    # Validations (D)
    "title_d8": "D8: AUC Präzision (Hanley-McNeil)",
    "d8_desc": "Stichprobengröße zur Schätzung der AUC mit gewünschter Präzision (KI-Breite).",
    "auc_expected": "Erwartete AUC (C-Statistik)",
    "formulas_header": "📚 Formeln und technische Details (Formulas & Technical Details)",
    "d8_assumptions": "**Annahmen**: Verwendet Varianznäherung nach Hanley & McNeil (1982). Nimmt symmetrische Normalität der AUC an. Numerische Optimierung zur Bestimmung von N.",
    "d8_mode_n_to_width": "KI-Breite aus N berechnen",
    "d8_mode_width_to_n": "N aus KI-Breite berechnen",
    "d8_opt_settings": "Erweiterte Optimierer-Einstellungen",
    "d8_practical_rounding": "Praktische Rundung anzeigen",
    "d8_n_input": "Stichprobengröße (N)",
    "d8_width_input": "KI-Breite (Gesamt)",
    "d8_opt_bound": "Suchobergrenze",
    "d8_opt_tol": "Toleranz",
    
    # D9
    "title_d9": "D9: Externe Validierung (Maßgeschneidert)",
    "common_inputs": "Gemeinsame Parameter",
    
    # UI Basics
    "search_placeholder": "Methode suchen...",
    "settings": "Einstellungen",
    
    # Footer
    "footer_copyright": "© 2026 Prognostic Research Sample Size Tool. Nur für akademische/forschungszwecke.",
    "footer_author": "Erstellt und gepflegt von: Minh Nguyen (minhnt@ump.edu.vn) - Dept. of Epidemiology, Faculty of Public Health, UMP Ho Chi Minh City",
    "footer_disclaimer": "Haftungsausschluss: Keine klinische Garantie. Der Benutzer ist für Validierung und Interpretation verantwortlich.",

    "intro_complete_md": """
### Willkommen (Welcome)

Diese Anwendung hilft Klinikern und Forschern bei der Planung der minimalen Stichprobengröße für prognostische Forschung, einschließlich:
* Prognosefaktor-Studien (Assoziationsstärke),
* Entwicklung klinischer Vorhersagemodelle (Risikovorhersage), und
* Validierung / Aktualisierung von Modellen (externe Validierung, Neukalibrierung).

Sie ist für binäre Ergebnisse (z.B. Ereignis vs. kein Ereignis) konzipiert, wobei einige Module auch für Überlebenszeitergebnisse (Cox PH) angepasst sind.

Quellcode (Download): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
oder [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)    

### Erste Schritte (Neue Benutzer)

#### 1. Klären Sie Ihr Forschungsziel
* Testen Sie einen einzelnen prognostischen Faktor (Assoziation)?
* Bauen Sie ein Vorhersagemodell?
* Validieren Sie ein bestehendes Modell in einer neuen Population?

#### 2. Schätzen Sie die Ereignisrate $p$ (oder den Anteil der Ereignisse bei Überlebenszeit)
* Lokale Krankenhausdaten bevorzugt (am besten).
* Wenn unsicher, geben Sie einen Bereich ein und führen Sie eine Sensitivitätsanalyse durch.

#### 3. Zählen Sie die Modellkomplexität (Parameter / df) korrekt
Verwenden Sie Parameter (Freiheitsgrade), nicht nur die "Anzahl der Variablen".
* Binärer Prädiktor: 1 df
* Kategorische Variable mit $L$ Ebenen: $L-1$ df
* Splines (RCS mit $K$ Knoten): $K-1$ df
* Interaktionen: $df(A \\times B) = df(A) \\cdot df(B)$

#### 4. Wählen Sie eine Methode aus dem Katalog unten
* Verwenden Sie **"Schnelle Tools" (Quick tools)** nur für grobe Planung.
* Verwenden Sie **Riley / Simulation / Assurance** Methoden für die Entwicklung von Vorhersagemodellen.

---

### Wann diese App verwendet werden sollte (und wann nicht)

**Verwenden Sie sie für:**
* Planung retrospektiver oder prospektiver Kohortenstudien zu Prognose/Vorhersage
* Entwicklung oder Validierung von Risikomodellen
* Schätzung der Stichprobengröße basierend auf Präzision der Prävalenz oder AUC
* Design externer Validierung mit Zielen für Kalibrierung und Diskriminierung

**Verwenden Sie sie NICHT als Hauptwerkzeug für:**
* Design von randomisierten kontrollierten Studien (verwenden Sie RCT-spezifische Power/Stichprobenmethoden)
* Planung von diagnostischen Genauigkeitsstudien für Sensitivität/Spezifität ohne prädiktive Modellierung
* Erwartung einer einzigen "richtigen" Zahl: Stichprobenplanung erfordert Annahmen und sollte Sensitivitätsanalysen beinhalten

---

### Verfügbare Methoden (Übersicht)

#### A. Schnell / Basis (Schnell, Approximativ)

**A1 — Faustregeln (EPV/EPP) (Heuristik)**
* **Wann:** Schnelle Prüfung, ob Ihre Ereignisse "grob ausreichend" für die geplante Modellgröße sind.
* **Wann vermeiden:** Ihr Modell enthält Splines/Interaktionen/Variablenselektion oder die Ereignisrate ist niedrig—EPV/EPP garantiert keine gute Kalibrierung oder geringen Optimismus-Bias.
* **Haupteingaben:** Ereignisrate $p$, Parameter $P$ (df), Ziel-EPP (z.B. 10/15/20)
* **Hauptausgaben:** Benötigte Ereignisse $E=t \\cdot P$, Benötigte Stichprobe $N=\\lceil E/p \\rceil$
* **Pro:** Sehr einfach. Gut für frühe Machbarkeitsprüfungen.
* **Contra:** Kann irreführend sein. Nicht leistungsbasiert.

**A2 — Basisrisiko-Präzision (Prävalenz KI-Breite)**
* **Wann:** Ziel ist die Schätzung der Ereignisrate $p$ mit einer gewünschten KI-Halbwertsbreite (z.B. ±2%).
* **Wann vermeiden:** Sie möchten Garantien für die Leistung des Vorhersagemodells (AUC/Kalibrierungssteigung).
* **Haupteingaben:** Erwartetes $p$, KI-Methode (Wilson empfohlen), Konfidenzniveau, Ziel-Halbwertsbreite $d$
* **Hauptausgaben:** Minimales $N$, das KI-Halbwertsbreite $\\le d$ erfüllt
* **Pro:** Direktes Präzisionsziel. Transparente Annahmen.
* **Contra:** Bezieht sich nur auf Prävalenz, nicht auf Modellleistung.

#### B. Prognosefaktor (Power) (Fokus Assoziation, nicht Größe des Vorhersagemodells)

**B3 — Logistische OR Power (Hsieh)**
* **Wann:** Sie möchten Power, um eine Ziel-Odds Ratio (OR) für einen prognostischen Faktor in der logistischen Regression zu erkennen.
* **Wann vermeiden:** Hauptziel ist die Entwicklung eines Vorhersagemodells (Kalibrierung/Diskriminierung), nicht Hypothesentests.
* **Haupteingaben:** Basisrisiko $p_0$, Ziel-OR, Alpha, Power, Expositionsprävalenz (binär) oder SD (kontinuierlich), $R^2$ mit Kovariaten (optional)
* **Hauptausgaben:** Benötigtes $N$ (und implizite Ereignisse) zur Erkennung der OR
* **Pro:** Klassischer Power-Rahmen für Assoziation.
* **Contra:** Behandelt nicht die Leistung des Vorhersagemodells. Empfindlich gegenüber Eingabeannahmen.

**B4 — Cox HR Power (Schoenfeld)**
* **Wann:** Zeit-bis-Ereignis-Ergebnisse; Sie möchten Power, um eine Hazard Ratio (HR) unter Cox PH zu erkennen.
* **Wann vermeiden:** PH-Annahmen könnten nicht zutreffen oder der Anteil der Ereignisse ist sehr unsicher.
* **Haupteingaben:** HR, Alpha, Power, Allokationsverhältnis (binär) oder SD (kontinuierlich), Erwarteter Anteil der Ereignisse während des Follow-ups
* **Hauptausgaben:** Benötigte Ereignisse; Umwandlung in $N$ unter Verwendung des Ereignisanteils
* **Pro:** Weitgehend akzeptiert. Ereignisbasierte Planung ist intuitiv.
* **Contra:** Hängt stark von Annahmen zu Ereignisanteil und Follow-up/Zensierung ab.

#### C. Entwicklung von Vorhersagemodellen (Empfohlen für den Aufbau von Risikomodellen)

**C5 — Riley et al. (Analytische Methode; ähnlich pmsampsize)**
* **Wann:** Entwicklung multivariater Vorhersagemodelle; Sie möchten Überanpassung kontrollieren und angemessene Präzision sicherstellen.
* **Wann vermeiden:** Sie können keine vernünftigen Annahmen zu Prävalenz und erwarteter Modellleistung (AUC oder $R^2$) machen. Verwenden Sie in diesem Fall Sensitivitätsanalyse oder Simulation.
* **Haupteingaben:** Ereignisrate $p$, Parameter $P$ (df), Ziel-Schrumpfung (z.B. 0.90), Erwartete Modellleistung (AUC oder Cox–Snell $R^2$)
* **Hauptausgaben:** Minimales $N$, das mehrere Kriterien erfüllt (Überanpassungskontrolle + Präzision)
* **Pro:** Prinzipienbasiert. Leistungsfokussiert. Weit zitiert.
* **Contra:** Hängt von Leistungsannahmen ab. Erfordert sorgfältiges Zählen der df.

**C6 — Entwicklungssimulation (Frequentistisch; samplesizedev/benutzerdefinierter DGM)**
* **Wann:** Sie bevorzugen es, "zu simulieren, was Sie tun werden", insbesondere bei Nichtlinearitäten/Interaktionen oder benutzerdefinierter Datenstruktur.
* **Wann vermeiden:** Sie können keinen vernünftigen Datengenerierungsmechanismus (DGM) spezifizieren oder benötigen sofortige Ergebnisse (rechenintensiv).
* **Haupteingaben:** Kandidaten-$N$-Raster, DGM-Annahmen (Verteilung/Korrelation Prädiktoren/Effekte), Leistungsziele (z.B. Kalibrierungssteigung, AUC-Schwellenwert), Simulationswiederholungen, Seed
* **Hauptausgaben:** Minimales $N$, das Ziele mit akzeptabler Wahrscheinlichkeit/Präzision erreicht
* **Pro:** Flexibel. Passt zu komplexer Modellierung.
* **Contra:** Starke Annahmen. Hohe Rechenkosten.

**C7 — Bayes'sche Assurance (MCMC)**
* **Wann:** Ihr endgültiges Modell wird Bayes'sch via MCMC geschätzt, und Sie möchten eine Stichprobengröße basierend auf Assurance (Wahrscheinlichkeit, Leistungsziele a posteriori zu erreichen).
* **Wann vermeiden:** Sie können Priors nicht rechtfertigen oder haben begrenztes Rechenbudget.
* **Haupteingaben:** DGM, Priors, Kandidaten-$N$, MCMC-Einstellungen, Assurance-Schwellenwert (z.B. 80%/90%), Leistungs-/Präzisionsziele
* **Hauptausgaben:** Minimales $N$, das Assurance-Schwellenwert erfüllt
* **Pro:** Passt zum Bayes'schen Workflow. Zielt direkt auf Posterior-Kriterien.
* **Contra:** Rechenintensiv. Erfordert Spezifikation von Priors.

#### D. Validierung / Aktualisierung (Für bestehende Modelle)

**D8 — AUC Präzision (Hanley–McNeil / presize)**
* **Wann:** Ihr Validierungsziel ist die Präzision der AUC (KI-Breite).
* **Wann vermeiden:** Kalibrierung (Steigung/CITL) ist ein Hauptanliegen—diese Methode zielt nur auf AUC ab.
* **Haupteingaben:** Erwartete AUC, Prävalenz oder Fall:Kontroll-Verhältnis, Konfidenzniveau, Ziel-KI-Breite
* **Hauptausgaben:** Minimales $N$, um gewünschte AUC-KI-Breite zu erreichen
* **Pro:** Einfach. Schnelle Planung für Diskriminierungspräzision.
* **Contra:** Näherungsvarianz. Ignoriert Kalibrierung.

**D9 — Externe Validierung (Maßgeschneidert; pmvalsampsize / sampsizeval)**
* **Wann:** Sie möchten Validierungsumfang für mehrere Leistungsmetriken (Kalibrierung + Diskriminierung) bestimmen, erfordert typischerweise Annahme zur LP-Verteilung.
* **Wann vermeiden:** Sie können LP-Verteilungsannahmen oder erwartete Leistung nicht rechtfertigen.
* **Haupteingaben:** Prävalenz, Erwartete AUC, Ziel Steigung/CITL Kalibrierung, Ziel KI-Breite oder SE, Annahme LP-Verteilung
* **Hauptausgaben:** Empfohlenes $N$, das Präzisionskriterien für jede Metrik erfüllt
* **Pro:** Maßgeschneidert. Fokus auf Kalibrierung.
* **Contra:** Erfordert zusätzliche Annahmen. Komplexer.

**D10 — Externe Validierung (Simulation; LP-basiert)**
* **Wann:** Sie können die Verteilung des linearen Prädiktors (LP) in der Ziel-Validierungspopulation spezifizieren/schätzen und wünschen simulationsbasierte Präzisionsplanung.
* **Wann vermeiden:** LP-Verteilung unbekannt und nicht annäherbar.
* **Haupteingaben:** LP-Verteilung (Normal/Beta/Empirisch), Fehlkalibrierungsparameter, Ziel KI-Breite der Metriken, Wiederholungen, Seed
* **Hauptausgaben:** Minimales $N$, das Präzisionsziele unter Simulation erreicht
* **Pro:** Sehr flexibel. Entspricht "Simulieren, was Sie erwarten".
* **Contra:** Starke Annahmen. Rechenkosten.

**D11 — Aktualisierung / Neukalibrierung (Intercept/Steigung)**
* **Wann:** Sie möchten ein bestehendes Modell neukalibrieren (Aktualisierung von Intercept und/oder Steigung) und benötigen ausreichende Präzision.
* **Wann vermeiden:** Sie entwickeln ein völlig neues Modell (verwenden Sie C5–C7).
* **Haupteingaben:** Aktualisierungstyp (nur Intercept vs Intercept+Steigung), Ereignisrate, Zielpräzision
* **Hauptausgaben:** Ausreichendes $N$ für stabile Aktualisierung
* **Pro:** Praktisch für den realen Einsatz.
* **Contra:** Hängt von Annahmen zum lokalen Case-Mix und Modellübertragbarkeit ab.

---

#### Haftungsausschluss

Keine klinische Garantie. Der Benutzer ist für Validierung und Interpretation verantwortlich. Dokumentieren Sie immer Ihre Annahmen und führen Sie Sensitivitätsanalysen durch.

#### Kontakt

Erstellt und gepflegt von: Minh Nguyen (minhnt@ump.edu.vn)
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
