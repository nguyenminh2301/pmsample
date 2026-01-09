
FR = {
    "title": "Ooutil de Taille d'Échantillon pour la Recherche Pronostique",
    "sidebar_title": "Configuration",
    "language": "Langue / Language",
    "mode": "Sélection de la Méthode",
    
    # Sidebar
    "lbl_settings": "Paramètres",
    "lbl_theme": "Thème",
    "lbl_theme_light": "Clair",
    "lbl_theme_dark": "Sombre",
    "lbl_theme_coder": "Coder",
    # Subgroups
    "sg_a1": "A1. Vérifications rapides",
    "sg_a2": "A2. Facteurs pronostiques",
    "sg_a3": "A3. Développement de modèle",
    "sg_a4": "A4. Validation",
    "sg_b1": "B1. Vérifications rapides",
    "sg_b2": "B2. Développement de modèle",
    "sg_c1": "C1. Développement de modèle",
    
    # New Hierarchy Titles
    "title_a1_1": "A1.1: Règles empiriques (EPV)",
    "title_a1_2": "A1.2: Précision du risque de base",
    "title_a2_1": "A2.1: Puissance Logistique (Hsieh)",
    "title_a2_2": "A2.2: Puissance Cox (Schoenfeld)",
    "title_a3_1": "A3.1: Riley et al. (Analytique)",
    "title_a3_2": "A3.2: Simulation de développement",
    "title_a3_3": "A3.3: Assurance Bayésienne",
    "title_a4_1": "A4.1: Précision AUC (Hanley-McNeil)",
    "title_a4_2": "A4.2: Validation externe (Personnalisée)",
    "title_a4_3": "A4.3: Validation externe (Simulation)",
    "title_b1": "B1: Règle de Green",
    "title_b2": "B2: Riley et al. (Continu)",
    "title_c1": "C1: Riley et al. (Survie)",

    "mode_riley": "Méthode A3.1: Riley et al. (Analytique)",
    "mode_bayes": "Méthode A3.3: Assurance Bayésienne (Simulation)",
    "mode_single": "Scénario Unique",
    "mode_batch": "Analyse de Sensibilité",
    "method1_tab": "Méthode A3.1 (Riley)",
    "method2_tab": "Méthode A3.3 (Bayesien)",
    "nav_title": "Navigation",
    "nav_readme": "Documentation Détaillée (README)",
    "nav_intro": "Introduction & Formules",
    "nav_calc": "Calculateur de Taille d'Échantillon",
    "intro_heading": "Bienvenue",
    "intro_text": "Cet outil aide à calculer la taille minimale de l'échantillon pour développer des modèles de prédiction clinique pour des résultats binaires.",
    "formula_heading": "Cadre Mathématique (Méthode A3.1)",
    "formula_intro": "La méthode A3.1 utilise les solutions analytiques de Riley et al., tandis que la méthode A3.3 utilise la simulation Bayesienne MCMC.",
    "sens_guide_title": "💡 Guide d'Analyse de Sensibilité (Mode Batch)",
    "sens_guide_text": """
    - **Plage**: Entrez `min-max` (ex: `0.05-0.10`). Les étapes sont générées automatiquement.
    - **Valeurs Spécifiques**: Entrez une liste séparée par des virgules (ex: `0.05, 0.10, 0.15`).
    """,
    "detail_view": "Voir le calcul détaillé du scénario",
    "footer_refs": "Références: Riley et al. (2018, 2020), BayesAssurance.",
    "calc_btn": "Calculer",
    "results": "Résultats",
    "sanity": "Vérification de Cohérence (Règles EPV)",
    "download_csv": "Télécharger CSV",
    "download_report": "Télécharger le Rapport Complet",
    "error_p": "La prévalence doit être entre 0 et 1.",
    "error_auc": "L'AUC doit être entre 0.5 et 1.",
    "error_parse": "Impossible d'analyser l'entrée.",
    
    # Riley specific
    "riley_inputs": "Paramètres d'Entrée (Riley)",
    "prevalence": "Prévalence du Résultat / Taux d'Événement",
    "prevalence_help": "Proportion de participants ayant l'événement (0 < p < 1).",
    "parameters": "Nombre de Paramètres Predictifs (ddl)",
    "parameters_help": "Degrés de liberté totaux (hors interception).",
    "shrinkage": "Rétrécissement Global Cible (Target Shrinkage, S)",
    "shrinkage_help": "Facteur de rétrécissement souhaité (défaut 0.9).",
    "perf_measure": "Performance Anticipée",
    "perf_auc": "AUC (Statistique C)",
    "perf_r2": "R-carré de Cox-Snell",
    "perf_cons": "Conservateur (15% du R2 max)",
    
    # Bayesian specific 
    "perf_cons_help": "Conservateur (15% du R2 max)",
    "perf_auc_help": "AUC (Statistique C) anticipée",
    "perf_r2_help": "R-carré de Cox-Snell anticipé",
    
    # Bayesian specific
    "bayes_inputs": "Paramètres de Simulation (Assurance Bayesienne)",
    "dgm_settings": "Mécanisme de Génération de Données (DGM)",
    "sim_settings": "Simulation & MCMC",
    "eval_settings": "Critères d'Évaluation",
    "n_candidates": "Tailles d'échantillon candidates (séparées par des virgules)",
    "n_candidates_help": "Liste des N à tester. Ex: 500, 1000, 1500.",
    "correlation": "Corrélation des prédicteurs (rho)",
    "n_sims": "Simulations par N",
    "assurance_threshold": "Seuil d'Assurance (Probabilité Cible)",
    "run_simulation": "Lancer la Simulation Bayesienne",
    "simulation_running": "Simulation en cours... Cela peut prendre du temps.",
    "assurance_result": "Analyse d'Assurance",
    
    # Method 6 (Dev Sim)
    "mode_dev_sim": "Méthode A3.2: Simulation de Développement (Fréquentiste)",
    "method6_tab": "Méthode A3.2 (Simulation)",
    "dev_sim_intro": "Taille basée sur la simulation pour le développement de modèles (fréquentiste, similaire à `samplesizedev`).",
    "dev_mode_simple": "Mode A: Simple (Piloté par AUC)",
    "dev_mode_custom": "Mode B: DGM Personnalisé",
    "target_auc": "AUC Moyenne Cible (Statistique C)",
    "target_auc_help": "L'algorithme recherchera les coefficients Beta pour atteindre cette AUC.",
    "criteria_settings": "Critères de Performance (Succès/Échec)",
    "crit_slope_mean": "Pente d'Étalonnage Moyenne >= 0.9",
    "crit_slope_ci": "Pr(0.9 <= Pente <= 1.1) >= 80%",
    "crit_auc": "AUC Moyenne >= Cible",
    "audit_trail": "Piste d'Audit RNG (JSON)",
    "future_methods": "À venir dans les futures versions...",
    
    # Quick Methods
    "method_quick_tab": "A. Rapide / Basique",
    "quick_mode_epv": "A1.1: Règles EPV / EPP (Heuristique)",
    "quick_mode_risk": "A1.2: Précision du Risque de Base (Largeur IC)",
    "target_epv": "Événements par Paramètre Cibles (EPP)",
    "target_epv_help": "Les valeurs heuristiques courantes sont 10, 15, 20. EPP est préféré à EPV.",
    "parameters_short": "paramètres",
    "target_epv_short": "EPP",
    "prevalence_short": "prévalence",
    "subjects_short": "sujets",
    "interpretation_a1": "Calcul",
    "result_a1": "Taille d'échantillon requise",
    "epv_warning_title": "⚠️ Avertissement Important",
    "epv_warning_text": "EPV/EPP ne sont que des règles heuristiques approximatives. Elles ne garantissent ni un bon étalonnage / discrimination, ni l'absence de biais d'optimisme. Très sensibles à la sélection de variables et aux termes non linéaires.",
    "ci_level": "Niveau de Confiance",
    "ci_half_width": "Demi-largeur Cible (Marge d'Erreur)",
    "ci_method": "Méthode IC",
    "ci_method_wilson": "Score de Wilson (Recommandé)",
    "ci_method_wald": "Wald (Simple)",
    "ci_method_cp": "Clopper-Pearson (Conservateur)",
    "risk_help": "Calcule N pour estimer le taux d'événement p avec une précision donnée. Ne garantit PAS la performance du modèle de prédiction.",
    
    # Power Methods (B)
    "title_b3": "A2.1: Puissance Logistic (Hsieh)",
    "title_b4": "A2.2: Puissance Cox (Schoenfeld)",
    "interpretation": "Interprétation",
    
    # UI Basics
    "d8_assumptions": "**Hypothèses**: Utilise l'approximation de variance de Hanley & McNeil (1982). Suppose une normalité symétrique de l'AUC. Optimisation numérique pour trouver N.",
    "d8_mode_n_to_width": "Calculer la largeur IC à partir de N",
    "d8_mode_width_to_n": "Calculer N requis à partir de la largeur IC",
    "d8_opt_settings": "Paramètres Avancés de l'Optimiseur",
    "d8_practical_rounding": "Afficher l'arrondi pratique",
    "d8_n_input": "Taille d'Échantillon (N)",
    "d8_width_input": "Largeur IC (Totale)",
    "d8_opt_bound": "Limite Supérieure de Recherche",
    "d8_opt_tol": "Tolérance",
    
    # Validations (D)
    "title_d8": "A4.1: Précision AUC (Hanley-McNeil)",
    "d8_desc": "Taille d'échantillon pour estimer l'AUC avec la précision souhaitée (largeur IC).",
    "auc_expected": "AUC (Statistique C) Anticipée",
    "formulas_header": "📚 Formules et Détails Techniques (Formulas & Technical Details)",
    "d8_assumptions": "**Hypothèses**: Utilise l'approximation de variance de Hanley & McNeil (1982). Suppose une normalité symétrique de l'AUC. Optimisation numérique pour trouver N.",
    "d8_mode_n_to_width": "Calculer la largeur IC à partir de N",
    "d8_mode_width_to_n": "Calculer N à partir de la largeur IC",
    "d8_opt_settings": "Paramètres Avancés de l'Optimiseur",
    "d8_practical_rounding": "Afficher l'arrondi pratique",
    "d8_n_input": "Taille d'Échantillon (N)",
    "d8_width_input": "Largeur IC (Totale)",
    "d8_opt_bound": "Limite Supérieure de Recherche",
    "d8_opt_tol": "Tolérance",
    
    # D9
    "title_d9": "A4.2: Validation Externe (Sur Mesure)",
    "common_inputs": "Paramètres Communs",
    
    # UI Basics
    "search_placeholder": "Rechercher une méthode...",
    "settings": "Paramètres",
    
    # Footer
    "footer_copyright": "© 2026 Outil de Taille d'Échantillon pour la Recherche Pronostique. Usage académique/recherche uniquement.",
    "footer_author": "Créé et maintenu par: Minh Nguyen (minhnt@ump.edu.vn) - Dept. of Epidemiology, Faculty of Public Health, UMP Ho Chi Minh City",
    "footer_disclaimer": "Avis de non-responsabilité: Pas de garantie clinique. L'utilisateur est responsable de la validation et de l'interprétation.",

    "intro_complete_md": """
### Bienvenue (Welcome)

Cette application aide les cliniciens et chercheurs à planifier la taille d'échantillon minimale pour la recherche pronostique, incluant :
* Études de facteurs pronostiques (puissance d'association),
* Développement de modèles de prédiction clinique (prédiction de risque), et
* Validation / Mise à jour de modèles (validation externe, recalibrage).

Elle est conçue pour les résultats binaires (ex: événement vs pas d'événement), avec certains modules adaptés aux résultats de survie (Cox PH).

Code source (Télécharger): [https://gitlab.com/minhthiennguyen/pmsample/](https://gitlab.com/minhthiennguyen/pmsample/)
ou [https://github.com/nguyenminh2301/pmsample.git](https://github.com/nguyenminh2301/pmsample.git)    

### Pour Commencer (Nouveaux Utilisateurs)

#### 1. Clarifiez votre Objectif de Recherche
* Testez-vous un facteur pronostique unique (association) ?
* Construisez-vous un modèle de prédiction ?
* Validez-vous un modèle existant dans une nouvelle population ?

#### 2. Estimez le Taux d'Événement $p$ (ou la fraction d'événements pour la survie)
* Données hospitalières locales préférées (le mieux).
* Si incertain, entrez une plage et exécutez une analyse de sensibilité.

#### 3. Comptez la Complexité du Modèle (Paramètres / ddl) Correctement
Utilisez les paramètres (degrés de liberté), pas seulement le "nombre de variables".
* Prédicteur binaire: 1 ddl
* Variable catégorielle à $L$ niveaux: $L-1$ ddl
* Splines (RCS avec $K$ nœuds): $K-1$ ddl
* Interactions: $ddl(A \\times B) = ddl(A) \\cdot ddl(B)$

#### 4. Sélectionnez une Méthode dans le Catalogue ci-dessous
* Utilisez **"Outils Rapides" (Quick tools)** uniquement pour une planification approximative.
* Utilisez les méthodes **Riley / Simulation / Assurance** pour le développement de modèles de prédiction.

---

### Quand utiliser cette application (et quand ne pas l'utiliser)

**Utilisez-la pour :**
* Planifier des études de cohorte rétrospectives ou prospectives sur le pronostic/prédiction
* Développer ou valider des modèles de risque
* Estimer la taille d'échantillon basée sur la précision de la prévalence ou de l'AUC
* Concevoir une validation externe avec des objectifs de calibration et de discrimination

**NE l'utilisez PAS comme outil principal pour :**
* Concevoir des Essais Contrôlés Randomisés (utilisez des méthodes de puissance/taille d'échantillon spécifiques aux ECR)
* Planifier des études de précision diagnostique pour la sensibilité/spécificité sans modélisation prédictive
* Attendre un seul nombre "correct" : la planification de taille d'échantillon nécessite des hypothèses et doit inclure une analyse de sensibilité

---

### Méthodes Disponibles (Aperçu)

#### A. Rapide / Basique (Rapide, Approximatif)

**A1 — Règles Empiriques (EPV/EPP) (Heuristique)**
* **Quand :** Besoin d'une vérification rapide si vos événements sont "approximativement suffisants" pour la taille de modèle prévue.
* **Quand Éviter :** Votre modèle a des splines/interactions/sélection de variables, ou le taux d'événements est faible—EPV/EPP ne garantit pas un bon étalonnage ou un faible biais d'optimisme.
* **Entrées Clés :** Taux d'événement $p$, Paramètres $P$ (ddl), EPP cible (ex: 10/15/20)
* **Sorties Clés :** Événements Requis $E=t \\cdot P$, Échantillon Requis $N=\\lceil E/p \\rceil$
* **Pour :** Très simple. Bon pour les vérifications de faisabilité précoces
* **Contre :** Peut être trompeur. Non basé sur la performance

**A2 — Précision du Risque de Base (Largeur IC de la Prévalence)**
* **Quand :** Objectif d'estimer le taux d'événement $p$ avec une demi-largeur d'IC souhaitée (ex: ±2%).
* **Quand Éviter :** Vous voulez des garanties de performance de modèle de prédiction (AUC/pente d'étalonnage).
* **Entrées Clés :** $p$ anticipé, Méthode IC (Wilson recommandé), Niveau de confiance, Demi-largeur cible $d$
* **Sorties Clés :** $N$ minimal satisfaisant la demi-largeur IC $\\le d$
* **Pour :** Objectif de précision direct. Hypothèses transparentes
* **Contre :** Concerne uniquement la prévalence, pas la performance du modèle

#### B. Facteur Pronostique (Puissance) (Focus Association, pas taille de modèle prédictif)

**B3 — Puissance Logistic OR (Hsieh)**
* **Quand :** Vous voulez de la puissance pour détecter un Odds Ratio (OR) cible pour un facteur pronostique dans une régression logistique.
* **Quand Éviter :** L'objectif principal est de développer un modèle de prédiction (calibration/discrimination), pas le test d'hypothèse.
* **Entrées Clés :** Risque de base $p_0$, OR cible, Alpha, Puissance, Prévalence exposition (binaire) ou SD (continu), $R^2$ avec covariables (optionnel)
* **Sorties Clés :** $N$ requis (et événements implicites) pour détecter l'OR
* **Pour :** Cadre classique de puissance pour l'association
* **Contre :** Ne traite pas la performance du modèle prédictif. Sensible aux hypothèses d'entrée

**B4 — Puissance Cox HR (Schoenfeld)**
* **Quand :** Résultats de temps-jusqu'à-événement; vous voulez de la puissance pour détecter un Hazard Ratio (HR) sous Cox PH.
* **Quand Éviter :** Les hypothèses PH peuvent ne pas tenir, ou la fraction d'événements est très incertaine et ne peut être estimée raisonnablement.
* **Entrées Clés :** HR, Alpha, Puissance, Ratio d'allocation (binaire) ou SD (continu), Fraction d'événements anticipée pendant le suivi
* **Sorties Clés :** Événements requis; convertit en $N$ en utilisant la fraction d'événements
* **Pour :** Largement accepté. La planification basée sur les événements est intuitive
* **Contre :** Dépend fortement des hypothèses de fraction d'événement et de suivi/censure

#### C. Développement de Modèle de Prédiction (Recommandé pour construire des modèles de risque)

**C5 — Riley et al. (Méthode Analytique; similaire à pmsampsize)**
* **Quand :** Développement de modèle de prédiction multivarié; vous voulez contrôler le surajustement et assurer une précision adéquate.
* **Quand Éviter :** Vous ne pouvez fournir aucune hypothèse raisonnable sur la prévalence et la performance attendue du modèle (AUC ou $R^2$). Utilisez l'analyse de sensibilité ou la simulation dans ce cas.
* **Entrées Clés :** Taux d'événement $p$, Paramètres $P$ (ddl), Rétrécissement cible (ex: 0.90), Performance modèle anticipée (AUC ou Cox–Snell $R^2$)
* **Sorties Clés :** $N$ minimal satisfaisant plusieurs critères (contrôle surajustement + précision)
* **Pour :** Fondé sur des principes. Focus sur la performance. Largement cité
* **Contre :** Dépend des hypothèses de performance. Nécessite un comptage soigneux des ddl

**C6 — Simulation de Développement (Fréquentiste; samplesizedev/DGM sur mesure)**
* **Quand :** Vous préférez "simuler ce que vous ferez", particulièrement avec des non-linéarités/interactions ou une structure de données personnalisée.
* **Quand Éviter :** Vous ne pouvez spécifier un mécanisme de génération de données (DGM) raisonnable, ou vous avez besoin de résultats instantanés (intensif en calcul).
* **Entrées Clés :** Grille de candidats $N$, Hypothèses DGM (dist/corrélation prédicteurs/effets), Objectifs performance (ex: pente étalonnage, seuil AUC), Répétitions simulation, Graine
* **Sorties Clés :** $N$ minimum atteignant les objectifs avec probabilité/précision acceptable
* **Pour :** Flexible. S'aligne avec la modélisation complexe
* **Contre :** Hypothèses lourdes. Coût de calcul élevé

**C7 — Assurance Bayesienne (MCMC)**
* **Quand :** Votre modèle final sera estimé par Bayes MCMC, et vous voulez une taille d'échantillon basée sur l'Assurance (probabilité de satisfaire les objectifs de performance a posteriori).
* **Quand Éviter :** Vous ne pouvez justifier les a priori, ou vous avez un budget de calcul limité.
* **Entrées Clés :** DGM, A priori, Candidats $N$, Paramètres MCMC, Seuil d'Assurance (ex: 80%/90%), Objectifs performance/précision
* **Sorties Clés :** $N$ minimal satisfaisant le seuil d'Assurance
* **Pour :** S'aligne avec le flux de travail Bayesien. Cible directement les critères a posteriori
* **Contre :** Intensif en calcul. Nécessite la spécification des a priori

#### D. Validation / Mise à jour (Pour modèles existants)

**D8 — Précision AUC (Hanley–McNeil / presize)**
* **Quand :** Votre objectif de validation est la précision de l'AUC (largeur IC).
* **Quand Éviter :** L'étalonnage (pente/CITL) est une préoccupation majeure—cette méthode cible uniquement l'AUC.
* **Entrées Clés :** AUC anticipée, Prévalence ou ratio cas:témoins, Niveau confiance, Largeur IC cible
* **Sorties Clés :** $N$ minimal pour atteindre la largeur IC d'AUC souhaitée
* **Pour :** Simple. Planification rapide pour la précision de discrimination
* **Contre :** Variance approximative. Ignore l'étalonnage

**D9 — Validation Externe (Sur Mesure; pmvalsampsize / sampsizeval)**
* **Quand :** Vous voulez dimensionner la validation pour plusieurs métriques de performance (calibration + discrimination), nécessitant généralement une hypothèse sur la distribution du LP.
* **Quand Éviter :** Vous ne pouvez justifier les hypothèses de distribution LP ou de performance attendue.
* **Entrées Clés :** Prévalence, AUC anticipée, Cible pente/CITL étalonnage, Cible largeur IC ou SE, Hypothèse distribution LP
* **Sorties Clés :** $N$ recommandé satisfaisant les critères de précision pour chaque métrique
* **Pour :** Sur mesure. Focus sur l'étalonnage
* **Contre :** Nécessite des hypothèses supplémentaires. Plus complexe

**D10 — Validation Externe (Simulation; basé sur LP)**
* **Quand :** Vous pouvez spécifier/estimer la distribution du Prédicteur Linéaire (LP) dans la population de validation cible et vous voulez une planification de précision basée sur la simulation.
* **Quand Éviter :** Distribution LP inconnue et impossible à approximer.
* **Entrées Clés :** Distribution LP (Normale/Beta/Empirique), Paramètres de mauvaise calibration, Cibles largeur IC des métriques, Répétitions, Graine
* **Sorties Clés :** $N$ minimal atteignant les objectifs de précision sous simulation
* **Pour :** Très flexible. Correspond à "simuler ce que vous attendez"
* **Contre :** Hypothèses lourdes. Coût de calcul

**D11 — Mise à jour / Recalibrage (Intercept/Pente)**
* **Quand :** Vous voulez recalibrer un modèle existant (mise à jour de l'intercept et/ou de la pente) et avez besoin d'une précision suffisante.
* **Quand Éviter :** Vous développez un modèle entièrement nouveau (utilisez C5–C7).
* **Entrées Clés :** Type de mise à jour (Intercept seul vs Intercept+Pente), Taux d'événement, Cible précision
* **Sorties Clés :** $N$ suffisant pour une mise à jour stable
* **Pour :** Pratique pour le déploiement réel
* **Contre :** Dépend des hypothèses sur le case-mix local et la transportabilité du modèle

---

#### Avis de non-responsabilité

Pas de garantie clinique. L'utilisateur est responsable de la validation et de l'interprétation. Documentez toujours vos hypothèses et exécutez des analyses de sensibilité.

#### Contact

Créé et maintenu par : Minh Nguyen (minhnt@ump.edu.vn)
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
