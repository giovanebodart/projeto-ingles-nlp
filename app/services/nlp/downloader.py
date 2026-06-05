import yt_dlp
import os

STORAGE_DIR = "app/temp"
os.makedirs(STORAGE_DIR, exist_ok=True)


def download_video(url: str, job_id: str) -> str:
    output_template = os.path.join(STORAGE_DIR, f"{job_id}.%(ext)s")

    ydl_opts = {
        "outtmpl": output_template,
        "format": "bestaudio/best",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        file_path = ydl.prepare_filename(info)

    return file_path