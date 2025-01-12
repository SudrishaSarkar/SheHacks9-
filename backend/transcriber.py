from google.cloud import speech_v1p1beta1 as speech
import io

def transcribe_speech(audio_file):
    """Transcribe audio file to text using Google Speech-to-Text API."""
    client = speech.SpeechClient()

    # Read audio file
    audio_content = audio_file.read()

    # Configure request
    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    # Transcribe speech
    response = client.recognize(config=config, audio=audio)

    # Extract transcription
    for result in response.results:
        return result.alternatives[0].transcript

    return "Could not transcribe audio."
