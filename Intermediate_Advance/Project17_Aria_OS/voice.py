import speech_recognition as sr
import pyttsx3
import os
from PyQt5.QtCore import QThread, pyqtSignal


class Ai_listener(QThread):
    finished=pyqtSignal(str)
  
    def __init__(self):
        super().__init__()
        self.is_speaking=False
        self.running=True
        pass
    def speak(self, text):
        try:
            self.is_speaking=True
            print("bhrwy ap to chup hogaa axhaa me bol rha hun")
            engine=pyttsx3.init('sapi5')
            voices=engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            engine.setProperty('rate',170)
            engine.setProperty('volume',1.0)
            engine.say(text)
            engine.runAndWait()
            engine.stop()
            self.is_speaking=False
            print("ab bhonk bhosdk ke !!!!")
        except Exception as e:
            print("TTS error:", e)


    def listen(self):
        r=sr.Recognizer()
        r.energy_threshold=3000
        r.pause_threshold=2.0
   
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            r.adjust_for_ambient_noise(source,duration=0.5)
            try:
                audio=r.listen(source,timeout=5)
                text=r.recognize_google(audio)
                print(f'You: {text}')
                return text.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""
        
    def run(self):
        self.is_speaking=False
        self.running=True
        self.speak("I am listening boss! What can I do for you?")
        while self.running:
                if self.is_speaking:
                    continue
                user_input = self.listen()
                if not user_input:
                    continue
                if any(word in user_input for word in ["exit", "bye", "goodbye", "stop"]):
                    self.speak("Goodbye boss! Stay safe!")
                    break
                self.finished.emit(user_input)
                print("ARIA thinking...")