from fastapi import FastAPI, WebSocket
from modules.voice_recognition import process_voice
from modules.sentiment_analysis import analyze_sentiment # type: ignore
from modules.translation import translate_text
from modules.web_scraper import fetch_resources # type: ignore
from modules.playlist_generator import generate_playlist

app = FastAPI()

@app.post("/rant/")
async def handle_rant(rant: str, translate: bool = False, target_language: str = "en"):
    # 1. Translate (if needed)
    if translate:
        rant = translate_text(rant, target_language)
    # 2. Analyze sentiment
    sentiment_result = analyze_sentiment(rant)
    # 3. Fetch resources
    resources = fetch_resources(sentiment_result["dominant_emotion"])
    # 4. Generate a mood playlist
    playlist = generate_playlist(sentiment_result["dominant_emotion"])

    return {
        "translation": rant if translate else None,
        "sentiment": sentiment_result,
        "resources": resources,
        "playlist": playlist,
    }

@app.websocket("/rant/voice")
async def handle_voice(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        voice_result = process_voice(data)
        await websocket.send_json(voice_result)
