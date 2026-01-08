
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
    category: str # A, B, C, D
    title_en: str
    title_vi: str
    status: MethodStatus
    title_zh: str = "" # Default empty if not provided immediately, but we will provide it
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
            "A": {"en": "A. Quick Tools", "vi": "Nhanh / Cơ bản", "zh": "A. 快速工具 (Quick Tools)", "jp": "A. クイックツール (Quick Tools)", "fr": "A. Outils Rapides (Quick Tools)", "de": "A. Schnelle Tools (Quick Tools)"},
            "B": {"en": "B. Prognostic Factors", "vi": "Yếu tố Tiên lượng (Power)", "zh": "B. 预后因素 (Prognostic Factors)", "jp": "B. 予後因子 (Prognostic Factors)", "fr": "B. Facteurs Pronostiques (Power)", "de": "B. Prognosefaktoren (Power)"},
            "C": {"en": "C. Prediction Models", "vi": "Phát triển Mô hình Dự báo", "zh": "C. 预测模型 (Prediction Models)", "jp": "C. 予測モデル (Prediction Models)", "fr": "C. Modèles de Prédiction (Development)", "de": "C. Vorhersagemodelle (Entwicklung)"},
            "D": {"en": "D. Validation", "vi": "Thẩm định / Cập nhật", "zh": "D. 验证 (Validation)", "jp": "D. 検証 (Validation)", "fr": "D. Validation / Mise à Jour", "de": "D. Validierung / Aktualisierung"},
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

# A1
registry.register(MethodSpec(
    id="a1", category="A",
    title_en="A1: Rules of Thumb (EPV)", title_vi="A1: Quy tắc Ngón tay cái (EPV)", title_zh="A1: 经验法则 (EPV)", title_jp="A1: 経験則 (EPV)", title_fr="A1: Règles empiriques (EPV)", title_de="A1: Faustregeln (EPV)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a1_epv.render_ui,
    description_en="Simple Events Per Variable (EPV) rules (10, 20, etc).",
    description_vi="Cỡ mẫu dựa trên số biến cố trên mỗi biến (EPV).",
    description_zh="基于每变量事件数 (EPV) 的经验法则。",
    description_jp="単純な変数あたりのイベント数 (EPV) ルール (10, 20など)。",
    description_fr="Règles simples d'Événements Par Variable (EPV) (10, 20, etc).",
    description_de="Einfache Ereignisse-pro-Variable (EPV) Regeln (10, 20, etc)."
))

# A2
registry.register(MethodSpec(
    id="a2", category="A",
    title_en="A2: Baseline Risk Precision", title_vi="A2: Độ chính xác Tỷ lệ nền", title_zh="A2: 基线风险精度", title_jp="A2: ベースラインリスク精度", title_fr="A2: Précision du Risque de Base", title_de="A2: Basisrisiko-Präzision",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a2_precision.render_ui,
    description_en="Sample size to estimate prevalence with precision.",
    description_vi="Cỡ mẫu để ước lượng tỷ lệ hiện mắc với độ chính xác mong muốn.",
    description_zh="以期望的精度估计患病率的样本量。",
    description_jp="精度よく有病率を推定するためのサンプルサイズ。",
    description_fr="Taille d'échantillon pour estimer la prévalence avec précision.",
    description_de="Stichprobengröße zur Schätzung der Prävalenz mit Präzision."
))

# B3
registry.register(MethodSpec(
    id="b3", category="B",
    title_en="B3: Logistic OR Power (Hsieh)", title_vi="B3: Cỡ mẫu Logistic (Hsieh)", title_zh="B3: Logistic 功效 (Hsieh)", title_jp="B3: Logistic 検出力 (Hsieh)", title_fr="B3: Puissance Logistic (Hsieh)", title_de="B3: Logistische Power (Hsieh)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b3_hsieh.render_ui,
    description_en="Power calculation for logistic regression (Hsieh 1998).",
    description_vi="Tính công suất cho hồi quy logistic (Hsieh 1998).",
    description_zh="Logistic 回归的功效计算 (Hsieh 1998)。",
    description_jp="ロジスティック回帰の検出力計算 (Hsieh 1998)。",
    description_fr="Calcul de puissance pour la régression logistique (Hsieh 1998).",
    description_de="Power-Berechnung für logistische Regression (Hsieh 1998)."
))

# B4
registry.register(MethodSpec(
    id="b4", category="B",
    title_en="B4: Cox Power (Schoenfeld)", title_vi="B4: Cỡ mẫu Cox (Schoenfeld)", title_zh="B4: Cox 功效 (Schoenfeld)", title_jp="B4: Cox 検出力 (Schoenfeld)", title_fr="B4: Puissance Cox (Schoenfeld)", title_de="B4: Cox Power (Schoenfeld)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b4_schoenfeld.render_ui,
    description_en="Power calculation for Cox PH (Schoenfeld 1983).",
    description_vi="Tính công suất cho hồi quy Cox (Schoenfeld 1983).",
    description_zh="Cox 比例风险模型的功效计算 (Schoenfeld 1983)。",
    description_jp="Cox 比例ハザードの検出力計算 (Schoenfeld 1983)。",
    description_fr="Calcul de puissance pour Cox PH (Schoenfeld 1983).",
    description_de="Power-Berechnung für Cox PH (Schoenfeld 1983)."
))

# C5
registry.register(MethodSpec(
    id="c5", category="C",
    title_en="C5: Riley et al. (Analytical)", title_vi="C5: Phương pháp Riley (Giải tích)", title_zh="C5: Riley 等 (解析法)", title_jp="C5: Riley 等 (解析的)", title_fr="C5: Riley et al. (Analytique)", title_de="C5: Riley et al. (Analytisch)",
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

# C6
registry.register(MethodSpec(
    id="c6", category="C",
    title_en="C6: Development Simulation", title_vi="C6: Mô phỏng Phát triển", title_zh="C6: 开发模拟 (Simulation)", title_jp="C6: 開発シミュレーション (Simulation)", title_fr="C6: Simulation de Développement", title_de="C6: Entwicklungssimulation",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c6_dev_sim.render_ui,
    description_en="Simulation-based sizing (custom DGM).",
    description_vi="Tính cỡ mẫu bằng mô phỏng tùy chỉnh.",
    description_zh="基于模拟的样本量计算 (自定义 DGM)。",
    description_jp="シミュレーションに基づくサイズ計算 (カスタム DGM)。",
    description_fr="Dimensionnement basé sur la simulation (DGM personnalisé).",
    description_de="Simulationsbasierte Größenbestimmung (benutzerdefinierter DGM)."
))

# C7
registry.register(MethodSpec(
    id="c7", category="C",
    title_en="C7: Bayesian Assurance", title_vi="C7: Đảm bảo Bayesian", title_zh="C7: 贝叶斯保证 (Assurance)", title_jp="C7: ベイズ保証 (Assurance)", title_fr="C7: Assurance Bayesienne", title_de="C7: Bayes'sche Assurance",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c7_bayes.render_ui,
    description_en="MCMC simulation for Bayesian Assurance.",
    description_vi="Mô phỏng MCMC tính xác suất thành công (Assurance).",
    description_zh="贝叶斯保证的 MCMC 模拟。",
    description_jp="ベイズ保証のための MCMC シミュレーション。",
    description_fr="Simulation MCMC pour l'Assurance Bayesienne.",
    description_de="MCMC-Simulation für Bayes'sche Assurance."
))

# D8
registry.register(MethodSpec(
    id="d8", category="D",
    title_en="D8: AUC Precision (Hanley-McNeil)", title_vi="D8: Độ chính xác AUC (Hanley-McNeil)", title_zh="D8: AUC 精度 (Hanley-McNeil)", title_jp="D8: AUC 精度 (Hanley-McNeil)", title_fr="D8: Précision AUC (Hanley-McNeil)", title_de="D8: AUC Präzision (Hanley-McNeil)",
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

# D9
registry.register(MethodSpec(
    id="d9", category="D",
    title_en="D9: External Validation (Tailored)", title_vi="D9: Thẩm định ngoài (Tailored)", title_zh="D9: 外部验证 (Tailored)", title_jp="D9: 外部検証 (Tailored)", title_fr="D9: Validation Externe (Sur Mesure)", title_de="D9: Externe Validierung (Maßgeschneidert)",
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

# Placeholder D10-D11
# D10
registry.register(MethodSpec(
    id="d10", category="D",
    title_en="D10: Ext. Validation (Simulation)", title_vi="D10: Thẩm định ngoài (Mô phỏng)", title_zh="D10: 外部验证 (模拟)", title_jp="D10: 外部検証 (シミュレーション)", title_fr="D10: Validation Ext. (Simulation)", title_de="D10: Ext. Validierung (Simulation)",
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
registry.register(MethodSpec("d11", "D", "D11: Updating / Recalibration", "D11: Cập nhật / Hiệu chỉnh", MethodStatus.COMING_SOON, title_zh="D11: 更新 / 重新校准", title_jp="D11: 更新 / 再キャリブレーション", title_fr="D11: Mise à jour / Recalibrage", title_de="D11: Aktualisierung / Neukalibrierung"))
