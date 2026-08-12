# snip 1

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow , QWidget , QHBoxLayout , QVBoxLayout , QLabel , QTextEdit , QLineEdit, QPushButton
from PyQt5.QtCore import Qt
import time
from pathlib import Path
from PyQt5.QtCore import QThread,pyqtSignal
import re
import pyttsx3

crnt_dir=Path(__file__).resolve().parent
proj_root=crnt_dir.parent
if str(proj_root) not in sys.path:
    sys.path.append(str(proj_root))

from brain import ask_aria,history
from camera import ai_camer
from voice import Ai_listener 
from PyQt5.QtGui import QPixmap





class ai_writer(QThread):
    finished = pyqtSignal(str)
    

    def __init__(self,user_message):
        super().__init__()
        self.message=user_message
        self.voice_buffer=""
        self.speaking=Ai_listener()
    def run(self):
        for chunk in ask_aria(self.message):
            self.finished.emit(chunk)
            self.msleep(70)
            self.voice_buffer+=chunk
            if re.search(r'[.!?\n]',chunk):
                sentence=self.voice_buffer.strip()
                if sentence:
                   self.speaking.speak(sentence)

                self.voice_buffer=""

class ARIAWindow(QMainWindow):
    def add_mes(self,sender,message):
        if sender == "ARIA":
            color = "#00d4ff"
        else:
            color = "#9b59b6"
     
        self.chat_display.append(
            f'<span style="color:{color}; font-weight:bold;">{sender}:</span> '
            f'<span style="color:#ddd;">{message}</span><br>'
        )
       
       

    def send_msg(self):
        text= self.text_input.text().strip()
        if not text:
            return
        self.add_mes("You",text)
        self.text_input.clear()
        self.add_mes("ARIA","Processing your request....")
        self.chat_display.append('<span style="color:#00d4ff; font-weight:bold;">ARIA: </span>')
        self.worker=ai_writer(text)
        self.worker.finished.connect(self.on_show)
        self.worker.start()
        # res=ask_aria(text)
        # self.add_mes("ARIA",res)

    def on_show(self,reply):
        cursor= self.chat_display.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertHtml(f'<span style="color:#ddd; font-size: 26px; white-space:pre-wrap;">{reply}</span>')
        self.chat_display.setTextCursor(cursor)    

    def on_camera(self,image):
         self.cam_display.setPixmap(QPixmap.fromImage(image))

    def close_camera(self):
        # 1. Thread se aane wale signal ko temporary disconnect kar diya taaki naya frame na aaye
        try:
            self.worker2.finished.disconnect(self.on_camera)
        except TypeError:
            pass  # Agar pehle se disconnected ho toh crash na ho
            
        # 2. Background thread ko safely band kiya
        self.worker2.stop()
        
        # 3. Purane stuck frame ko ab saaf karein (ab koi frame iske baad nahi chipkega!)
        self.cam_display.clear()
        self.cam_display.setText("Camera is OFF")
        self.cam_display.setAlignment(Qt.AlignCenter)

    def open_camera(self):
        self.cam_display.setText("Camera Loading...")
        
        # 1. Pehle connection dobara lagayein taaki images aana shuru hon
        try:
            self.worker2=ai_camer()
            self.worker2.finished.connect(self.on_camera)
        except TypeError:
            pass  # Double connection se bachne ke liye
            
        # 2. Worker ko dobara fire karein
        self.worker2.start()

    
    def listn(self):
        self.worker3= Ai_listener()
        # Input field (QLineEdit) ya Chat display (QTextEdit) mein text set karne ke liye:
        self.worker3.finished.connect(self.voicetext)
        self.worker3.start()

    def voicetext(self,text):
        u_t=text
        print('texting in voice text to fill full your field wait buddy')
        self.text_input.setText(u_t)
        from PyQt5.QtWidgets import QApplication
        QApplication.processEvents()  # makes sure UI updates first
        self.send_msg()
            
            
    
    def __init__(self):
        super().__init__()
        self.worker2=ai_camer()
        self.worker2.finished.connect(self.on_camera)
        self.worker2.start()
        self.setWindowTitle("Aria AI OS")
        self.setGeometry(0,0,1900,900)
        self.setStyleSheet("background-color: #0a0a0a; ")
        # snip 2 central widgets 
        central =QWidget() #   widget 1  bnaya canvas container 
        self.setCentralWidget(central)  # make it main container

        main_layout= QHBoxLayout(central) # tu items ko horizontal dal
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10,10,10,10)
        # snip 3 LEft panel
        left_panel = QWidget() # widget  2 bnaya 
        left_panel.setStyleSheet("background-color: #111; border-radius: 10px; border:1px solid #9b59b6")
        left_panel.setFixedWidth(350)

        left_layout=QVBoxLayout(left_panel) # to items ko vertical dal 

        cam_label= QLabel("CAMERA FEED")
        cam_label.setAlignment(Qt.AlignCenter)
        cam_label.setStyleSheet("color: #00d4ff; font-size: 20px; font-weight: bold; margin:30px")

        self.cam_display = QLabel("Camera Loading.....")
        self.cam_display.setAlignment(Qt.AlignCenter)
        self.cam_display.setStyleSheet("color: #555; font-size: 14px; border: 2px solid #00d4ff")
        self.cam_display.setFixedHeight(460)

        send_btn1 = QPushButton("ON")
        send_btn2 = QPushButton("CLOSE")
        send_btn1.setStyleSheet("""
                    QPushButton {
                        background-color: #00d4ff;
                        color: black;
                        border-radius: 8px;
                        padding: 10px 20px;
                        font-weight: bold;
                        font-size: 15px;
                        height:20px;
                        
                    }
                    QPushButton:hover { background-color: #00b8d9; }
                """)
        send_btn2.setStyleSheet("""
                    QPushButton {
                        background-color: #9b59b6;
                        color: white;
                        border-radius: 8px;
                        padding: 10px 20px;
                        font-weight: bold;
                        font-size: 15px;
                        height:20px;
                        
                    }
                    QPushButton:hover { background-color: #cc0000; }
                """)



        left_layout.addWidget(cam_label)
        left_layout.addWidget(self.cam_display)
        left_layout.addWidget(send_btn2)
        left_layout.addWidget(send_btn1)
        left_layout.addStretch()

        send_btn2.clicked.connect(self.close_camera)
        send_btn1.clicked.connect(self.open_camera)

        
        # [Abhi hum is left_panel ko main_layout mein daal rahe hain takay test ho sakay]
        main_layout.addWidget(left_panel)

        #snip 4 chat area
        center_panel=QWidget()
        center_panel.setStyleSheet("background-color: #111; border-radius: 10px;")
        center_layout=QVBoxLayout(center_panel)

        title=QLabel("🤖 ARIA AI OS")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00d4ff; font-size: 28px; font-weight: bold; padding: 10px;")
        center_layout.addWidget(title)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.chat_display.setStyleSheet("""
            QTextEdit {
                background-color: #1a1a1a;
                border: 1px solid #9b59b6;
                border-radius: 8px;
                padding: 20px 20px;
                font-size: 26px;
                
            
            }
        """)
        center_layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()
        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Type or speak to ARIA...")
        self.text_input.setStyleSheet("""
            QLineEdit {
                background-color: #1a1a1a;
                color: white;
                border: 1px solid #00d4ff;
                border-radius: 8px;
                padding: 10px;
                font-size: 20px;
                height:50px;
                
            }
        """)
        send_btn = QPushButton("Send BOss")
        send_btn.setStyleSheet("""
            QPushButton {
                background-color: #00d4ff;
                color: black;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 15px;
                height:50px;
            }
            QPushButton:hover { background-color: #00b8d9; }
        """)

        voice_btn = QPushButton(" Speak Up Boss")
        voice_btn.setStyleSheet("""
            QPushButton {
                background-color: #9b59b6;
                color: white;
                border-radius: 8px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 15px;
                height:50px;
            }
            QPushButton:hover { background-color: #cc0000; }
        """)
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(send_btn)
        input_layout.addWidget(voice_btn)
        center_layout.addLayout(input_layout)

        # Main horizontal layout mein panel ko add kiya
        main_layout.addWidget(center_panel)
        right_panel = QWidget()
        right_panel.setStyleSheet("background-color: #111; border-radius: 10px;")
        right_panel.setFixedWidth(450)
        right_layout = QVBoxLayout(right_panel)

        status_label = QLabel("⚡ SYSTEM STATUS")
        status_label.setAlignment(Qt.AlignCenter)
        status_label.setStyleSheet("color: #00d4ff; font-size: 24px; font-weight: bold;")

        self.status_items = QLabel(
            "🟢 AI Brain: Online\n"
            "🟢 Voice: Ready\n"
            "🟢 Camera: Active\n"
            "🟢 Gestures: Ready\n"
            "🟡 Web Search: Standby"
        )
        self.status_items.setStyleSheet("color: #aaa; font-size: 18px; padding: 10px;")

        right_layout.addWidget(status_label)
        right_layout.addWidget(self.status_items)
        right_layout.addStretch()

        # add right panel to main layout
        main_layout.addWidget(right_panel)
        self.add_mes("ARIA", "Hello! I am ARIA, your personal AI OS. How can I help you today?")                
        # 🔗 Event Listeners / Signals Connection
        self.text_input.returnPressed.connect(self.send_msg)
        send_btn.clicked.connect(self.send_msg)
        voice_btn.clicked.connect(self.listn)     
# if __name__=="__main__":
def starter():
    app = QApplication(sys.argv)  # 1. Engine start kiya
    window = ARIAWindow()          # 2. Window ka object banaya
    window.show()                  # 3. Window ko screen par dikhaya
    # sys.exit(app.exec_())          # 4. App ko chala kar loop mein daal diya
    return window  # Return the window object for further use if needed

