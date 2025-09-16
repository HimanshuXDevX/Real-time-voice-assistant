import asyncio
import speech_recognition as sr
import os

from openai import OpenAI
from openai.helpers import LocalAudioPlayer
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
async_client = AsyncOpenAI()

async def tts(speech: str):
    async with async_client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="sage",
        instructions="Speak in a cheerful and positive tone",
        input=speech,
        response_format="pcm",
    )as response:
        await LocalAudioPlayer().play(response)


def main():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 2

        SYSTEM_PROMPT = f"""
                You're an expert voice agent. You are given the transcript of what
                user has said using voice.
                You need to output as if you are an voice agent and whatever you speak
                will be converted back to audio using AI and played back to user.
            """
        
        messages = [
            { "role": "system", "content": SYSTEM_PROMPT },
        ]

        while True:

            print("Please Speak...")
            audio = r.listen(source)

            print("Processing Audio...")
            out = r.recognize_google(audio)

            print("You Said:", out)
            messages.append({ "role": "user", "content": out })

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=messages
            )

            print("AI Response", response.choices[0].message.content)
            asyncio.run(tts(speech=response.choices[0].message.content))

main()