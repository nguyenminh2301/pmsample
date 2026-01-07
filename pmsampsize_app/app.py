import streamlit as st
import pandas as pd
import numpy as np
import time
import json
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
    # Retrieve theme from session state or default
    theme = st.session_state.get("theme", "Light")
    
    css = ""
    if theme == "Dark":
        # Streamlit handles Dark mode mostly natively if configured, but we can force some css
        css = """
        <style>
        .stApp { background-color: #0e1117; color: #fafafa; }
        </style>
        """
    elif theme == "Coder":
        css = """
        <style>
        .stApp { background-color: #1e1e1e; color: #d4d4d4; font-family: 'Courier New', monospace; }
        .stButton>button { color: #d4d4d4; border-color: #444; }
        </style>
        """
    else: # Light
        css = """
        <style>
        .stApp { background-color: #ffffff; color: #000000; }
        </style>
        """
    
    st.markdown(css, unsafe_allow_html=True)

# --- UI COMPONENTS ---

def render_sidebar(lang):
    """Renders the Tree Navigation and Settings."""
    T = TRANS.get(lang, TRANS["EN"])
    st.sidebar.title(T["title"])
    
    # 1. Search
    search_query = st.sidebar.text_input(T["search_placeholder"], "")
    
    # 2. Tree Navigation
    st.sidebar.markdown("### Method Catalog")
    
    # "Introduction" is effectively the home page
    if st.sidebar.button("🏠 " + ("Giới thiệu" if lang=="VI" else "Introduction"), use_container_width=True):
        st.session_state["selected_method"] = "intro"

    # Categories
    categories = ["A", "B", "C", "D"]
    methods = registry.get_all()
    
    for cat in categories:
        cat_name = registry.get_category_name(cat, lang)
        # Filter methods in this category
        cat_methods = [m for m in methods if m.category == cat]
        
        # Apply Search Filter
        if search_query:
            cat_methods = [m for m in cat_methods if search_query.lower() in (m.title_en + m.title_vi).lower()]
            if not cat_methods:
                continue # Skip empty categories during search
        
        with st.sidebar.expander(cat_name, expanded=(search_query!="")):
            for m in cat_methods:
                title = m.title_vi if lang == "VI" else m.title_en
                icon = "✨" if m.status == MethodStatus.AVAILABLE else "🚧"
                if m.status == MethodStatus.BETA: icon = "🧪"
                
                # Button for each method
                if st.button(f"{icon} {title}", key=f"nav_{m.id}", use_container_width=True):
                    st.session_state["selected_method"] = m.id

    st.sidebar.divider()
    
    # 3. Settings
    st.sidebar.markdown("### Settings")
    
    # Language
    lang_idx = 0
    if lang == "VI": lang_idx = 1
    elif lang == "KO": lang_idx = 2
    
    new_lang = st.sidebar.selectbox("Language / Ngôn ngữ", ["English (EN)", "Tiếng Việt (VI)", "한국어 (KO)", "中文 (ZH)", "日本語 (JP)"], index=lang_idx)
    
    if "English" in new_lang: selected_lang = "EN"
    elif "Tiếng Việt" in new_lang: selected_lang = "VI"
    elif "한국어" in new_lang: selected_lang = "KO"
    else:
        st.sidebar.info("Coming soon / Sắp ra mắt")
        selected_lang = lang # Keep current
        
    if selected_lang != st.session_state.get("lang", "EN"):
        st.session_state["lang"] = selected_lang
        st.rerun()

    # Theme
    current_theme = st.session_state.get("theme", "Light")
    theme_opts = ["Light", "Dark", "Coder"]
    try:
        idx = theme_opts.index(current_theme)
    except: idx = 0
    new_theme = st.sidebar.selectbox("Theme", theme_opts, index=idx)
    if new_theme != current_theme:
        st.session_state["theme"] = new_theme
        st.rerun()



def render_intro_page(lang):
    """Renders the Introduction / Dashboard page."""
    T = TRANS.get(lang, TRANS["EN"]) # Fallback
    
    st.title(T["title"])
    
    # Render detailed markdown content
    st.markdown(T.get("intro_complete_md", "Introduction content missing."))
    
    st.info("👈 Select a method from the sidebar to begin.")


def render_method_page(method_id, lang):
    """Renders a specific method page."""
    # Find method
    m = registry._methods.get(method_id)
    if not m:
        st.error("Method not found.")
        return
        
    T = TRANS.get(lang, TRANS["EN"])
    
    # Title
    title = m.title_vi if lang == "VI" else m.title_en
    st.title(title)
        
    # Tags / Badges
    # cols = st.columns([0.8, 0.2])
    # with cols[1]:
    #     for tag in m.ref_badges:
    #         st.caption(f"🏷️ {tag}")

    # Description
    desc = m.description_vi if lang == "VI" else m.description_en
    st.markdown(f"_{desc}_")
    
    st.divider()
    
    if m.status != MethodStatus.AVAILABLE and m.status != MethodStatus.BETA:
        st.warning(f"🚧 {T.get('future_methods', 'Coming soon...')}")
        st.info("This method is planned for future updates.")
        return

    # Render Method UI (Delegate)
    if m.render_ui_fn:
        m.render_ui_fn(T)
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
    if "selected_method" not in st.session_state: st.session_state["selected_method"] = "intro"
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
    else:
        render_method_page(method_id, lang)

if __name__ == "__main__":
    main()
