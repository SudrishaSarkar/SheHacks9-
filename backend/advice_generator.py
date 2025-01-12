import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_advice(query):
    """Generate personalized advice based on the user's query."""
    prompt = f"""
    A user is asking for help with the following query:
    "{query}"

    Provide empathetic and practical advice tailored to their problem:
    """
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()
