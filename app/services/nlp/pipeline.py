import os
import uuid
from app.services.nlp.downloader import download_video
from app.services.nlp.transformer import convert_to_wav
from app.services.nlp.transcriber import transcribe_audio
from app.services.nlp.analyze import analyze_text

STORAGE_DIR = "app/temp"
os.makedirs(STORAGE_DIR, exist_ok=True)


def execute(url: str, language: str) -> dict:
    job_id = str(uuid.uuid4())

    video_path = None
    wav_path = None
    txt_path = None

    try:
        # 1. Download
        video_path = download_video(url, job_id)

        # 2. Converte para .wav e deleta o vídeo original
        wav_path = convert_to_wav(video_path, job_id)
        _delete_file(video_path)
        video_path = None

        # 3. Transcreve para .txt e deleta o .wav
        txt_path = transcribe_audio(wav_path, job_id)
        _delete_file(wav_path)
        wav_path = None
        
        texts = _read_txt(txt_path)
        _delete_file(txt_path)
        txt_path = None

        # 4. Analisa o .txt com o pipeline de NLP e retorna o response estruturado
        return analyze_text(url, texts, language)

    except Exception:
        _delete_file(video_path)
        _delete_file(wav_path)
        _delete_file(txt_path)
        raise

def _read_txt(txt_path: str) -> list[str]:
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines()]
    return [line for line in lines if line]

def _delete_file(path: str) -> None:
    try:
        if path and os.path.exists(path):
            os.remove(path)
    except OSError:
        pass