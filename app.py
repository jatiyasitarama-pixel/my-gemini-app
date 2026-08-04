from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# API key set करो
genai.configure(api_key="AQ.Ab8RN6KPfnJtVhd4Z8R-OIyvsmZT6SXeabDCjiXE1bxnuEWQbg")

# model बनाओ
model = genai.GenerativeModel("gemini-3.6-flash")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = model.generate_content(user_input)

    return jsonify({
        "reply": response.text
    })

if __name__ == "__main__":
    app.run()
