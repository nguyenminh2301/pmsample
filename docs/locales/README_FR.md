# Estimation de la Taille d'Échantillon pour la Recherche Pronostique

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pmsample.streamlit.app/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Une boîte à outils conçue pour calculer les tailles d'échantillon minimales dans la recherche pronostique clinique. Développée pour les data scientists, les statisticiens et les chercheurs cliniques, cette application met en œuvre des méthodes statistiques validées pour le **Développement de Modèles de Prédiction**, la **Validation Externe**, les **Études de Facteurs Pronostiques** et la **Mise à jour de Modèles**.

🔗 **Accéder à l'application:** [https://pmsample.streamlit.app/](https://pmsample.streamlit.app/)

> **Note**: Le contenu en chinois, japonais, français et allemand de cette application a été partiellement traduit par IA. Pour toute question, veuillez contacter l'administrateur de l'application.

---

## 1. Aperçu et Objectif

Cette application fournit une suite d'outils pour répondre aux exigences complexes de la planification de la taille de l'échantillon dans la recherche médicale. Contrairement aux calculateurs de puissance de base, cet outil se concentre sur les nuances spécifiques de la *modélisation pronostique*, où l'objectif est souvent une estimation précise du risque (étalonnage et discrimination) plutôt qu'un simple test d'hypothèse.

### Fonctionnalités Clés

* **Rigueur Méthodologique**: Met en œuvre des algorithmes strictement conformes à la littérature statistique évaluée par des pairs (Riley et al., Hanley & McNeil, Hsieh, et al.).
* **Validation**: Les calculs de base ont été vérifiés par rapport à des packages R réputés (`pmsampsize`, `presize`, `pmvalsampsize`, `sampsizeval`) pour garantir l'exactitude.
* **Support Multilingue**: Support complet de l'anglais et du vietnamien, et support partiel du chinois, japonais, français et allemand, facilitant la collaboration internationale.
* **Analyse de Sensibilité**: Le traitement par lots intégré permet aux chercheurs d'évaluer comment les exigences de taille d'échantillon varient selon une gamme d'hypothèses (par exemple, variation de la prévalence ou du $R^2$ anticipé).

---

## 2. Catalogue de Méthodes

L'application est structurée en quatre modules principaux, chacun ciblant une phase spécifique du cycle de recherche.

### A. Évaluation Préliminaire de Faisabilité

| Méthode | Description | Scénarios d'Application |
| :--- | :--- | :--- |
| **A1: Événements par Variable (EPV/EPP)** | Règle empirique basée sur le ratio événements/paramètres prédictifs. | *Vérification de faisabilité uniquement.* **Non recommandé comme justification principale** pour un protocole car ne tient pas compte du surajustement ou de l'étalonnage. |
| **A2: Précision du Risque de Base** | Estime la taille d'échantillon nécessaire pour estimer la prévalence avec une largeur d'Intervalle de Confiance (IC) spécifiée. | Épidémiologie descriptive; planification de l'étalonnage global (calibration-in-the-large). |

### B. Études de Facteurs Pronostiques (Association)

| Méthode | Description | Référence |
| :--- | :--- | :--- |
| **B3: Puissance Régression Logistique** | Calcule la taille d'échantillon pour détecter un Odds Ratio (OR) cible pour un prédicteur, en ajustant pour la covariance avec d'autres facteurs. | **Hsieh et al. (1998)** |
| **B4: Puissance Régression Cox** | Calcule le nombre d'événements requis pour détecter un Hazard Ratio (HR) cible dans l'analyse de survie. | **Schoenfeld (1983)** |

### C. Développement de Modèle de Prédiction (Recommandé)

C'est le module central pour construire de nouveaux modèles de prédiction clinique.

| Méthode | Description | Objectifs Clés |
| :--- | :--- | :--- |
| **C5: Approche Analytique (Riley)** | **Le Gold Standard.** Solution fermée pour le développement de modèles multivariés. | 1. Limiter le rétrécissement global (shrinkage $S \ge 0.9$).<br />2. Limiter l'optimisme dans la performance apparente.<br />3. Estimation précise de l'intercept. |
| **C6: Conception basée sur la Simulation** | Simule des Mécanismes de Génération de Données (DGM) spécifiques pour estimer les exigences des modèles complexes. | Termes non linéaires, interactions complexes, structures de corrélation spécifiques. |
| **C7: Assurance Bayesienne** | Simulation basée sur MCMC pour déterminer la taille d'échantillon avec une probabilité de succès garantie (Assurance). | Développement de modèles Bayésiens. |

### D. Validation et Mise à jour

Outils pour planifier la validation externe de modèles existants.

| Méthode | Description | Référence |
| :--- | :--- | :--- |
| **D8: Précision AUC** | Calcule N pour atteindre une largeur d'intervalle de confiance spécifique pour l'AUC (C-statistic). | **Hanley & McNeil (1982)** |
| **D9: Taille de Validation Sur Mesure** | Calcule N pour assurer une estimation précise du ratio O/E, de la Pente d'Étalonnage et de l'AUC. | **Riley et al. (2021)** / `pmvalsampsize` |
| **D10: Simulation de Validation** | Planification basée sur la simulation utilisant la distribution du Prédicteur Linéaire (LP). | **Snell et al. (2021)** |
| **D11: Mise à jour de Modèle** | Taille d'échantillon requise pour mettre à jour (recalibrer) un modèle existant (Intercept/Pente) pour un nouveau cadre. | **Van Calster et al.** |

---

## 3. Installation et Exécution Locale

Pour déployer cette application sur votre propre infrastructure :

### Prérequis

* Python 3.9 ou supérieur
* Git

### Étapes de Déploiement

1. **Cloner le Dépôt (Clone)**

   ```bash
   git clone https://github.com/nguyenminh2301/pmsample.git
   cd pmsample
   ```

2. **Configuration de l'Environnement**
   Il est fortement recommandé d'utiliser un environnement virtuel.

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. **Installer les Dépendances**

   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer l'Application**

   ```bash
   streamlit run pmsampsize_app/app.py
   ```

---

## 4. Avis de Non-responsabilité

**Pour Usage Académique et de Recherche Uniquement.**

Ce logiciel est une implémentation de méthodes statistiques publiées dans la littérature évaluée par des pairs. Bien que tous les efforts aient été faits pour assurer l'exactitude des algorithmes, les auteurs et mainteneurs n'assument aucune responsabilité quant à la conception ou aux résultats de toute étude basée sur cet outil.

* **Responsabilité de l'Utilisateur**: Les utilisateurs sont responsables de la vérification des paramètres d'entrée et de l'interprétation des résultats dans le contexte de leur domaine clinique spécifique.
* **Aucune Garantie Médicale**: Cet outil ne fournit pas de conseils médicaux.

---

**Auteur & Maintenance:**
Minh Nguyen (minhnt@ump.edu.vn)
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
(Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam)
