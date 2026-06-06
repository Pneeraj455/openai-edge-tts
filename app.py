from flask import Flask, request, jsonify

app = Flask(__name__)

# Home route (check server running)
@app.route("/", methods=["GET"])
def home():
    return "Server is running"

# TTS route (fix for your 404 issue)
@app.route("/tts", methods=["POST"])
def tts():
    data = request.json

    # safe extraction
    input_text = data.get("input", "")
    voice = data.get("voice", "")

    return jsonify({
        "status": "success",
        "input": input_text,
        "voice": voice
    })

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
