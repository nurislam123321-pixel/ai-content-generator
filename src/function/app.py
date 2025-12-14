import os
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = model.generate_content(prompt)
    return jsonify({"result": response.text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
