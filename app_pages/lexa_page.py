import streamlit as st
import os
import sys

# ---------------- PATH FIX ---------------- #

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

PROJECT_ROOT = os.path.abspath(
    os.path.join(CURRENT_DIR, "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ---------------- IMPORT ENGINE ---------------- #

from modules.lexa.engine import lexa_app

# ---------------- MAIN FUNCTION ---------------- #

def show_lexa():

    st.title("⚖️ Lexa: The Digital Arbitrator")
    st.subheader("Autonomous Compliance & Claims Verification")

    st.markdown("---")

    # ---------------- SIDEBAR ---------------- #

    with st.sidebar:

        st.header("📋 Case Status")

        st.info(
            "Lexa is currently using the "
            "'Standard Electronics Policy' "
            "for verification."
        )

        if st.button("Reset Session"):

            if "final_report" in st.session_state:
                del st.session_state["final_report"]

            st.rerun()

    # ---------------- MAIN LAYOUT ---------------- #

    col1, col2 = st.columns([1, 1])

    # ==================================================
    # LEFT SIDE
    # ==================================================

    with col1:

        st.write("### 🎤 Step 1: Tell Your Story")

        user_story = st.text_area(
            "Describe what happened...",
            placeholder=(
                "e.g., My Sony headphones were stolen "
                "from my office desk in Mumbai yesterday. "
                "They cost 25,000 rupees."
            ),
            height=200
        )

        start_btn = st.button("🚀 Launch Lexa Audit")

    # ==================================================
    # RIGHT SIDE
    # ==================================================

    with col2:

        st.write("### 🏁 Step 2: Lexa's Verdict")

        # ---------------- PROCESS ---------------- #

        if start_btn and user_story:

            inputs = {
                "user_input": user_story
            }

            try:

                with st.status(
                    "Lexa is deliberating...",
                    expanded=True
                ) as status:

                    for output in lexa_app.stream(inputs):

                        for node_name, data in output.items():

                            st.write(
                                f"✅ Department "
                                f"**{node_name.upper()}** "
                                f"has finished."
                            )

                            # ---------------- STATUS UPDATES ---------------- #

                            if node_name == "interviewer":

                                status.update(
                                    label=(
                                        "Intake complete. "
                                        "Consulting Policy Database..."
                                    )
                                )

                            if node_name == "auditor":

                                status.update(
                                    label="Arbitration Complete!",
                                    state="complete"
                                )

                                st.session_state.final_report = data

                st.success("Analysis Finished!")

                # ---------------- TABS ---------------- #

                tab1, tab2 = st.tabs(
                    [
                        "📝 Final Verdict",
                        "📚 Policy Citations"
                    ]
                )

                # ---------------- VERDICT ---------------- #

                with tab1:

                    if isinstance(
                        st.session_state.final_report,
                        dict
                    ):

                        verdict = (
                            st.session_state.final_report
                            .get("verdict", "No verdict generated.")
                        )

                        st.markdown(verdict)

                    else:
                        st.write(st.session_state.final_report)

                # ---------------- SOURCES ---------------- #

                with tab2:

                    st.write(
                        "Lexa found these relevant "
                        "sections in your policy:"
                    )

                    if isinstance(
                        st.session_state.final_report,
                        dict
                    ):

                        sources = (
                            st.session_state.final_report
                            .get("sources", [])
                        )

                        if sources:

                            for source in sources:

                                st.caption(source)
                                st.divider()

                        else:
                            st.info("No policy citations found.")

            except Exception as e:

                st.error(f"Error occurred: {e}")

        elif start_btn and not user_story:

            st.warning("Please enter your story first.")