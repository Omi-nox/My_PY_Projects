import speech_recognition as sr
import pyttsx3
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))

history = [
    {"role": "system", "content": """You are ARIA, an advanced AI voice assistant 
    built by Umar using Python, Groq API and speech recognition. 
    You are helpful, smart and friendly.
    Keep responses SHORT and CONVERSATIONAL — max 2-3 sentences.
    Never use bullet points or markdown — you are speaking out loud."""}
]

def speak(text):
    print(f'ARIA: {text}')
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 2000
    r.pause_threshold = 2.0
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=5)
            text = r.recognize_google(audio)
            print(f'You: {text}')
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak('Internet connection issue!')
            return ""

def ask_aria(user_message):
    history.append({'role': 'user', 'content': user_message})
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=history,
        max_tokens=150
    )
    reply = response.choices[0].message.content
    history.append({'role': 'assistant', 'content': reply})
    return reply

# main loop
speak("Hello! I am ARIA, your AI voice assistant built by Umar. How can I help you?")

while True:
    user_input = listen()
    if not user_input:
        continue
    if any(word in user_input for word in ["exit", "bye", "goodbye", "stop"]):
        speak("Goodbye boss! Stay safe!")
        break
    print("ARIA thinking...")
    response = ask_aria(user_input)
    speak(response)