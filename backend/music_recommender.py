import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from emotion_to_genre_map import EMOTION_TO_GENRE
from random import choice
from config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

# Spotify API authentication
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

# List of Spotify's top 20 artists (curated)
TOP_ARTISTS = [
    "Taylor Swift", "Drake", "Bad Bunny", "The Weeknd", 
    "Ariana Grande", "Ed Sheeran", "BTS", "Justin Bieber", 
    "Doja Cat", "Olivia Rodrigo", "Billie Eilish", "Harry Styles", 
    "Kendrick Lamar", "Post Malone", "Dua Lipa", "Shawn Mendes", 
    "Selena Gomez", "Rihanna", "Coldplay", "Imagine Dragons"
]

def recommend_song(emotion):
    """Recommend a song based on the user's emotion."""
    genre = EMOTION_TO_GENRE.get(emotion, "pop")
    artist = choice(TOP_ARTISTS)

    # Search for tracks by the selected artist and genre
    results = sp.search(q=f"genre:{genre} artist:{artist}", type='track', limit=10)
    tracks = results['tracks']['items']

    if tracks:
        track = choice(tracks)  # Randomly pick a track
        return {
            "track_name": track['name'],
            "artist": track['artists'][0]['name'],
            "url": track['external_urls']['spotify']
        }

    return {"error": "No song found for the given emotion."}
