```python id="6g7r0w"
from flask import Flask, request, jsonify
import edge_tts
import asyncio

app = Flask(__name__)

@app.route("/")
def home():
    return "Server Running"

@app.route("/tts", methods=["POST"])
def tts():
    data = request.json

    text = data.get("input")
    voice = data.get("voice", "hi-IN-SwaraNeural")

    async def generate():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("output.mp3")

    asyncio.run(generate())

    return jsonify({
        "message": "Audio generated successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```
