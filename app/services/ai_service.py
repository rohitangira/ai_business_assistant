import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch OpenAI API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(user_message: str) -> str:
    """
    Sends a user message to OpenAI GPT and returns the AI-generated response.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Choose the appropriate model
            messages=[{"role": "user", "content": user_message}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
