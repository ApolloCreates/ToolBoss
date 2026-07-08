# toolboss/pages/dashboard.py

import streamlit as st

def show_dashboard():

    st.title("🛠️ ToolBoss")
    st.subheader("AI Productivity Suite")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.info("🤖 LEXA AI")
        st.write("""
        AI-powered assistant suite including:
        - Auditor
        - Interview Assistant
        - Librarian
        """)

    with col2:
        st.success("🎙️ Meeting Summarizer")
        st.write("""
        Upload meeting recordings and get:
        - Transcription
        - Summary
        - Action Items
        """)