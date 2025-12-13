import os
import json
from flask import Flask, request, jsonify
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

app = Flask(__name__)

@app.route("/", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = model.generate_content(prompt)

    return jsonify({
        "result": response.text
    })

