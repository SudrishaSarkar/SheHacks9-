from google.cloud import translate_v2 as translate

def translate_text(text, target_language='en'):
    """Translate text to English using Google Cloud Translation API."""
    client = translate.Client()
    result = client.translate(text, target_language=target_language)
    return result['translatedText']
