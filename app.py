from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Server is running"

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json

    input_text = data.get("input")
    voice = data.get("voice")

    return jsonify({
        "status": "success",
        "input": input_text,
        "voice": voice
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
