from translator import translate_text

def test_translation():
    text = "Hola Mundo"  # Example input
    translated = translate_text(text, target_language='en')
    print(f"Original: {text}")
    print(f"Translated: {translated}")

if __name__ == "__main__":
    test_translation()
