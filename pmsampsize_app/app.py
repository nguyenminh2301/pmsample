import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import os
import matplotlib.pyplot as plt

# Import internal modules (with fallback for direct execution)

try:
    from pmsampsize_app.registry import registry, MethodStatus
    from pmsampsize_app.utils.i18n import TRANS
except ImportError:
    from registry import registry, MethodStatus
    from utils.i18n import TRANS

# Page Config
st.set_page_config(
    page_title="Prognostic Research Sample Size Tool",
    page_icon="🧬",
    layout="wide"
)

# --- THEME MANAGEMENT ---
def apply_theme():
    # GitHub Dark Theme - Comprehensive Coverage
    css = """
    <style>
    /* Base Application */
    .stApp { 
        background-color: #0d1117 !important; 
        color: #c9d1d9 !important; 
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #c9d1d9 !important;
    }
    
    /* Text Elements */
    p, li, span, label, div {
        color: #c9d1d9 !important;
    }
    
    /* Secondary Text */
    .stMarkdown p, .stMarkdown li {
        color: #8b949e !important;
    }
    
    /* Links */
    a {
        color: #58a6ff !important;
    }
    a:hover {
        color: #79c0ff !important;
    }
    
    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
    }
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] span {
        color: #c9d1d9 !important;
    }
    
    /* Input Fields */
    div[data-baseweb="input"] > div {
        background-color: #0d1117 !important;
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    
    input, textarea {
        color: #c9d1d9 !important;
        background-color: #0d1117 !important;
    }
    
    /* Select Boxes */
    div[data-baseweb="select"] > div {
        background-color: #0d1117 !important;
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    
    /* Text Areas */
    .stTextArea textarea {
        color: #c9d1d9 !important;
        background-color: #0d1117 !important;
        border-color: #30363d !important;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #238636 !important;
        color: #ffffff !important;
        border: 1px solid #30363d !important;
    }
    .stButton > button:hover {
        background-color: #2ea043 !important;
    }
    
    /* Info/Warning/Success/Error Boxes */
    .stAlert {
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    
    /* DataFrames and Tables */
    .stDataFrame {
        border: 1px solid #30363d;
    }
    .stDataFrame table {
        color: #c9d1d9 !important;
    }
    .stDataFrame th {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    .stDataFrame td {
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    
    /* Metrics */
    .stMetric {
        color: #c9d1d9 !important;
    }
    .stMetricLabel {
        color: #8b949e !important;
    }
    .stMetricValue {
        color: #c9d1d9 !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border-color: #30363d !important;
    }
    
    /* Radio Buttons and Checkboxes */
    .stRadio label, .stCheckbox label {
        color: #c9d1d9 !important;
    }
    
    /* Number Input */
    .stNumberInput label {
        color: #c9d1d9 !important;
    }
    
    /* Markdown */
    .stMarkdown {
        color: #c9d1d9 !important;
    }
    
    /* Code Blocks */
    code {
        color: #79c0ff !important;
        background-color: #161b22 !important;
    }
    
    /* Divider */
    hr {
        border-color: #30363d !important;
    }
    
    /* Header/Toolbar */
    header[data-testid="stHeader"] {
        background-color: #161b22 !important;
    }
    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# --- UI COMPONENTS ---

def render_sidebar(lang):
    """Renders the Tree Navigation and Settings."""
    
    # 0. Logo
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "assets", "logo.png")
        if os.path.exists(logo_path):
            # Center logo using columns
            _, col2, _ = st.sidebar.columns([3, 2, 3])
            with col2:
                st.image(logo_path, width=50)
    except Exception:
        pass
        
    # 1. Language Selector (Moved from bottom)
    from utils.locales.en import EN
    from utils.locales.vi import VI
    from utils.locales.zh import ZH
    from utils.locales.jp import JP
    from utils.locales.fr import FR
    from utils.locales.de import DE
    from utils.locales.ko import KO
    locales = {"EN": EN, "VI": VI, "ZH": ZH, "JP": JP, "FR": FR, "DE": DE, "KO": KO}
    
    # We need a temporary T_loc here for the label 'Language'
    T_loc = locales.get(lang, EN)
    
    lang_idx = 0
    if lang == "VI": lang_idx = 1
    elif lang == "KO": lang_idx = 2
    elif lang == "ZH": lang_idx = 3
    elif lang == "JP": lang_idx = 4
    elif lang == "FR": lang_idx = 5
    elif lang == "DE": lang_idx = 6
    
    new_lang = st.sidebar.selectbox(
        T_loc.get('language', "Language"), 
        ["English (EN)", "Tiếng Việt (VI)", "한국어 (KO)", "中文 (ZH)", "日本語 (JP)", "Français (FR)", "Deutsch (DE)"], 
        index=lang_idx
    )
    
    if "English" in new_lang: selected_lang = "EN"
    elif "Tiếng Việt" in new_lang: selected_lang = "VI"
    elif "한국어" in new_lang: selected_lang = "KO"
    elif "中文" in new_lang: selected_lang = "ZH"
    elif "日本語" in new_lang: selected_lang = "JP"
    elif "Français" in new_lang: selected_lang = "FR"
    elif "Deutsch" in new_lang: selected_lang = "DE"
    else: selected_lang = lang
        
    if selected_lang != st.session_state.get("lang", "EN"):
        st.session_state["lang"] = selected_lang
        st.rerun()

    st.sidebar.divider()

    T = TRANS.get(lang, TRANS["EN"])
    st.sidebar.title(T["title"])
    
    # 1. Search
    search_query = st.sidebar.text_input(T["search_placeholder"], "")
    
    # 2. Tree Navigation
    st.sidebar.markdown("### " + T.get("nav_title", "Method Catalog")) # Use T["nav_title"] here
    
    # "Introduction" is effectively the home page
    # User requested to default to README and hide Introduction (or make it secondary)
    # Replaced Intro with README in prominence
    
    if st.sidebar.button("📄 " + T.get("nav_readme", "Detailed Documentation (README)"), use_container_width=True):
        st.session_state["selected_method"] = "readme"

    # Hidden or moved Intro
    # if st.sidebar.button("🏠 " + T.get("nav_intro", "Introduction"), use_container_width=True):
    #     st.session_state["selected_method"] = "intro"

    # Categories
    categories = ["A", "B", "C"]
    methods = registry.get_all()
    
    for cat in categories:
        cat_name = registry.get_category_name(cat, lang)
        
        # Filter methods in this category
        cat_methods = [m for m in methods if m.category == cat]
        
        # Apply Search Filter (if query exists)
        if search_query:
            cat_methods = [m for m in cat_methods if search_query.lower() in (m.title_en + m.title_vi + m.title_zh + m.title_jp + m.title_fr + m.title_de).lower()]
            if not cat_methods:
                continue # Skip empty categories during search (unless we want to show headers?)
        
        # Sort methods by ID to ensure A1.1 comes before A1.2
        cat_methods.sort(key=lambda x: x.id)

        # Show Category Expander
        # Force expand if searching, or if it's the A category (default focus)
        is_expanded = (search_query != "") or (cat == "A")
        
        with st.sidebar.expander(cat_name, expanded=is_expanded):
            # Group by Subgroup
            # We use a dictionary to group
            grouped = {}
            for m in cat_methods:
                # Use getattr to avoid AttributeError if registry is stale
                val = getattr(m, "subgroup", None)
                sg = val if val else "Other"
                
                if sg not in grouped: grouped[sg] = []
                grouped[sg].append(m)
            
            # Sort subgroups? A1..., A2... - They should naturally sort if we keyed them well
            # But dict order isn't guaranteed in all py versions (though 3.7+ yes).
            # Let's simple sort keys
            sorted_sgs = sorted(grouped.keys())
            
            for sg in sorted_sgs:
                # Render Subgroup Header if distinct and not "Other"
                if sg != "Other":
                    # Translate Subgroup
                    # registry now stores keys like 'sg_a1' in .subgroup
                    # T is generic, we need T dict from arguments... wait, render_sidebar gets 'lang' but not 'T' directly?
                    # We need to import the locale dicts or use a helper. 
                    # app.py usually gets T at the start of main, but render_sidebar receives just 'lang'.
                    # We need to look up the translation.
                    from utils.locales.en import EN
                    from utils.locales.vi import VI
                    from utils.locales.zh import ZH
                    from utils.locales.jp import JP
                    from utils.locales.fr import FR
                    from utils.locales.de import DE
                    from utils.locales.ko import KO
                    
                    locales = {"EN": EN, "VI": VI, "ZH": ZH, "JP": JP, "FR": FR, "DE": DE, "KO": KO}
                    T_loc = locales.get(lang, EN)
                    
                    sg_label = T_loc.get(sg, sg) # Fallback to key if not found
                    st.markdown(f"**{sg_label}**")
                
                for m in grouped[sg]:
                    title = m.title_en
                    if lang == "VI": title = m.title_vi
                    elif lang == "ZH": title = m.title_zh
                    elif lang == "JP": title = m.title_jp
                    elif lang == "FR": title = m.title_fr
                    elif lang == "DE": title = m.title_de
                    elif lang == "KO": title = getattr(m, "title_ko", m.title_en) # generic fallback
                    
                    # Fallback if specific lang title is missing
                    if not title: title = m.title_en
                    
                    icon = "✨" if m.status == MethodStatus.AVAILABLE else "🚧"
                    if m.status == MethodStatus.BETA: icon = "🧪"
                    if m.status == MethodStatus.COMING_SOON: icon = "⏳"
                    
                    # Button for each method
                    btn_label = f"{icon} {title}"
                    if m.id == st.session_state.get("selected_method"):
                        btn_label = f"👉 {btn_label}"
                        
                    if st.button(btn_label, key=f"nav_{m.id}", use_container_width=True):
                        st.session_state["selected_method"] = m.id

    st.sidebar.divider()
    
    # Settings (Language moved to top)







def render_intro_page(lang):
    """Renders the Introduction / Dashboard page."""
    T = TRANS.get(lang, TRANS["EN"]) # Fallback
    
    st.title(T["title"])
    
    # Render detailed markdown content
    st.markdown(T.get("intro_complete_md", "Introduction content missing."))
    
    st.info("👈 Select a method from the sidebar to begin.")


def render_readme_page(lang):
    """Renders the README.md file as the documentation page."""
    
    # Determine file path based on language
    # Assuming app.py is in pmsampsize_app/
    # And README files are in root/
    
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    
    filename = "README.md"
    if lang == "VI":
        filename = os.path.join("docs", "locales", "README_VI.md")
    elif lang == "KO":
        filename = os.path.join("docs", "locales", "README_KO.md")
    elif lang == "ZH":
        filename = os.path.join("docs", "locales", "README_ZH.md")
    elif lang == "JP":
        filename = os.path.join("docs", "locales", "README_JP.md")
    elif lang == "FR":
        filename = os.path.join("docs", "locales", "README_FR.md")
    elif lang == "DE":
        filename = os.path.join("docs", "locales", "README_DE.md")
        
    file_path = os.path.join(root_dir, filename)
    
    # Fallback to English if specific lang file doesn't exist
    if not os.path.exists(file_path):
        file_path = os.path.join(root_dir, "README.md")
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            st.markdown(content)
    except Exception as e:
        st.error(f"Error loading documentation: {e}")
        st.info(f"Looking for: {file_path}")


def render_method_page(method_id, lang):
    """Renders a specific method page."""
    # Find method
    m = registry._methods.get(method_id)
    if not m:
        st.error("Method not found.")
        return
        
    T = TRANS.get(lang, TRANS["EN"])
    
    # Title
    # Title
    title = m.title_en
    if lang == "VI": title = m.title_vi
    elif lang == "ZH": title = m.title_zh
    elif lang == "JP": title = m.title_jp
    elif lang == "FR": title = m.title_fr
    elif lang == "DE": title = m.title_de
    st.title(title)
        
    # Tags / Badges
    # cols = st.columns([0.8, 0.2])
    # with cols[1]:
    #     for tag in m.ref_badges:
    #         st.caption(f"🏷️ {tag}")

    # Description
    # Description
    desc = m.description_en
    if lang == "VI": desc = m.description_vi
    elif lang == "ZH": desc = m.description_zh
    elif lang == "JP": desc = m.description_jp
    elif lang == "FR": desc = m.description_fr
    elif lang == "DE": desc = m.description_de
    st.markdown(f"_{desc}_")
    
    st.divider()
    
    if m.status != MethodStatus.AVAILABLE and m.status != MethodStatus.BETA:
        st.warning(f"🚧 {T.get('future_methods', 'Coming soon...')}")
        st.info("This method is planned for future updates.")
        return

    # Render Method UI (Delegate)
    # Render Method UI (Delegate)
    if m.render_ui_fn:
        m.render_ui_fn(T)
    elif m.status == MethodStatus.COMING_SOON:
        st.info(f"⏳ {T.get('future_methods', 'Coming soon...')}")
    else:
        st.error("UI Module not linked.")
        
    # Footer Area (Formulas & Refs)
    st.markdown("---")
    # with st.expander("📚 Formulas & technical details / Công thức"):
    #     st.markdown("### Formulas")
    #     # Placeholder for specific formulas if not in the module itself
    #     st.markdown("_See technical documentation in the About page or method description._")
        
    #     st.markdown("### References")
    #     st.markdown("*   Riley RD et al. ...")
    #     st.markdown("*   Hsieh FY et al. ...")

    # render_footer(T) # Can be redundant if sidepanel has info


def main():
    # Initialize Session State
    if "lang" not in st.session_state: st.session_state["lang"] = "EN"
    if "selected_method" not in st.session_state: st.session_state["selected_method"] = "readme" # Default to README
    if "theme" not in st.session_state: st.session_state["theme"] = "Coder"
    
    # Apply Theme
    apply_theme()
    
    # Lang
    lang = st.session_state["lang"]
    
    # Sidebar
    render_sidebar(lang)
    
    # Main Content
    method_id = st.session_state["selected_method"]
    
    if method_id == "intro":
        render_intro_page(lang)
    elif method_id == "readme":
        render_readme_page(lang)
    else:
        render_method_page(method_id, lang)

if __name__ == "__main__":
    main()
