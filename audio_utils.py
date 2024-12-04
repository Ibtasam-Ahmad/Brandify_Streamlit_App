from openai import OpenAI
from io import BytesIO

def speech_to_text(audio_file, api_key):
    """Convert speech to text using OpenAI Whisper."""
    try:
        client = OpenAI(api_key=api_key)
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1"
        )
        return transcript.text
    except Exception as e:
        return f"Error during transcription: {e}"

def text_to_speech(text, api_key):
    """Convert text to speech using OpenAI API."""
    try:
        client = OpenAI(api_key=api_key)
        response = client.audio.speech.create(
            model="tts-1",
            input=text,
            voice="alloy"
        )
        audio_data = BytesIO(response.content)
        return audio_data
    except Exception as e:
        return f"Error during text-to-speech conversion: {e}"
