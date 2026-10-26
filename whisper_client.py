# whisper_client.py
import requests
import numpy as np
from audio_recorder import create_wav_buffer
from config import WHISPER_URL, TARGET_SAMPLE_RATE, WHISPER_MODEL

def transcribe_audio_chunk(audio_data: np.ndarray, retries =2) -> str | None:
    # Converts audio array into wav buffer in memory and posts to whisper endpoint
    wav_buffer = create_wav_buffer(audio_data, TARGET_SAMPLE_RATE)

    for attempt in range(retries):
        try:
            files = {"file": ("chunk.wav", wav_buffer, "audio/wav")}
            data = {
                "model": WHISPER_MODEL,
                "language": "en"
            }

            response = requests.post(WHISPER_URL, files=files, data=data, timeout=30)
            response.raise_for_status()

            result = response.json()
            return result.get("text", "").strip()

        except requests.exceptions.Timeout:
            print(f"\nWhisper API timeout {attempt+1}")
            continue
        except requests.exceptions.ConnectionError:
            print("Failed to connect to Whisper API")
            break
        except requests.exceptions.HTTPError as err:
            print(f"Whisper API returned HTTP error: {err}")
            break
        return None