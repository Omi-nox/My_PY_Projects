from groq import Groq
from dotenv import load_dotenv

import os

load_dotenv()

client=Groq(api_key=os.getenv('Groq_Api'))
history = [
    {"role": "system", "content": """You are ARIA, an advanced AI OS assistant built by Umar Asghar.
    
STRICT RULES:
- Keep responses SHORT — maximum 2-3 sentences
- Speak naturally like a human assistant
- Only give detailed explanation if user specifically says "explain" or "detail"
- If user asks a simple question — give simple direct answer
- Never repeat yourself
- Never add unnecessary context"""}
]

def ask_aria(user_message):
    history.append({'role': 'user', 'content': user_message})
    response = client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=history,
        max_tokens=100,      # ← strict limit
        temperature=0.5,     # ← less creative = less hallucination
        stream=True
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta

def ask_aria(user_message):
    history.append({'role':'user','content':user_message})
    response= client.chat.completions.create(
        model='llama-3.1-8b-instant',
        messages=history,
        stream=True
    )
    ai_reply=''
    for i in response:
        word= i.choices[0].delta.content or ""
        if word:
            ai_reply+=word
            print(word)
            yield word
  
    history.append({'role':'assistant','content':ai_reply})
   

# - NO bullet points, NO markdown, NO lists