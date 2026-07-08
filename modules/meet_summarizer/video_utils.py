import subprocess

def extract_audio_from_video(video_path, audio_output_path):

    command = [
        "ffmpeg",
        "-i",
        video_path,
        "-y",
        audio_output_path
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Audio extracted successfully: {audio_output_path}")
        return audio_output_path

    except subprocess.CalledProcessError as e:
        print("Error during audio extraction:", e)
        raise