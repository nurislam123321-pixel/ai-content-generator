import os
import json
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def generate_ai(request):
    # CORS
    if request.method == "OPTIONS":
        return ("", 204, {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "POST",
            "Access-Control-Allow-Headers": "Content-Type"
        })

    headers = {
        "Access-Control-Allow-Origin": "*"
    }

    data = request.get_json(silent=True)
    prompt = data.get("prompt") if data else None

    if not prompt:
        return (json.dumps({"error": "No prompt"}), 400, headers)

    response = model.generate_content(prompt)

    return (json.dumps({"result": response.text}), 200, headers)
