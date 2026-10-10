from google import genai
from config import GEMINI_API_KEY


client = genai.Client(
    api_key="AQ.Ab8RN6Kw9tIsVIgJfXA7VHTMXRBayCS01OFZvygQv6GmwW1aoA"
)


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text
