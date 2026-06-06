from flask import Flask, request, send_file
import edge_tts
import uuid
import asyncio

app = Flask(**name**)

@app.route("/")
def home():
return "TTS Server Running"

@app.route("/v1/audio/speech", methods=["POST"])
def tts():
data = request.json

```
text = data.get("input")
voice = data.get("voice", "hi-IN-SwaraNeural")

filename = f"{uuid.uuid4()}.mp3"

async def generate():
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(filename)

asyncio.run(generate())

return send_file(filename, mimetype="audio/mpeg")
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=10000)
