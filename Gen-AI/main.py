"""
This is a Genrative AI MOdel .
Using Google Gemini API
"""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import datetime

# Load environment variables from .env file
load_dotenv(dotenv_path='./.env')


def get_greeting():
    now = datetime.datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def generate(user_input, history):
    api_key = os.environ.get("GOOGLE_API_KEY")

    if not api_key:
        print("Error: GOOGLE_API_KEY not found in .env file.")
        return ""

    client = genai.Client(
        api_key=api_key,
    )

    model = "gemini-2.0-flash-thinking-exp-01-21"
    contents = []
    for role, text in history:
        contents.append(types.Content(role=role, parts=[types.Part.from_text(text=text)]))
    contents.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        response_text += chunk.text
    return response_text

if __name__ == "__main__":
    conversation_history = []
    greeting = get_greeting()
    welcome_message = f" Hello User, {greeting} | Welcome to the Gen-AI Chatbot!"
    print(f"AI: {welcome_message}")
    conversation_history.append(("model", welcome_message))

    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() == "exit":
            break
        bot_response = generate(user_prompt, conversation_history)
        conversation_history.append(("user", user_prompt))
        conversation_history.append(("model", bot_response))
        print()