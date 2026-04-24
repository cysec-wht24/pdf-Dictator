import pypdf
import re
import asyncio
import edge_tts
import pygame
import io

VOICE = "en-US-ChristopherNeural"

ignore = [
    "NPTEL Online Certification Courses",
    "Indian Institute of Technology Kharagpur",
    "TYPE OF QUESTION: MCQ/MSQ",
    "week",
]

reader = pypdf.PdfReader("nptel.pdf")

start_page = 19
actual_page = start_page - 1

async def speak(text):
    tts = edge_tts.Communicate(text, voice=VOICE, rate="0%")
    audio = b""
    async for chunk in tts.stream():
        if chunk["type"] == "audio":
            audio += chunk["data"]

    pygame.mixer.init()
    pygame.mixer.music.load(io.BytesIO(audio))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)

for page in reader.pages[actual_page:]:
    text = page.extract_text()
    for phrase in ignore:
        text = re.sub(phrase, "", text, flags=re.IGNORECASE)
    asyncio.run(speak(text))