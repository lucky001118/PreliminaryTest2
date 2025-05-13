# 🎙️ Voice Restaurant Recommendation Assistant

This is a **Voice-Enabled AI Assistant** built using Python, Google Gemini API, and speech libraries. It listens to user voice commands, understands their restaurant-related preferences (like cuisine, budget, and location), and responds with spoken restaurant suggestions.

---

## 🚀 Features

| Feature                            | Description                                                                 |
|------------------------------------|-----------------------------------------------------------------------------|
| 🎤 Speech Recognition              | Converts voice input into text using `speech_recognition`.                  |
| 🧠 AI-Powered Recommendation       | Uses **Google Gemini (Generative AI)** for restaurant suggestions.         |
| 🔊 Text-to-Speech                  | Replies with a human-like voice using `pyttsx3`.                            |
| 🌐 Context-Aware Conversations     | Maintains basic chat history and handles follow-up questions.              |
| 🛑 Exit Gracefully                 | Say “exit”, “quit”, or “stop” to end the assistant.                        |
| 🇮🇳 Indian English Support          | Auto-selects Indian voice if available for better regional understanding.  |

---

## 🧱 System Architecture

             ┌────────────────────┐
             │ User Voice Input   │
             └────────┬───────────┘
                      ▼
             ┌────────────────────┐
             │ SpeechRecognition  │ (stt)
             └────────┬───────────┘
                      ▼
     ┌────────────────────────────────────┐
     │ Gemini Generative AI (via Google)  │
     │ - Understands context              │
     │ - Recommends restaurants           │
     └────────┬───────────────────────────┘
                      ▼
             ┌────────────────────┐
             │ pyttsx3 (tts)      │
             └────────┬───────────┘
                      ▼
             ┌────────────────────┐
             │ Voice Output       │
             └────────────────────┘

---

## 🛠️ How It Works

### 1. Google Gemini Configuration

```python
import google.generativeai as genai

genai.configure(api_key=gimini_api)
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(history=[ {... rules...} ])
```
Configures the Gemini model with custom rules.

Only responds to restaurant-related queries.

### 2. Text-to-Speech Setup (pyttsx3)

```python
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', indian_voice)  # if available
```

Converts AI text responses into voice.

Auto-selects Indian English voice for regional relevance.

### 3. Speech Recognition

```python 
import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    audio = recognizer.listen(source)
    text = recognizer.recognize_google(audio, language='en-IN')
```

Listens to user voice and converts it to text using Google API.

### 4. Main Interaction Loop

```python
while True:
    ...
    if text.lower() in ['exit', 'quit', 'stop']:
        break
    response = chat.send_message(text)
    engine.say(response.text)
    engine.runAndWait()
```

Keeps listening for commands.

Ends if exit command is detected.

Speaks the AI's recommendation using pyttsx3.

## 🧪 Example Usage
You: "Can you suggest a South Indian restaurant in Delhi under 500 rupees?"
Assistant:
🗣️ "Sure!

Saravana Bhavan – Known for authentic Tamil food. Affordable and family-friendly.

Sagar Ratna – Excellent dosas and quick service."

## 📦 Requirements
Python 3.7+

Packages:

pyttsx3

speech_recognition

google-generativeai

## Installation
```bash
pip install pyttsx3 SpeechRecognition google-generativeai
```

## 🔒 Notes
The Gemini API key is currently hardcoded – not secure for production. Use environment variables or secret managers in production.

The AI assistant is limited to restaurant-related conversations only.

## 📈 Future Improvements
GUI support with Tkinter or Streamlit

Multilingual capabilities

Integration with real-time restaurant APIs (like Zomato, Yelp, Google Maps)

Logging & advanced conversation history


