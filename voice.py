import asyncio
import edge_tts

async def speak(text):
    tts = edge_tts.Communicate(text, voice="en-US-GuyNeural")  # male voice
    await tts.save("output.mp3")

asyncio.run(speak("Hello this is a test"))