from flask import Flask, request
import google.generativeai as genai

app = Flask(__name__)

https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key="AQ.Ab8RN6LTEH_q-ic4iR55pqZJXqwd9HVv-PmaGyKq_kYtkru2Og" 


# 🏠 Home route (check server)
@app.route('/')
def home():
    return "Server chal raha hai 🚀"


# 💬 Chat route (MAIN)
@app.route('/chat')
def chat():
    user_msg = request.args.get('msg')

    # agar message nahi mila
    if not user_msg:
        return "Message nahi mila"

    try:
        response = model.generate_content(user_msg)

        reply = response.text   # 👈 IMPORTANT

        return reply   # 👈 DIRECT TEXT (NO JSON)

    except Exception as e:
        return "Error: " + str(e)


# ▶️ Run server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
