from faster_whisper import WhisperModel
import os

TRANSCRIPTION_DIR = "app/temp"

os.makedirs(TRANSCRIPTION_DIR, exist_ok=True)

model = WhisperModel(
    "small",
    device="cuda",
    compute_type="float16"
)


def transcribe_audio(audio_path: str, job_id: str) -> str:
    segments, _ = model.transcribe(audio_path)

    output_file = os.path.join(TRANSCRIPTION_DIR, f"{job_id}.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment.text + "\n")

    return output_file