import speech_recognition as sr
from PyQt5.QtCore import QThread, pyqtSignal 
from PyQt5.QtWidgets import QApplication
from gui.main_window import starter
import sys
from pathlib import Path
import signal
import random
import pyttsx3
import time

crnt_dir=Path(__file__).resolve().parent
proj_root=crnt_dir.parent
if str(proj_root) not in sys.path:
    sys.path.append(str(proj_root))

def  speak(texx):
    engine= pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 1.0)
    engine.say(texx)
    engine.runAndWait()
    engine.stop()



class WakeThread(QThread):
    wake_signal = pyqtSignal()
    already_here=pyqtSignal()
    close_ui_signal=pyqtSignal()
    terminate_signal=pyqtSignal()  # Signal to indicate termination
    def __init__(self):
        super().__init__()
        self.running=True
        self.close_ui=False # to track ke ui open h
        self.terminate_sig=False # to track ke terminate command aaya h ya nahi

    def run(self):
        r=sr.Recognizer()
        r.energy_threshold=3000
        r.pause_threshold=1.0

        wake_words  = ['uth jao','wake up', 'arya', 'arya wake up', 'are you there arya']
        close_words = ['close', 'close arya', 'arya close']
        response_words = ['yes Umar', 'i am here', 'i am listening babe', 'how can i help you Baby', 'hey my sexy boss']
        already_here_words = ['i am already here', 'i am already babe', 'fuck me i am here', 'for you always Umar']
        closing_words=['ok good bye','take care boss','as you wish','ok babe','ok my sexy boss']
        termiation_words=['termination done boss','kill command successful','program killed']
        random.shuffle(response_words)
        random.shuffle(already_here_words)
        random.shuffle(closing_words)
        random.shuffle(termiation_words)
        while self.running:
            try:
                 with sr.Microphone() as source:
                    if self.close_ui:
                        print("😴 Background listener paused while UI is open...")
                    else:   
                        print("😴 Sleeping... say ARIA to wake")
                    r.adjust_for_ambient_noise(source,duration=0.5)
                    audio=r.listen(source,timeout=5, phrase_time_limit=5)
                    text=r.recognize_google(audio)
                    print(f'You: {text}')
                    if not self.close_ui and any(word in text.lower() for word in wake_words):
                        choices=random.choice(response_words)
                        speak(choices)
                        self.wake_signal.emit()
                        print("⚡ here we go to active!")
                    elif self.close_ui and any(word in text.lower() for word in wake_words):
                        choices=random.choice(already_here_words)
                        speak(choices)
                        self.already_here.emit()
                        print("⚡ Already active!")    
                   # CASE 3: UI Khula hai aur Close Word bola
                    elif  self.close_ui and any(word in text.lower() for word in close_words):
                        print("😴 Close command detected! Closing UI...")
                        self.close_ui = False
                        choices=random.choice(closing_words)
                        speak(choices)
                        self.close_ui_signal.emit() 
                     # ✅ Cleanest
                    elif any(word in text.lower() for word in ['terminate','kill the script','kill the program']):
                        print("Termination command detected!")
                        choices = random.choice(termiation_words)
                        speak(choices)
                        self.terminate_signal.emit()
                        break
                        # sys.exit(0)
            except sr.WaitTimeoutError:
                continue  # silence — keep listening
            except sr.UnknownValueError:
                continue  # couldn't understand — keep listening
            except Exception as e:
                print(f"Wake word error: {e}")
                continue
    def stop(self):
        self.running=False
        self.quit()  
        # self.wait()   
        if not self.wait(1000):  # Wait for 1 second
            print("Thread did not terminate in time, forcing termination.")
            self.terminate()  # Forcefully terminate the thread

class master_controller(QThread):
    def __init__(self,wake_Thread):
        super().__init__()
        self.window=None
        self.wake_thread=wake_Thread

    def open_window(self):
        if self.window is None:
            self.window = starter()  # Call the starter function to create the window
            self.window.show()
            self.wake_thread.close_ui = True  # Set the flag to indicate that the UI is open
            print("ARIA UI Opened. Background listener paused...")
        else:
            self.window.show()  # Show the existing window if it's already created
            self.window.activateWindow()
            print("Already open — bringing to front")

    def handle_already_here(self):
        print("ARIA: Boss, I am already here!")
        if self.window:
            self.window.activateWindow()  # Window ko samne Focus mein le aao

    def close_ui(self):
        if self.window:
            self.window.hide()  # Hide the window instead of closing it
            self.window = None
            self.wake_thread.close_ui = False  # Reset the flag to indicate that the UI is closed
            print("ARIA UI Closed. Background listener running...")
    def terminatation(self):
        print("Termination signal received.Sweep  clean")
        self.wake_thread.stop()  # Stop the wake thread
        sys.exit(0)  # Exit the application

if __name__ == "__main__":
    # Terminal par Ctrl + C se complete kill karne ke liye
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = QApplication(sys.argv)

    app.setQuitOnLastWindowClosed(False)  # Ensure the app doesn't quit when the window is closed
    wakeThread = WakeThread()
    controller = master_controller(wakeThread)

    # Signals Connection
    wakeThread.wake_signal.connect(controller.open_window)
    wakeThread.already_here.connect(controller.handle_already_here)
    wakeThread.close_ui_signal.connect(controller.close_ui)
    wakeThread.terminate_signal.connect(controller.terminatation)

    wakeThread.start()
    print("🚀 ARIA background listener started!")
    print("Say 'ARIA' to open | Say 'Close ARIA' to close")
    sys.exit(app.exec_())