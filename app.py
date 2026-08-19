# toolboss/app.py

import streamlit as st

st.set_page_config(
    page_title="ToolBoss",
    page_icon="🛠️",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🛠️ ToolBoss")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard",
        "LEXA AI",
        "Meeting Summarizer",
        "About"
    ]
)

# ---------------- ROUTING ---------------- #

if page == "Dashboard":
    from app_pages.dashboard import show_dashboard
    show_dashboard()

elif page == "LEXA AI":
    from app_pages.lexa_page import show_lexa
    show_lexa()

elif page == "Meeting Summarizer":
    from app_pages.summarizer_page import show_summarizer
    show_summarizer()

elif page == "About":
    from app_pages.about import show_about
    show_about()