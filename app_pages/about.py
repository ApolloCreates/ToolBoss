import streamlit as st


def show_about():

    # ---------------- HERO SECTION ---------------- #

    st.title("🚀 About ToolBoss")

    st.markdown(
        """
        ### One workspace. Multiple AI-powered tools.

        **ToolBoss** is an AI-powered productivity platform designed to bring
        useful intelligent utilities together in one simple workspace.

        Instead of switching between different applications for transcription,
        summarization, document analysis, and AI-assisted workflows, ToolBoss
        provides a unified environment where these capabilities can be accessed
        from a single platform.
        """
    )

    st.divider()

    # ---------------- PLATFORM OVERVIEW ---------------- #

    st.header("💡 What is ToolBoss?")

    st.markdown(
        """
        ToolBoss is built around the idea of combining multiple AI utilities
        into one productivity platform.

        The platform provides specialized tools that can help users:

        - 🎙️ **Transcribe audio and meetings**
        - 📝 **Generate concise meeting summaries**
        - ✅ **Identify action items automatically**
        - 🤖 **Analyze information using AI agents**
        - 📚 **Work with policies and structured information**
        - 🔍 **Extract useful insights from unstructured content**

        Each tool is designed to perform a specific task while sharing the
        same overall platform experience.
        """
    )

    # ---------------- FEATURES ---------------- #

    st.header("✨ What ToolBoss Can Do")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎙️ AI Meeting Summarizer")

        st.write(
            """
            Upload an audio or video recording of a meeting and transform
            lengthy conversations into useful information.

            The meeting workflow can:

            • Transcribe spoken conversations  
            • Generate a structured summary  
            • Extract potential action items  
            • Help users quickly understand what happened during a meeting
            """
        )

        st.subheader("🤖 LEXA AI")

        st.write(
            """
            LEXA is an AI-powered multi-agent workflow designed to analyze
            claims and evaluate them against predefined policy rules.

            Different AI departments collaborate during the analysis process,
            including an interviewer and an auditor, before producing a final
            verdict.
            """
        )

    with col2:

        st.subheader("🧠 Intelligent Processing")

        st.write(
            """
            ToolBoss combines modern AI and NLP technologies to process
            unstructured information and convert it into useful outputs.

            Depending on the tool, the platform can work with:

            • Text  
            • Audio  
            • Video  
            • Structured information  
            • Policy documents
            """
        )

        st.subheader("⚡ Productivity Focused")

        st.write(
            """
            ToolBoss focuses on reducing repetitive work and helping users
            extract useful information faster.

            Instead of manually listening to meetings, searching through
            transcripts, or checking every field of a claim, AI-assisted
            workflows handle much of the initial processing.
            """
        )

    st.divider()

    # ---------------- TECHNOLOGY ---------------- #

    st.header("🛠️ Technology Behind ToolBoss")

    st.markdown(
        """
        ToolBoss brings together several modern technologies from the
        Python and AI ecosystem.
        """
    )

    tech_col1, tech_col2, tech_col3 = st.columns(3)

    with tech_col1:

        st.markdown("### 🐍 Python")

        st.write(
            "Core programming language used to build the platform and AI workflows."
        )

        st.markdown("### 🎨 Streamlit")

        st.write(
            "Provides the interactive web interface and application dashboard."
        )

    with tech_col2:

        st.markdown("### 🤗 Hugging Face")

        st.write(
            "Used for transformer-based NLP and text processing workflows."
        )

        st.markdown("### 🎙️ Whisper")

        st.write(
            "Used for converting spoken audio into text transcripts."
        )

    with tech_col3:

        st.markdown("### 🕸️ LangGraph")

        st.write(
            "Used to build stateful multi-step and multi-agent AI workflows."
        )

        st.markdown("### 🗄️ ChromaDB")

        st.write(
            "Provides vector-storage capabilities for AI and retrieval workflows."
        )

    st.divider()

    # ---------------- HOW IT WORKS ---------------- #

    st.header("⚙️ How ToolBoss Works")

    st.markdown(
        """
        ToolBoss follows a modular architecture. Each utility has its own
        processing pipeline while the Streamlit application provides a
        unified interface.
        """
    )

    step1, step2, step3, step4 = st.columns(4)

    with step1:
        st.markdown("### 01")
        st.subheader("Input")
        st.write("Users provide text, audio, video, or other supported information.")

    with step2:
        st.markdown("### 02")
        st.subheader("Process")
        st.write("The selected AI workflow processes the provided information.")

    with step3:
        st.markdown("### 03")
        st.subheader("Analyze")
        st.write("AI models and specialized workflows extract useful information.")

    with step4:
        st.markdown("### 04")
        st.subheader("Output")
        st.write("The processed results are presented in an easy-to-understand format.")

    st.divider()

    # ---------------- VISION ---------------- #

    st.header("🎯 Our Vision")

    st.markdown(
        """
        The goal of ToolBoss is to create a practical AI workspace where
        intelligent tools can work together instead of existing as isolated
        applications.

        As the platform evolves, additional AI utilities and agent-based
        workflows can be integrated into the same ecosystem.

        **The long-term vision is simple: make AI-powered productivity tools
        accessible from one place.**
        """
    )

    # ---------------- WHY TOOLBOSS ---------------- #

    st.header("🌟 Why ToolBoss?")

    reasons = [
        ("🧩 Modular", "Each tool is designed as an independent module."),
        ("🤖 AI-Powered", "Uses modern AI models and intelligent workflows."),
        ("⚡ Practical", "Focused on solving real productivity problems."),
        ("🔗 Extensible", "New AI tools can be added to the platform."),
        ("🎯 Unified", "Multiple utilities are accessible through one interface."),
        ("📈 Scalable", "The architecture can evolve as new capabilities are added."),
    ]

    for i in range(0, len(reasons), 2):

        col1, col2 = st.columns(2)

        with col1:
            title, description = reasons[i]
            st.markdown(f"### {title}")
            st.write(description)

        if i + 1 < len(reasons):

            with col2:
                title, description = reasons[i + 1]
                st.markdown(f"### {title}")
                st.write(description)

    st.divider()

    # ---------------- FOOTER ---------------- #

    st.markdown(
        """
        <div style="text-align:center; padding:30px 0;">

        <h3>🚀 ToolBoss</h3>

        <p>
        AI-powered utilities. One unified workspace.
        </p>

        <p style="color:gray;">
        Built to explore the practical possibilities of modern AI.
        </p>

        </div>
        """,
        unsafe_allow_html=True,
    )