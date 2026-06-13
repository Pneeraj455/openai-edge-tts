from flask import Flask, request, Response
import edge_tts
import asyncio
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Edge TTS Server is running! Use POST /v1/audio/speech"

@app.route('/v1/audio/speech', methods=['POST'])
async def text_to_speech():
    try:
        data = request.get_json()
        if not data:
            return {"error": "No JSON data"}, 400

        text = data.get('input') or data.get('text')
        voice = data.get('voice', 'hi-IN-MadhurNeural')
        response_format = data.get('response_format', 'mp3')

        if not text:
            return {"error": "No input text provided"}, 400

        communicate = edge_tts.Communicate(text=text, voice=voice)

        audio_data = b''
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]

        return Response(
            audio_data,
            mimetype=f'audio/{response_format}',
            headers={
                "Content-Disposition": f'attachment; filename=speech.{response_format}'
            }
        )
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
