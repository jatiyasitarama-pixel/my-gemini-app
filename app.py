from flask import Flask, request
import os
import requests

app = Flask(__name__)

API_KEY = "AQ.Ab8RN6LvFXgrhzKYV4YeVr1Yg7NfpQaTf7hd7pDWbhpsSLIZ5Q"

@app.route('/')
def home():
    return "Gemini Chatbot Running ✅"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    user_msg = request.args.get('msg')
    if not user_msg:
        return "Message nahi mila", 400
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [{"parts": [{"text": user_msg}]}]
    }
    
    response = requests.post(url, json=data, headers=headers)
    result = response.json()
    
    try:
        reply = result['candidates'][0]['content']['parts'][0]['text']
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
