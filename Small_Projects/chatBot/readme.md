# 🤖 Smart Custom Rule-Based Chatbot

A Python-based smart chatbot that remembers the user's name, detects conversational intents using nested loops, and responds dynamically based on predefined keywords.

## 🚀 Features

* **Contextual Memory**: Remembers the user's name throughout the session using a memory management system.
* **Name Extraction**: Uses advanced string manipulation (`.split()`, `.strip()`, `.title()`) to seamlessly extract and clean names from inputs like *"my name is Umar Khan"*.
* **Intent Detection**: Employs a robust nested loop architecture over structured dictionary data (`intents.items()`) for accurate keyword matching.
* **Fallback Protocol**: Features a safe dictionary handling system via `.get()` to prevent runtime errors and includes an unknown intent fallback handler.
* **Diverse Topics**: Pre-configured categories covering Greetings, Farewells, Thanks, Games, Guns, and Movies with fun emoji responses.

---

## 🛠️ Code Architecture Explained

### 1. The Nested Loop Core
The bot scans user input using a secure two-tier nested loop that avoids `KeyError` exceptions by iterating efficiently:
```python
for intent, data in intents.items():
    for keyword in data["keywords"]:
        if keyword in user_input:
            return intent, random.choice(data["responses"])
```

### 2. Name Extraction Logic
Extracts the name dynamically by splitting the target trigger phrase, selecting the trailing slice, removing whitespace, and capitalizing the first letters:
```python
name = user_input.split("my name is")[-1].strip().title()
```

### 3. Safe Memory Lookup
Utilizes Python’s built-in `.get()` method to safely fetch data from volatile session memory without crashing:
```python
return memory.get(key, None)
```

---

## 🎮 Sample Conversation Log

```text
Welcome to the manual CHAT BOT!!!!
name is not available, ask from user
Bot : what is your name?
You : my name is umar khan
Bot : Nice to meet you Umar Khan! I'll remember that 😎
You : what about gun
Bot : Locked and loaded! 🔫
You : what is my name
Bot : Your name is Umar Khan, I remember! 🧠
You : see you
Bot : goodbye! Apna khayal rakhna. ✨
```

---

## 📦 How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory:
   ```bash
   cd My_PY_Projects
   ```
3. Run the Python script:
   ```bash
   python chatbot.py
   ```

---

## 📝 Technologies Used
* **Language**: Python 3.x
* **Core Modules**: `random`
* **Concepts**: Nested loops, Dictionary Views (`.items()`), String Slicing (`[-1]`), Error mitigation (`.get()`).
