from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "AQ.Ab8RN6Kf1VyF-YeMnIY5BOCzUzaXfJB8iXvLDsDLpqZkYeS_1w" # 👈 apni API key daal

@app.route("/")
def home():
    return "Gemini Chatbot Running ✅"

@app.route("/chat")
def chat():
    user_msg = 
    request.json.get("msg")

    url =url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}" 

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
    except:
        reply = str(result)

    return reply
return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
