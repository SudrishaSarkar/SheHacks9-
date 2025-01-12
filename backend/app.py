from flask import Flask, request, jsonify
from transcriber import transcribe_speech
from translator import translate_text
from emotion_analyzer import analyze_emotion
from advice_generator import generate_advice
from music_recommender import recommend_song

app = Flask(__name__)

@app.route('/api/rant', methods=['POST'])
def handle_rant():
    """Main endpoint to handle user queries."""
    try:
        audio_file = request.files.get('audio')
        language = request.form.get('language', 'en')  # Default to English

        if not audio_file:
            return jsonify({"error": "No audio file provided."}), 400

        # Step 1: Transcribe speech to text
        text = transcribe_speech(audio_file)

        # Step 2: Translate text to English
        translated_text = translate_text(text, target_language='en')

        # Step 3: Analyze emotion
        emotion = analyze_emotion(translated_text)

        # Step 4: Generate advice
        advice = generate_advice(translated_text)

        # Step 5: Recommend a song
        song = recommend_song(emotion)

        return jsonify({
            "original_text": text,
            "translated_text": translated_text,
            "emotion": emotion,
            "advice": advice,
            "recommended_song": song
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def test_translation():
    text = "Hola Mundo"  # Example input
    translated = translate_text(text, target_language='en')
    print(f"Original: {text}")
    print(f"Translated: {translated}") 

if __name__ == "__main__":
    app.run(debug=True)
