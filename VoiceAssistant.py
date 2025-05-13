gimini_api  = "AIzaSyD79ETOO6_BgnyzSOzKKMFs07Fwtiz9CpA"


# from google import genai
import google.generativeai as genai
import pyttsx3    #tts module of python [This library converts the text to speech form.]
import speech_recognition as sr  # for the stt module of python [This library is able to convert the voice to text]

# ---------- This is the part of gimini AI ---------------  {
# Configuring the gimini
genai.configure(api_key=gimini_api)
model = genai.GenerativeModel("gemini-1.5-flash")

# defining the custome rules for the gimini for taking it oly for the resutaurant related works
chat = model.start_chat(history=[
    {
        "role": "user",
        
        "parts": ["""
You are a restaurant recommendation voice assistant.
You are a helpful assistant that recommends restaurants based on cuisine, budget, and location.
Ask follow-up questions if needed, then suggest 2-3 good options in bullet points with reasons.
                  
Rules:
- When someone asks "Who are you?", reply: "I'm your Restaurant Recommendation Voice Assistant. You can ask me for restaurant suggestions based on cuisine, location, or budget."
- If someone asks something not about restaurants, respond: "Sorry, I'm only trained to provide restaurant-related information."
- If any required info (cuisine, budget, location) is missing, ask a polite follow-up question.
- Keep responses short, polite, and useful.
"""]
    }
])

# -------------------------------------------------   }

# -------- This is the part of the PYTTSX3 ---------------   {
# some pyttsx3 configurations
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Try to auto-select Indian English if available
indian_voice = None
for voice in voices:
    if "India" in voice.name or "en-in" in voice.id:
        indian_voice = voice.id
        break

if indian_voice:
    engine.setProperty('voice', indian_voice)
    print("Indian English voice set!")
else:
    print("Indian English voice not found. Using default.")

# --------------------------------------------------   }


# This is code bloc related to the Speach to text convertion ------------  {

recognizer = sr.Recognizer()

#  -------------------------------------------------------------- }


while True:
    # prompt = input("You: ")

    try:
        # Use microphone as input source
        with sr.Microphone() as source:
            print("\n🕒 Listening... (Say something)")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

        # Convert speech to text
        text = recognizer.recognize_google(audio, language='en-IN')
        print("✅ You said:", text)

         # Exit condition
        if text.lower() in ['exit', 'quit', 'stop']:
            print("👋 Exiting. Goodbye!")
            break
        
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ API error: {e}")
    except sr.WaitTimeoutError:
        print("⌛ Timeout: You were silent. Try again.")
    
    if text.lower() in ["exit", "quit"]:
        break
    
    response = chat.send_message(text)
    print(f"Restaurant Assistant: {response.text}")
    engine.say(response.text)
    engine.runAndWait()
    