# transcript.py
from datetime import datetime
from pathlib import Path

TRANSCRIPT_DIR = Path("transcripts")

def save_transcript(transcript: str) -> path:
    TRANSCRIPT_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = TRANSCRIPT_DIR / f"transcript_{timestamp}.txt"

    file_path.write_text(transcript, encoding="utf-8")

    return file_path