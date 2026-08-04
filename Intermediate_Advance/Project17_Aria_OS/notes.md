# 🤖 Project 17 — ARIA AI OS

Before we write a single line — we need to plan properly. Big projects fail without structure.

## 📁 Project Structure

Create this folder structure:
```
Project17_ARIA_OS/
├── main.py              ← starts everything
├── brain.py             ← Groq AI logic
├── voice.py             ← speech in/out
├── vision.py            ← camera + YOLO
├── automation.py        ← pyautogui controls
├── web_search.py        ← news + weather
├── .env                 ← API keys
├── .gitignore           ← ignore .env
├── models/
│   └── yolov8n.pt       ← copy from Project 12
└── gui/
    └── main_window.py   ← PyQt5 interface
```
## Before Snippet 1 — Install PyQt5
```
bash
pip install PyQt5
pip install pyqt5-tools if it is not working do this 
pip install PyQt5-Qt5 PyQt5-sip 
```
**PyQt5:** Python ka aik powerful GUI framework hai jo application ka main structure (skin aur skeleton) banane ke liye use hota hai, jaise windows, buttons, layouts, aur chat boxes.advance gui bnane ke lia use hota ha ye 

**PyQt5-tools:** Yeh PyQt5 ka aik helper toolkit hai, jismein Qt Designer software hota hai jo bina code likhe drag-and-drop ke zariye application ka interface design aur manage karne mein help karta hai.ske ilawa yeh code compilation aur debugging ke tools bhi provide karta hai. or backgroud application smooth chla tha ha .

**Is Project Mein Roll:** Halankeh hum ARIA ka poora code khud hathon se (programmatically) likh rahe hain taake tumhari coding strong ho, lekin background mein applications ko sahi tarah se run aur compile karne ke liye is helper library ka install hona zaroori hota hai.

## 🧩 Snippet 1 — The Main Window

This is ARIA's face. Open gui/main_window.py and type:
* **import sys :** python modulejb pyqt5 app bnd krty ha to system ko signal bhgta ha (sys.exit)
* **QApplication :** yeh pyqt5 ka engine any guui app run ke lia background me ek main event loop ha jo click events control krta ha
* **class ARIAWindow(QMainWindow):**Hum apni aik customized window bana rahe hain jo QMainWindow se properties udhaar le rahi hai (Inheritance). QMainWindow hamein aik standard desktop window deta hai jismein title bar, minimize, aur close buttons pehle se lage hote hain.
* **super().__init__():**Yeh line likhna zaroori hai takay QMainWindow ka background setup sahi se active ho jaye aur hum apni window ko customize kar sakein.
* **self.setGeometry(0, 0, 1200, 700):**Window ka size set kar raha hai. Pehle do numbers (0, 0) screen par window ki position (X, Y) hain, aur 1200 width (chaudai) jabke 700 height (lambaee) hai.
* **self.setStyleSheet("background-color: #0a0a0a;"):**Yeh bilkul CSS ki tarah kaam karta hai. Is line se humne ARIA ke interface ka background color pure dark/black (#0a0a0a) set kar diya.
* **Yeh jo QMainWindow aur QWidget wagera hain**, yeh hamari apni banayi hui classes nahi hain, balki PyQt5 library ki built-in classes hain.
* **from PyQt5.QtCore import Qt kis liye hai?:**Qt basically PyQt5 ka aik Mega-Namespace (Dictionary type samajh lo) hai, jismein pehle se hazaron constants aur settings store hoti hain.
   **Iska kaam kya hai?** Jab hamein kisi cheez ko align karna ho (jaise text ko center mein karna), keyboard ki kisi khas key ko pehchanna ho, ya kisi widget ka behavior control karna ho, to hum Qt module ka use karte hain.

Example: Aage chal kar jab hum likhenge cam_label.setAlignment(Qt.AlignCenter), to yeh jo Qt.AlignCenter hai, yeh isi module se aa raha hai jo system ko batata hai ke text ko bilkul beech (center) mein rakhna hai.

### important concepts and logic :
**🔥 1. Kya setCentralWidget kisi bhi widget ko main container bana deta hai?**
Ji haan, bilkul!
**QMainWindow (jo hamari main window hai)** ke paas pehle se aik khali slot hota hai jise wo "Central Area" kehta hai. Jab tum likhte ho self.setCentralWidget(any_widget), to tum PyQt5 ko kehte ho ke "Bhai, is pooray khali slot par is naye widget ko bitha do aur isko main container bna kar do."
Humne QWidget ko central banaya kyunki wo aik bilkul blank canvas hota hai jiske andar hum layouts laga kar mazeed widgets (Left, Center, Right panels) daal sakte hain.
**🎨 2. Yeh setStyleSheet, setFixedWidth, setAlignment properties kya hain aur kahan se aati hain?**
Yeh saari properties PyQt5 ki built-in functions (methods) hain.
QWidget (Parent Class): ***setFixedWidth(), setFixedHeight(), aur setStyleSheet()*** jaisi cheezein generic hain. Yeh har us widget par available hoti hain jo QWidget se banta hai (chahe wo button ho, label ho, ya khali panel).
Specific Properties: ***setAlignment()***sirf QLabel ya QLineEdit (text/display elements) par hota hai kyunki button ya khali panel ke andar ke text ko align karne ki logic unke apne paas hoti hai.
Hum inhein main_layout par nahi laga sakte kyunki layout koi visible cheez (widget) nahi hai, wo sirf aik invisible manager hai jo widgets ki jagah decide karta hai. Styling aur dimensions humesha visible widgets par lagti hain.
**🌐 3. Yeh CSS kahan se aa rahi hai? Kya hum HTML/CSS se apps bana sakte hain?**
PyQt5 ke andar aik feature hota hai jise QSS (Qt Style Sheets) kehte hain. Yeh 95% bilkul web wali standard CSS ki tarah hi kaam karti hai!
Agar tumhein HTML/CSS aati hai, to tumhare liye PyQt5 ko modern aur killer look dena bacchon ka khel ban jayega (jaise humne #111 aur border-radius: 10px use kiya).
HTML ka use: Tumne notice kiya hoga add_message function mein humne <span> tags use kiye hain! PyQt5 ke labels aur text boxes HTML tags ko bhi support karte hain, isliye hum chat ka color aur font HTML se control kar pa rahe hain.
**🧠 4. Sab se bada sawal: Kahin simple variable (cam_label) aur kahin self.cam_display kyun?**
Yeh Scope (Aukaat) ka farq hai brother! OOPs ka sab se main rule:
Simple Variable (cam_label): Yeh variable sirf __init__ constructor ke andar hi paida hota hai aur wahin khatam ho jata hai. Chunkeh humne camera ka title sirf aik baar likh kar chor dena hai, pure project mein isko kabhi dubara change nahi karna, isliye iske sath self. lagane ki zaroorat nahi hai.
self. ke sath (self.cam_display): Jab hum kisi variable ke sath self. laga dete hain, to wo poori Class ki property ban jata hai. Iska matlab hai ke hum is variable ko class ke kisi bhi aur function (jaise aage chal kar opencv wale function) mein direct access aur update kar sakte hain. Chunkeh camera feed real-time mein update hogi, isliye iska self. ke sath hona zaroori tha taake dusre functions isko pehchan sakein.
## 🧩 Snippet 2 — The Main Window
Is part mein hum seekhenge ke aik poori khaali window ko different areas (Left, Center, Right panels) mein kaise organize kiya jata hai. Iske liye hum use karenge Central Widget aur Main Horizontal Layout.
* **central = QWidget():** QMainWindow (jo hamari main window hai) ke paas pehle se aik khali screen hoti hai. Lekin us par direct designing nahi ki ja sakti. Hamein aik generic container element chahiye hota hai jise Central Widget kehte hain. Yeh samajh lo ke yeh aik khali canvas (board) hai jo humne window ke upar chipka diya hai taake ab saari cheezein iske upar set ho sakein.
* **self.setCentralWidget(central)** se humne window ko bata diya ke bhai, ab se tumhara main center area yahi central widget hai.
* **main_layout = QHBoxLayout(central):**QHBoxLayout (Horizontal Layout): Yeh sab se important concept hai! Horizontal ka matlab hota hai left-to-right (letao hua). Yeh layout apne andar aane wali tamam cheezon (widgets) ko ek ke baad ek, left se right ki taraf line mein lagata jata hai.
* **Chunkeh hamari ARIA OS mein 3 panels hain:** Left (Camera), Center (Chat), aur Right (System Stats), isliye humne Horizontal Layout chuna taake ye teeno panels side-by-side fit ho sakein. (central) likhne ka matlab hai ke yeh layout hamare canvas par apply ho jaye.
* **main_layout.setSpacing(10):**Yeh teeno panels ke darmiyan 10 pixels ka gap (fasla) rakhega taake panels aapas mein chipke na rahein aur interface neat lagay.
* **main_layout.setContentsMargins(10, 10, 10, 10):**Yeh window ke charon kinarom (Left, Top, Right, Bottom) se 10 pixels ka margin (space) chorta hai, bilkul CSS ki tarah, taake panels bilkul screen ke kinarom se touch na ho rahe hon.
* **left_layout.addStretch():**
Yeh aik invisible spring (spacer) ki tarah kaam karta hai. Yeh ooper ke saare widgets (labels) ko ooper push kar deta hai aur baki bachi hui saari khali jagah ko khud gher leta hai, taake hamara design bikhray na.
## 🧩 Snippet 3 — The Main Window
Part 3: Left Panel (Camera Feed) Setup
## 🧩 Snippet 4 — The Main Window
Part 4: Center Panel (Chat & Input Area) Setup
same code workinng snippet like left panel ke lia bnaya hmny 
**self.chat_display = QTextEdit() aur setReadOnly(True):**
ye chat cannvas pe apply horha h  QTextEdit ek chat display area ha 
QTextEdit multi-line text show aur input karne ke liye use hota hai. Humne .setReadOnly(True) kiya hai taake user khud chat history ke andar ghus kar text delete ya edit na kar sake. Yeh area sirf messages dikhane ke liye hai.
self. lagaya hai kyunki hume functions ke zariye is mein text append (add) karna padega.
**self.text_input = QLineEdit()**:
QLineEdit sirf single-line text input field ke liye hota hai (jaise search bars ya input fields hoti hain). Yahan user apna message type karega.
**returnPressed.connect()** — Enter key triggers send
**clicked.connect()** — button click triggers function
**Pseudo-classes in CSS (QPushButton:hover):**
QSS/CSS ka magical feature! Jab mouse cursor button ke upar aayega (:hover), to uska background color light blue ya light red ho jayega. Yeh application ko super-interactive responsive look deta hai.
## 🧩 Snippet 5 — The Main Window
Part 5: Right Panel (System Status) Setup
* **🧠 Logic aur Concepts Easy Steps Mein:**
setFixedWidth(250):
Left panel 350px ka tha, center panel flexible hai (jitni screen bachegi wo gher lega), aur right panel ko humne 250 pixels par fix kar diya kyunki system status dikhane ke liye itni width kaafi hai.
* **self.status_items = QLabel(...):**
Yahan humne aik hi QLabel ke andar multiline text (\n yaani new line use kar ke) daal diya hai. Iske sath self. lagaya hai kyunki aage chal kar jab hum asal modules connect karenge (jaise camera off ho to red dot ho jaye), to hum isi label ko code se update karenge!
## 🧩 Snippet 6 — The Main Window
Part 6: Chat Functions (add_message aur send_message)
Apni class ke constructor (def __init__(self):) ke baahar aur neche, yeh do functions add karo:
## 🧩 Snippet 7 — The Main Window
Last Phase: Connecting Signals (Events Binding)
### 🔗 Event Listeners / Signals Connection
        self.text_input.returnPressed.connect(self.send_message)
        send_btn.clicked.connect(self.send_message)
Jaise hi trigger hota hai, control send_message(self) function ke paas jata hai:

text = self.text_input.text().strip(): Yeh line input field (QLineEdit) ke andar ghusti hai aur .text() function ke zariye jo kuch bhi tumne type kiya hota hai, us pure text ko khinch kar bahar nikalti hai aur text naam ke variable mein save kar deti hai. .strip() aage peeche ki faltu spaces saaf kar deta hai.

self.text_input.clear(): Text fetch karne ke foran baad, yeh input field ko khali (wipe out) kar deti hai taake field dubara naye message ke liye ready ho jaye.

### 🧩 Snippet 8 — connect groq-ai to send button
get response give chunk to thread then next function
```
cursor= self.chat_display.textCursor() // cursor control
# Yahan clear() nahi karna! Bas jo naya lafz aaya hai use text box ke end mein insert karna hai
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.End) # Cursor ko text ke bilkul aakhir mein le jayein
        cursor.insertPlainText(chunk)   # Naya chunk bina line badle aage jor dein
        or
        cursor.insertHtml(f'<span style="color:#ddd; font-size: 26px;">{chunk}</span>')
        self.chat_display.setTextCursor(cursor) #Wapas cursor ko wahi set kar diya taaki agla word iske bhi aage jure.
```
### ***main streaming chunks in brain***
```
# brain.py ke andar yeh function add karein
def ask_aria_stream(user_message):
    history.append({'role': 'user', 'content': user_message})
    
    # 🌟 stream=True lagana zaroori hai
    response = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=history,
        stream=True 
    )
    
    full_reply = ""
    for chunk in response:
        # Har ek word/chunk ko extract karna
        word = chunk.choices[0].delta.content or ""
        if word:
            full_reply += word
            yield word # Naya lafz instantly worker ko bhej dena
            
    # Jab poora response aa jaye, tab history mein save karein
    history.append({'role': 'assistant', 'content': full_reply})
```
***then in gui- streaming*** 
```
# 🌟 Naya streaming function import karein
from brain import ask_aria_stream, history 

# ==================== 🛠️ FIXED WORKER CLASS ====================
class ai_writer(QThread):
    finished = pyqtSignal(str) # Har ek naya chunk GUI tak lekar jayega

    def __init__(self, user_message):
        super().__init__()
        self.message = user_message
        
    def run(self): # 🌟 Hamesha 'run' function hi use hoga background ke liye
        # brain.py ke stream function se ek-ek lafz lena aur emit karna
        for chunk in ask_aria_stream(self.message):
            self.finished.emit(chunk)
# ===============================================================
==================== 🛠️ FIXED ON_SHOW FUNCTION ====================
    def on_show(self, chunk):
        # Yahan clear() nahi karna! Bas jo naya lafz aaya hai use text box ke end mein insert karna hai
        cursor = self.chat_display.textCursor()
        cursor.movePosition(cursor.End) # Cursor ko text ke bilkul aakhir mein le jayein
        cursor.insertPlainText(chunk)   # Naya chunk bina line badle aage jor dein
        self.chat_display.setTextCursor(cursor)
    # ===================================================================
```
### 🧩 Snippet 8 — Camera Setup
```
import cv2
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage
            # convert OpenCV BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            # 4. RAM memory se data lekar PyQt5 ki QImage banayein
            qt_img = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            
            # 5. Picture ko 320x240 size mein chota karein taaki panel mein fit aaye
            qt_img = qt_img.scaled(320, 240)

            # 7. Thread ko safely band karne ka switch
    def stop(self):
        self.running = False
        self.quit()

    main window file me 
    from PyQt5.QtGui import QPixmap
    on_camera function me call hoga
     self.cam_display.setPixmap(QPixmap.fromImage(image))
     # 2. 🌟 Purane stuck frame ko saaf karke wahan simple text set kar diya!
    self.cam_display.clear()
    self.cam_display.setText("Camera is OFF")
    self.cam_display.setAlignment(Qt.AlignCenter) # Text ko center mein lane ke liye

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
            self.worker2.finished.connect(self.on_camera)
        except TypeError:
            pass  # Double connection se bachne ke liye
            
        # 2. Worker ko dobara fire karein
        self.worker2.start()
```
PyQt5 ko image screen par draw karne ke liye computer ki memory mein exact space chahiye hoti hai. Woh is formula se pata lagata hai ki: "Acha, image 640 pixels chori (w) hai aur har pixel ke paas 3 bytes (ch) ka color data hai, toh ek line mein total 640 * 3 = 1920 bytes ka data chal raha hai."
camera on and stop 
axha phly frame ana bnd kro by disconnect , phr stop phr clear kro 
on krny ke lia dosra thread na bnao start sy dosra bnta without connect,phly usko connect kro  or phr start  

🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
🧩 Snippet 1 — The Main Window
* **1. if __name__ == "__main__":** block kya hai?Yeh Python ka aik standard protocol hai jo yeh check karta hai ke kya yeh file direct run ki ja rahi hai ya kisi aur file mein import ho rahi hai.
* **app = QApplication(sys.argv):** Yeh poori application ka Engine hai. sys.argv ka matlab hai command line arguments (agar hum terminal se koi parameters pass karein). Yeh engine background mein clicks, window resizing, aur keyboard keypresses ko sunta aur handle karta hai. Iske bina GUI chal hi nahi sakti.
* **Aur sys.exit()** ka kaam yeh hai ke jab tum window ka [X] (Close) button dabao, to yeh computer ke Operating System ko clean signal bheje ke "Bhai program poora close ho chuka hai, memory khaali kar do."



# FastAPI streaming endpoint
@app.get("/chat")
async def stream_chat(message: str):
    async def generate():
        for chunk in groq_stream(message):
            yield chunk
    return StreamingResponse(generate())

// React receives stream
const response = await fetch('/chat')
const reader = response.body.getReader()
while(true) {
    const {done, value} = await reader.read()
    if(done) break
    setResponse(prev => prev + decode(value))
}