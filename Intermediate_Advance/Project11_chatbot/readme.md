# 🤖 ARIA - AI Chatbot with Conversation Memory

ARIA is an intelligent, context-aware AI chatbot built using **Flask (Python)** and the **Groq Cloud API** powering the `llama-3.1-8b-instant` model. The chatbot maintains a persistent conversation history, allowing it to remember past interactions within the session.

---

## ✨ Features

- **Context-Aware Memory**: The chatbot retains full conversation history to remember user details (e.g., names, preferences) across multiple turns.
- **Custom System Identity**: Pre-configured with a system prompt defining the AI's persona as **ARIA**, a friendly and concise assistant built by **Umar**.
- **Smart UI Message Filtering**: Employs a server-side list comprehension filter to strip away background system instructions, ensuring users only see clean user/assistant chat logs on the frontend.
- **Blazing Fast Performance**: Powered by Groq's LPU inference engine for near-instantaneous AI responses.

---

## 🛠️ Project Structure

Your project directory should look like this:

```text
Project11_chatbot/
│
├── app.py               # Main Python Flask backend application
├── .env                 # Environment file for storing the Groq API key (gitignored)
├── README.md            # Project documentation (This file)
└── templates/
    └── index.html       # Frontend HTML template for the chat interface
```

---

## 🚀 Setup & Installation

Follow these steps to set up and run the application on your local machine:

### 1. Clone or Open the Project
Navigate into your project directory using your terminal or favorite IDE (like VS Code):
```bash
cd Project11_chatbot
```

### 2. Install Dependencies
Install the required packages using `pip`:
```bash
pip install flask groq python-dotenv
```

### 3. Configure the Environment Variables
Create a file named **`.env`** in the root directory of your project. Add your Groq API key into it:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```
*(Note: Do not commit your `.env` file to GitHub for security reasons. Add `.env` to a `.gitignore` file).*

### 4. Run the Application
Start the Flask development server:
```bash
python app.py
```

Once running, open your web browser and navigate to **`http://127.0.0.1:5000`** to chat with ARIA.

---

## ⚙️ Code Architecture & Workflow

1. **State Management (`history`)**: The application uses a global list to store the sequence of dictionaries containing chat roles (`system`, `user`, `assistant`) and their text content.
2. **Backend Engine (`ask_ai`)**: Appends the new user prompt to the chat history, sends the entire structural payload to Groq's completions endpoint, extracts the text string, and appends the assistant's reply back to the array.
3. **Data Security & Presentation Filter**: In the `/` home route, a list comprehension `[m for m in history if m["role"] != "system"]` isolates the background system identity matrix from the list. This prevents system configurations from appearing as messages inside the chat canvas container.

---

## 👨‍💻 Author
Developed with ❤️ by **Umar** using Python, Flask, and Groq API.
