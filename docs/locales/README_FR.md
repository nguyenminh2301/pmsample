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

L'application est désormais structurée hiérarchiquement (Catégorie A: Résultats Binaires).

### A. Résultats Binaires (Binary Outcomes)

#### A1. Vérifications Rapides (Quick Checks)

| Méthode | Description | Objectif |
| :--- | :--- | :--- |
| **A1.1: Événements par Variable (EPV)** | Règle empirique. | Vérification de faisabilité. |
| **A1.2: Précision du Risque de Base** | Estimation de la prévalence avec largeur IC. | Épidémiologie descriptive. |

#### A2. Facteurs Pronostiques (Prognostic Factors)

| Méthode | Description | Objectif |
| :--- | :--- | :--- |
| **A2.1: Puissance Logistique (Hsieh)** | Puissance pour détecter un Odds Ratio (OR). | Études d'association. |
| **A2.2: Puissance Cox (Schoenfeld)** | Puissance pour détecter un Hazard Ratio (HR). | Analyse de survie. |

#### A3. Développement de Modèles (Model Development)

| Méthode | Description | Objectif |
| :--- | :--- | :--- |
| **A3.1: Approche Analytique (Riley)** | **Recommandé.** Ajustement pour rétrécissement, optimisme et précision. | Nouveau développement. |
| **A3.2: Conception Simulée** | Simulation de DGM spécifiques pour scénarios complexes. | Développement (Complexe). |
| **A3.3: Assurance Bayesienne** | Simulation MCMC pour probabilité de succès garantie. | Développement Bayésien. |

#### A4. Validation / Mise à jour (Validation / Updating)

| Méthode | Description | Objectif |
| :--- | :--- | :--- |
| **A4.1: Précision AUC** | Largeur IC pour l'AUC (C-statistic). | Validation (Discrimination). |
| **A4.2: Validation Externe** | Précision pour O/E, pente d'étalonnage et AUC. | Validation (Complète). |
| **A4.3: Simulation de Validation** | Simulation basée sur distribution LP. | Validation (Simulation). |
| **A4.4: Mise à jour de Modèle** | Taille d'échantillon pour recalibrage (Intercept/Pente). | Mise à jour de modèles. |

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

## 5. Citation

Si vous utilisez cet outil dans vos recherches, veuillez le citer comme suit :

> Nguyen, M. (2025). Prognostic Research Sample Size Tool (Version 1.0) [Software]. Available at https://pmsample.streamlit.app/

Ou utilisez l'entrée BibTeX :

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

**Auteur & Maintenance:**
Minh Nguyen (minhnt@ump.edu.vn)
Department of Epidemiology, Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City, Vietnam
(Bộ môn Dịch tễ học, Khoa Y tế công cộng, Đại học Y Dược TP. Hồ Chí Minh, Việt Nam)
