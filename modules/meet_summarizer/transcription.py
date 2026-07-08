import whisper
from pydub import AudioSegment
import os

# 🔹 Explicitly tell Whisper where ffmpeg is
os.environ["FFMPEG_BINARY"] = r"C:\Users\pande\OneDrive\Desktop\ffmpeg-8.0-full_build\bin\ffmpeg.exe"  # Update to your actual ffmpeg.exe path

def extract_audio(video_path, audio_path="temp_audio.wav"):
    """
    Extracts audio from video and saves it as a WAV file.
    """
    audio = AudioSegment.from_file(video_path)  # pydub handles mp4, mov, avi
    audio.export(audio_path, format="wav")
    return audio_path

def transcribe_audio(audio_path):
    """
    Transcribes the audio file using Whisper.
    """
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")

    model = whisper.load_model("base")  # choose model: tiny, small, base, medium, large
    result = model.transcribe(audio_path)
    return result['text']

if __name__ == "__main__":
    video_path = "your_video.mp4"  # replace with your video file
    audio_path = extract_audio(video_path)
    
    print(f"✅ Audio extracted at {audio_path}")

    transcript = transcribe_audio(audio_path)
    print("📜 Transcription:\n", transcript)
