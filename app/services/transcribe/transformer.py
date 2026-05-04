import subprocess
import os

STORAGE_DIR = "app/temp"
os.makedirs(STORAGE_DIR, exist_ok=True)


def convert_to_wav(audio_path: str, job_id: str) -> str:
    output_wav = os.path.join(STORAGE_DIR, f"{job_id}.wav")

    command = [
        "ffmpeg",
        "-i", audio_path,
        "-ar", "16000",   # 16kHz — exigido pelo Whisper para máxima precisão
        "-ac", "1",       # Mono
        "-c:a", "pcm_s16le",
        output_wav,
        "-y",             # Sobrescreve se já existir
    ]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        error_msg = result.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(f"ffmpeg falhou para job {job_id}: {error_msg}")

    return output_wav