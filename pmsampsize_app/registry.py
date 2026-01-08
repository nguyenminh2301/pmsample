
from dataclasses import dataclass, field
from typing import List, Dict, Callable, Optional, Any
import enum

class MethodStatus(enum.Enum):
    AVAILABLE = "available"
    COMING_SOON = "coming_soon"
    BETA = "beta"

@dataclass
class MethodSpec:
    id: str
    category: str # A, B, C
    subgroup: str # e.g. "Quick Checks"
    title_en: str
    title_vi: str
    status: MethodStatus
    title_zh: str = ""
    title_jp: str = ""
    title_fr: str = ""
    title_de: str = ""
    ref_badges: List[str] = field(default_factory=list) # e.g. ["PubMed (+1)", "CRAN"]
    description_en: str = ""
    description_vi: str = ""
    description_zh: str = ""
    description_jp: str = ""
    description_fr: str = ""
    description_de: str = ""
    # Callable that takes NO args, returns None. 
    # It should import streamlit and render the UI itself.
    render_ui_fn: Optional[Callable[[Any], None]] = None 
    formula_md_en: str = ""
    formula_md_vi: str = ""
    
class MethodRegistry:
    def __init__(self):
        self._methods: Dict[str, MethodSpec] = {}
        self._categories = {
            "A": {"en": "A. Binary Outcomes", "vi": "A. Kết cục Nhị giá", "zh": "A. 二元结果", "jp": "A. 二値アウトカム", "fr": "A. Résultats Binaires", "de": "A. Binäre Ergebnisse"},
            "B": {"en": "B. Continuous Outcomes", "vi": "B. Kết cục Liên tục", "zh": "B. 连续结果", "jp": "B. 連続アウトカム", "fr": "B. Résultats Continus", "de": "B. Kontinuierliche Ergebnisse"},
            "C": {"en": "C. Survival Outcomes", "vi": "C. Kết cục Sống còn", "zh": "C. 生存结果", "jp": "C. 生存アウトカム", "fr": "C. Résultats de Survie", "de": "C. Überlebenszeitergebnisse"},
        }
    
    def register(self, spec: MethodSpec):
        self._methods[spec.id] = spec
        
    def get_all(self):
        return list(self._methods.values())
        
    def get_by_category(self, cat: str):
        return [m for m in self._methods.values() if m.category == cat]
        
    def get_category_name(self, cat: str, lang: str):
        return self._categories.get(cat, {}).get(lang.lower(), self._categories.get(cat, {}).get("en", cat))

registry = MethodRegistry()

# Register Methods
# Delayed imports to avoid cycles if any (though wrapped nicely now)

try:
    from pmsampsize_app.methods import a1_epv, a2_precision, b3_hsieh, b4_schoenfeld, c5_riley, c6_dev_sim, c7_bayes, d8_auc_precision, d9_extval, d10_sim
except ImportError:
    # Fallback for direct execution
    from methods import a1_epv, a2_precision, b3_hsieh, b4_schoenfeld, c5_riley, c6_dev_sim, c7_bayes, d8_auc_precision, d9_extval, d10_sim

# --- A. BINARY OUTCOMES ---

# Subgroup: A1. Quick Checks
# A1 (Old A1) -> A1.1
registry.register(MethodSpec(
    id="a1_1", category="A", subgroup="A1. Quick Checks / Kiểm tra nhanh",
    title_en="A1.1: Rules of Thumb (EPV)", title_vi="A1.1: Quy tắc Ngón tay cái (EPV)", title_zh="A1.1: 经验法则 (EPV)", title_jp="A1.1: 経験則 (EPV)", title_fr="A1.1: Règles empiriques (EPV)", title_de="A1.1: Faustregeln (EPV)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a1_epv.render_ui,
    description_en="Simple Events Per Variable (EPV) rules (10, 20, etc).",
    description_vi="Cỡ mẫu dựa trên số biến cố trên mỗi biến (EPV).",
    description_zh="基于每变量事件数 (EPV) 的经验法则。",
    description_jp="単純な変数あたりのイベント数 (EPV) ルール (10, 20など)。",
    description_fr="Règles simples d'Événements Par Variable (EPV) (10, 20, etc).",
    description_de="Einfache Ereignisse-pro-Variable (EPV) Regeln (10, 20, etc)."
))

# A2 (Old A2) -> A1.2
registry.register(MethodSpec(
    id="a1_2", category="A", subgroup="A1. Quick Checks / Kiểm tra nhanh",
    title_en="A1.2: Baseline Risk Precision", title_vi="A1.2: Độ chính xác Tỷ lệ nền", title_zh="A1.2: 基线风险精度", title_jp="A1.2: ベースラインリスク精度", title_fr="A1.2: Précision du Risque de Base", title_de="A1.2: Basisrisiko-Präzision",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a2_precision.render_ui,
    description_en="Sample size to estimate prevalence with precision.",
    description_vi="Cỡ mẫu để ước lượng tỷ lệ hiện mắc với độ chính xác mong muốn.",
    description_zh="以期望的精度估计患病率的样本量。",
    description_jp="精度よく有病率を推定するためのサンプルサイズ。",
    description_fr="Taille d'échantillon pour estimer la prévalence avec précision.",
    description_de="Stichprobengröße zur Schätzung der Prävalenz mit Präzision."
))

# Subgroup: A2. Prognostic Factor (Power)
# B3 (Old B3) -> A2.1
registry.register(MethodSpec(
    id="a2_1", category="A", subgroup="A2. Prognostic Factors / Yếu tố tiên lượng",
    title_en="A2.1: Logistic Power (Hsieh)", title_vi="A2.1: Cỡ mẫu Logistic (Hsieh)", title_zh="A2.1: Logistic 功效 (Hsieh)", title_jp="A2.1: Logistic 検出力 (Hsieh)", title_fr="A2.1: Puissance Logistic (Hsieh)", title_de="A2.1: Logistische Power (Hsieh)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b3_hsieh.render_ui,
    description_en="Power calculation for logistic regression (Hsieh 1998).",
    description_vi="Tính công suất cho hồi quy logistic (Hsieh 1998).",
    description_zh="Logistic 回归的功效计算 (Hsieh 1998)。",
    description_jp="ロジスティック回帰の検出力計算 (Hsieh 1998)。",
    description_fr="Calcul de puissance pour la régression logistique (Hsieh 1998).",
    description_de="Power-Berechnung für logistische Regression (Hsieh 1998)."
))

# B4 (Old B4) -> A2.2
registry.register(MethodSpec(
    id="a2_2", category="A", subgroup="A2. Prognostic Factors / Yếu tố tiên lượng",
    title_en="A2.2: Cox Power (Schoenfeld)", title_vi="A2.2: Cỡ mẫu Cox (Schoenfeld)", title_zh="A2.2: Cox 功效 (Schoenfeld)", title_jp="A2.2: Cox 検出力 (Schoenfeld)", title_fr="A2.2: Puissance Cox (Schoenfeld)", title_de="A2.2: Cox Power (Schoenfeld)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b4_schoenfeld.render_ui,
    description_en="Power calculation for Cox PH (Schoenfeld 1983).",
    description_vi="Tính công suất cho hồi quy Cox (Schoenfeld 1983).",
    description_zh="Cox 比例风险模型的功效计算 (Schoenfeld 1983)。",
    description_jp="Cox 比例ハザードの検出力計算 (Schoenfeld 1983)。",
    description_fr="Calcul de puissance pour Cox PH (Schoenfeld 1983).",
    description_de="Power-Berechnung für Cox PH (Schoenfeld 1983)."
))

# Subgroup: A3. Model Development
# C5 (Old C5) -> A3.1
registry.register(MethodSpec(
    id="a3_1", category="A", subgroup="A3. Model Development / Phát triển mô hình",
    title_en="A3.1: Riley et al. (Analytical)", title_vi="A3.1: Phương pháp Riley (Giải tích)", title_zh="A3.1: Riley 等 (解析法)", title_jp="A3.1: Riley 等 (解析的)", title_fr="A3.1: Riley et al. (Analytique)", title_de="A3.1: Riley et al. (Analytisch)",
    status=MethodStatus.AVAILABLE,
    ref_badges=["PubMed (+2)", "R Pkg"],
    render_ui_fn=c5_riley.render_ui,
    description_en="Standard method for prediction model development (Riley 2020).",
    description_vi="Phương pháp chuẩn cho phát triển mô hình (Riley 2020).",
    description_zh="预测模型开发的标准方法 (Riley 2020)。",
    description_jp="予測モデル開発の標準的手法 (Riley 2020)。",
    description_fr="Méthode standard pour le développement de modèles (Riley 2020).",
    description_de="Standardmethode für die Entwicklung von Vorhersagemodellen (Riley 2020)."
))

# C6 (Old C6) -> A3.2
registry.register(MethodSpec(
    id="a3_2", category="A", subgroup="A3. Model Development / Phát triển mô hình",
    title_en="A3.2: Development Simulation", title_vi="A3.2: Mô phỏng Phát triển", title_zh="A3.2: 开发模拟 (Simulation)", title_jp="A3.2: 開発シミュレーション (Simulation)", title_fr="A3.2: Simulation de Développement", title_de="A3.2: Entwicklungssimulation",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c6_dev_sim.render_ui,
    description_en="Simulation-based sizing (custom DGM).",
    description_vi="Tính cỡ mẫu bằng mô phỏng tùy chỉnh.",
    description_zh="基于模拟的样本量计算 (自定义 DGM)。",
    description_jp="シミュレーションに基づくサイズ計算 (カスタム DGM)。",
    description_fr="Dimensionnement basé sur la simulation (DGM personnalisé).",
    description_de="Simulationsbasierte Größenbestimmung (benutzerdefinierter DGM)."
))

# C7 (Old C7) -> A3.3
registry.register(MethodSpec(
    id="a3_3", category="A", subgroup="A3. Model Development / Phát triển mô hình",
    title_en="A3.3: Bayesian Assurance", title_vi="A3.3: Đảm bảo Bayesian", title_zh="A3.3: 贝叶斯保证 (Assurance)", title_jp="A3.3: ベイズ保証 (Assurance)", title_fr="A3.3: Assurance Bayesienne", title_de="A3.3: Bayes'sche Assurance",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c7_bayes.render_ui,
    description_en="MCMC simulation for Bayesian Assurance.",
    description_vi="Mô phỏng MCMC tính xác suất thành công (Assurance).",
    description_zh="贝叶斯保证的 MCMC 模拟。",
    description_jp="ベイズ保証のための MCMC シミュレーション。",
    description_fr="Simulation MCMC pour l'Assurance Bayesienne.",
    description_de="MCMC-Simulation für Bayes'sche Assurance."
))

# Subgroup: A4. Validation
# D8 (Old D8) -> A4.1
registry.register(MethodSpec(
    id="a4_1", category="A", subgroup="A4. Validation / Thẩm định",
    title_en="A4.1: AUC Precision (Hanley-McNeil)", title_vi="A4.1: Độ chính xác AUC (Hanley-McNeil)", title_zh="A4.1: AUC 精度 (Hanley-McNeil)", title_jp="A4.1: AUC 精度 (Hanley-McNeil)", title_fr="A4.1: Précision AUC (Hanley-McNeil)", title_de="A4.1: AUC Präzision (Hanley-McNeil)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d8_auc_precision.render_ui,
    ref_badges=["PMC (+1)"],
    description_en="Sample size to estimate AUC with desired CI width (Hanley-McNeil 1982).",
    description_vi="Cỡ mẫu để ước lượng AUC với độ chính xác mong muốn (Hanley-McNeil 1982).",
    description_zh="以期望的 CI 宽度估计 AUC 的样本量 (Hanley-McNeil 1982)。",
    description_jp="所望の CI 幅で AUC を推定するためのサンプルサイズ (Hanley-McNeil 1982)。",
    description_fr="Taille d'échantillon pour estimer l'AUC avec précision (Hanley-McNeil 1982).",
    description_de="Stichprobengröße zur Schätzung der AUC mit gewünschter KI-Breite (Hanley-McNeil 1982)."
))

# D9 (Old D9) -> A4.2
registry.register(MethodSpec(
    id="a4_2", category="A", subgroup="A4. Validation / Thẩm định",
    title_en="A4.2: External Validation (Tailored)", title_vi="A4.2: Thẩm định ngoài (Tailored)", title_zh="A4.2: 外部验证 (Tailored)", title_jp="A4.2: 外部検証 (Tailored)", title_fr="A4.2: Validation Externe (Sur Mesure)", title_de="A4.2: Externe Validierung (Maßgeschneidert)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d9_extval.render_ui,
    ref_badges=["CRAN (+2)", "CRAN (+2)"],
    description_en="Validation sizing using Riley/Archer (pmvalsampsize) or Pavlou (sampsizeval) criteria.",
    description_vi="Cỡ mẫu thẩm định ngoài theo tiêu chuẩn Riley/Archer hoặc Pavlou.",
    description_zh="使用 Riley/Archer 或 Pavlou 标准的验证规模计算。",
    description_jp="Riley/Archer または Pavlou 基準を使用した検証サイズ計算。",
    description_fr="Dimensionnement de validation selon Riley/Archer ou Pavlou.",
    description_de="Validierungsgröße nach Riley/Archer oder Pavlou-Kriterien."
))

# D10 (Old D10) -> A4.3
registry.register(MethodSpec(
    id="a4_3", category="A", subgroup="A4. Validation / Thẩm định",
    title_en="A4.3: Ext. Validation (Simulation)", title_vi="A4.3: Thẩm định ngoài (Mô phỏng)", title_zh="A4.3: 外部验证 (模拟)", title_jp="A4.3: 外部検証 (シミュレーション)", title_fr="A4.3: Validation Ext. (Simulation)", title_de="A4.3: Ext. Validierung (Simulation)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d10_sim.render_ui,
    ref_badges=["PubMed"],
    description_en="Simulation-based validation sizing (Snell et al. 2021).",
    description_vi="Tính cỡ mẫu thẩm định bằng mô phỏng (Snell et al. 2021).",
    description_zh="基于模拟的验证规模计算 (Snell et al. 2021)。",
    description_jp="シミュレーションに基づく検証サイズ計算 (Snell et al. 2021)。",
    description_fr="Dimensionnement de validation basé sur la simulation (Snell et al. 2021).",
    description_de="Simulationsbasierte Validierungsgröße (Snell et al. 2021)."
))

# --- B. CONTINUOUS OUTCOMES ---
registry.register(MethodSpec("b1", "B", "B1. Quick Checks", "B1: Green's Rule", "B1: Quy tắc Green", MethodStatus.COMING_SOON, title_zh="B1: Green 规则", title_jp="B1: Green のルール", title_fr="B1: Règle de Green", title_de="B1: Green's Regel"))
registry.register(MethodSpec("b2", "B", "B2. Model Development", "B2: Riley et al. (Continuous)", "B2: Riley et al. (Liên tục)", MethodStatus.COMING_SOON, title_zh="B2: Riley 等 (连续)", title_jp="B2: Riley 等 (連続)", title_fr="B2: Riley et al. (Continu)", title_de="B2: Riley et al. (Kontinuierlich)"))

# --- C. SURVIVAL OUTCOMES ---
registry.register(MethodSpec("c1", "C", "C1. Model Development", "C1: Riley et al. (Survival)", "C1: Riley et al. (Sống còn)", MethodStatus.COMING_SOON, title_zh="C1: Riley 等 (生存)", title_jp="C1: Riley 等 (生存)", title_fr="C1: Riley et al. (Survie)", title_de="C1: Riley et al. (Überlebenszeit)"))
