from io import BytesIO
import openai

def speech_to_text(audio_file, api_key):
    """Convert speech to text using OpenAI Whisper."""
    try:
        openai.api_key = api_key
        audio_bytes = audio_file.read()
        response = openai.Audio.transcribe(
            model="whisper-1",
            file=BytesIO(audio_bytes)
        )
        return response['text']
    except Exception as e:
        return f"Error during transcription: {e}"

def text_to_speech(text, api_key):
    """Convert text to speech using OpenAI API."""
    try:
        openai.api_key = api_key
        response = openai.Audio.create(
            input=text,
            voice="alloy",
            model="tts-1"
        )
        return BytesIO(response['audio'])
    except Exception as e:
        return f"Error during text-to-speech conversion: {e}"
