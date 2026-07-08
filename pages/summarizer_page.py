import streamlit as st
import tempfile
import os

from modules.meet_summarizer.transcription import transcribe_audio
from modules.meet_summarizer.summarization import summarize_text
from modules.meet_summarizer.action_items import extract_action_items
from modules.meet_summarizer.video_utils import extract_audio_from_video


def show_summarizer():

    st.title("🎙️ AI Meeting Summarizer")

    uploaded_file = st.file_uploader(
        "Upload meeting audio/video",
        type=["mp3", "wav", "mp4"]
    )

    if uploaded_file is not None:

        st.success("File uploaded successfully!")

        # Create temp file
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            temp_path = tmp_file.name

        file_extension = uploaded_file.name.split(".")[-1]

        try:

            # ---------------- VIDEO HANDLING ---------------- #

            if file_extension == "mp4":

                st.info("Extracting audio from video...")

                audio_path = "temp_audio.wav"

                extract_audio_from_video(
                    temp_path,
                    audio_path
                )

            else:
                audio_path = temp_path

            # ---------------- TRANSCRIPTION ---------------- #

            st.info("Transcribing audio...")

            transcript = transcribe_audio(audio_path)

            st.subheader("📝 Transcript")
            st.write(transcript)

            # ---------------- SUMMARY ---------------- #

            st.info("Generating summary...")

            summary = summarize_text(transcript)

            st.subheader("📌 Summary")
            st.write(summary)

            # ---------------- ACTION ITEMS ---------------- #

            st.info("Extracting action items...")

            actions = extract_action_items(transcript)

            st.subheader("✅ Action Items")
            st.write(actions)

        except Exception as e:
            st.error(f"Error: {e}")

        finally:

            if os.path.exists(temp_path):
                os.remove(temp_path)