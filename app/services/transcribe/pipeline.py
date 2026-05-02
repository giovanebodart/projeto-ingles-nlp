import os
from downloader import download_video
from transformer import convert_to_wav
from transcriber import transcribe_audio

STORAGE_DIR = "app/temp"
os.makedirs(STORAGE_DIR, exist_ok=True)

def execute(url: str, job_id: str) -> str:
    audio_path = download_video(url, job_id)
    convert_to_wav(audio_path, job_id)
    transcribe_audio(audio_path, job_id)