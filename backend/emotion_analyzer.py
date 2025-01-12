import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_emotion(text):
    """Analyze emotion using OpenAI's GPT model."""
    prompt = f"Analyze the emotion of the following text: '{text}'. Is it positive, negative, or neutral?"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10
    )
    return response.choices[0].text.strip().lower()
