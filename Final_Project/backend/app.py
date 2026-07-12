from flask import Flask, request, jsonify
from flask_cors import CORS

from inference import chat
from config import HOST, PORT, DEBUG

app = Flask(__name__)

# Enable CORS
CORS(app)


# ==========================================
# Home Route
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "running",
        "message": "GPT Chatbot Backend is Live 🚀"
    })


# ==========================================
# Chat Route
# ==========================================

@app.route("/chat", methods=["POST"])
def chatbot():

    try:

        data = request.get_json()

        if data is None:
            return jsonify({
                "success": False,
                "error": "No JSON data received."
            }), 400

        prompt = data.get("message", "").strip()

        if prompt == "":
            return jsonify({
                "success": False,
                "error": "Empty message."
            }), 400

        response = chat(prompt)

        return jsonify({
            "success": True,
            "user": prompt,
            "response": response
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# ==========================================
# Run Server
# ==========================================

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)