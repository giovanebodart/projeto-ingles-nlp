import subprocess
import os

STORAGE_DIR = "app/temp"

os.makedirs(STORAGE_DIR, exist_ok=True)


def convert_to_wav(audio_path: str, job_id: str) -> str:
    output_audio = os.path.join(STORAGE_DIR, f"{job_id}.wav")

    command = [
        "ffmpeg",
        "-i", audio_path,
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        output_audio,
        "-y"
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    return output_audio