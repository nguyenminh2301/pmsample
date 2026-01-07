
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
    ref_badges: List[str] = field(default_factory=list) # e.g. ["PubMed (+1)", "CRAN"]
    description_en: str = ""
    description_vi: str = ""
    # Callable that takes NO args, returns None. 
    # It should import streamlit and render the UI itself.
    render_ui_fn: Optional[Callable[[Any], None]] = None 
    formula_md_en: str = ""
    formula_md_vi: str = ""
    
class MethodRegistry:
    def __init__(self):
        self._methods: Dict[str, MethodSpec] = {}
        self._categories = {
            "A": {"en": "A. Quick Tools", "vi": "Nhanh / Cơ bản"},
            "B": {"en": "B. Prognostic Factors", "vi": "Yếu tố Tiên lượng (Power)"},
            "C": {"en": "C. Prediction Models", "vi": "Phát triển Mô hình Dự báo"},
            "D": {"en": "D. Validation", "vi": "Thẩm định / Cập nhật"},
        }

    def register(self, spec: MethodSpec):
        self._methods[spec.id] = spec
        
    def get_all(self):
        return list(self._methods.values())
        
    def get_by_category(self, cat: str):
        return [m for m in self._methods.values() if m.category == cat]
        
    def get_category_name(self, cat: str, lang: str):
        return self._categories.get(cat, {}).get(lang.lower(), cat)

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
    title_en="A1: Rules of Thumb (EPV)", title_vi="A1: Quy tắc Ngón tay cái (EPV)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a1_epv.render_ui,
    description_en="Simple Events Per Variable (EPV) rules (10, 20, etc).",
    description_vi="Cỡ mẫu dựa trên số biến cố trên mỗi biến (EPV)."
))

# A2
registry.register(MethodSpec(
    id="a2", category="A",
    title_en="A2: Baseline Risk Precision", title_vi="A2: Độ chính xác Tỷ lệ nền",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=a2_precision.render_ui,
    description_en="Sample size to estimate prevalence with precision.",
    description_vi="Cỡ mẫu để ước lượng tỷ lệ hiện mắc với độ chính xác mong muốn."
))

# B3
registry.register(MethodSpec(
    id="b3", category="B",
    title_en="B3: Logistic OR Power (Hsieh)", title_vi="B3: Cỡ mẫu Logistic (Hsieh)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b3_hsieh.render_ui,
    description_en="Power calculation for logistic regression (Hsieh 1998).",
    description_vi="Tính công suất cho hồi quy logistic (Hsieh 1998)."
))

# B4
registry.register(MethodSpec(
    id="b4", category="B",
    title_en="B4: Cox Power (Schoenfeld)", title_vi="B4: Cỡ mẫu Cox (Schoenfeld)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=b4_schoenfeld.render_ui,
    description_en="Power calculation for Cox PH (Schoenfeld 1983).",
    description_vi="Tính công suất cho hồi quy Cox (Schoenfeld 1983)."
))

# C5
registry.register(MethodSpec(
    id="c5", category="C",
    title_en="C5: Riley et al. (Analytical)", title_vi="C5: Phương pháp Riley (Giải tích)",
    status=MethodStatus.AVAILABLE,
    ref_badges=["PubMed (+2)", "R Pkg"],
    render_ui_fn=c5_riley.render_ui,
    description_en="Standard method for prediction model development (Riley 2020).",
    description_vi="Phương pháp chuẩn cho phát triển mô hình (Riley 2020)."
))

# C6
registry.register(MethodSpec(
    id="c6", category="C",
    title_en="C6: Development Simulation", title_vi="C6: Mô phỏng Phát triển",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c6_dev_sim.render_ui,
    description_en="Simulation-based sizing (custom DGM).",
    description_vi="Tính cỡ mẫu bằng mô phỏng tùy chỉnh."
))

# C7
registry.register(MethodSpec(
    id="c7", category="C",
    title_en="C7: Bayesian Assurance", title_vi="C7: Đảm bảo Bayesian",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=c7_bayes.render_ui,
    description_en="MCMC simulation for Bayesian Assurance.",
    description_vi="Mô phỏng MCMC tính xác suất thành công (Assurance)."
))

# D8
registry.register(MethodSpec(
    id="d8", category="D",
    title_en="D8: AUC Precision (Hanley-McNeil)", title_vi="D8: Độ chính xác AUC (Hanley-McNeil)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d8_auc_precision.render_ui,
    ref_badges=["PMC (+1)"],
    description_en="Sample size to estimate AUC with desired CI width (Hanley-McNeil 1982).",
    description_vi="Cỡ mẫu để ước lượng AUC với độ chính xác mong muốn (Hanley-McNeil 1982)."
))

# D9
registry.register(MethodSpec(
    id="d9", category="D",
    title_en="D9: External Validation (Tailored)", title_vi="D9: Thẩm định ngoài (Tailored)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d9_extval.render_ui,
    ref_badges=["CRAN (+2)", "CRAN (+2)"],
    description_en="Validation sizing using Riley/Archer (pmvalsampsize) or Pavlou (sampsizeval) criteria.",
    description_vi="Cỡ mẫu thẩm định ngoài theo tiêu chuẩn Riley/Archer hoặc Pavlou."
))

# Placeholder D10-D11
# D10
registry.register(MethodSpec(
    id="d10", category="D",
    title_en="D10: Ext. Validation (Simulation)", title_vi="D10: Thẩm định ngoài (Mô phỏng)",
    status=MethodStatus.AVAILABLE,
    render_ui_fn=d10_sim.render_ui,
    ref_badges=["PubMed"],
    description_en="Simulation-based validation sizing (Snell et al. 2021).",
    description_vi="Tính cỡ mẫu thẩm định bằng mô phỏng (Snell et al. 2021)."
))
registry.register(MethodSpec("d11", "D", "D11: Updating / Recalibration", "D11: Cập nhật / Hiệu chỉnh", MethodStatus.COMING_SOON))
