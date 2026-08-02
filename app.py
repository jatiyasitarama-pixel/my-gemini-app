from flask import Flask, request
import requests
import os
from dotenv import load_dotenv

# .env load karo
load_dotenv()

app = Flask(__name__)

# API key yaha se aayegi
API_KEY = os.getenv("API_KEY")
API_KEY="AQ.Ab8RN6ISAx91P1YQxXezECbTcW_-Cp6-H0HJC1liyQLwI0X-ZQ"
@app.route("/")
def home():
    return "Gemini Chatbot Running"

@app.route("/chat")
def chat():
    user_msg = request.args.get("msg")

    if not user_msg:
        return "Message nahi mila"

    url =url =url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}" 

    data = {
        "contents": [
            {
                "parts": [
                    {"text": user_msg}
                ]
            }
        ]
    }

    response = requests.post(url, json=data)
    result = response.json()

    try:
        reply = result["candidates"][0]["content"]["parts"][0]["text"]
        return reply
    except:
        return str(result)

if __name__ == "__main__":
    app.run(debug=True)