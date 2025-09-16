# 🎙️ AI Voice Assistant
This project is a **real-time AI-powered voice assistant** built with Python and OpenAI.  
It listens to your speech, processes it with a conversational AI model, and replies back with **natural-sounding voice output**.  
Think of it as your own **Jarvis/Siri/Alexa** – but powered by **OpenAI GPT + TTS models**.

---

## ✨ Features

- 🎤 **Voice Input** – Speak naturally, and the assistant listens via your microphone.
- 📝 **Speech-to-Text** – Converts your voice into text using the `speech_recognition` library.
- 🤖 **AI Processing** – Sends your query to `gpt-4.1-mini` for conversational reasoning.
- 🔊 **Voice Output** – Converts AI replies into speech using `gpt-4o-mini-tts` with a cheerful `"sage"` voice.
- 🔄 **Interactive Loop** – Maintains conversation history for context-aware dialogue.
- ⚡ **Streaming TTS** – Audio playback starts while generation is still in progress.

---

## How to use this
1. clone this repo
2. install dependencies "pip install -r requirements.txt"
3. setup environment variable .env file
4. inside env file OPENAI_API_KEY=your_api_key_here
5. Run the assistant