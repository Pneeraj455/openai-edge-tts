from flask import Flask, request, Response
import edge_tts
import asyncio
import io

app = Flask(__name__)

@app.route('/v1/audio/speech', methods=['POST'])
async def text_to_speech():
    try:
        data = request.get_json()
        text = data.get('input')
        voice = data.get('voice', 'hi-IN-MadhurNeural')
        response_format = data.get('response_format', 'mp3')

        communicate = edge_tts.Communicate(text, voice)
        audio_data = b''
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]

        return Response(
            audio_data,
            mimetype=f'audio/{response_format}',
            headers={"Content-Disposition": f'attachment; filename=speech.{response_format}'}
        )
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
