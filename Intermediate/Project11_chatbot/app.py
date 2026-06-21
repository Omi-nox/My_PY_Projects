from groq import Groq
from dotenv import load_dotenv
from flask import Flask, render_template , request , redirect , url_for , flash
import os

load_dotenv() # reads .env file

client=Groq(api_key=os.getenv('GROQ_API_KEY'))
history=[ {"role": "system", "content": "You are a helpful assistant named ARIA. You are friendly, smart and concise. You were built by Umar using Python and Groq API."}
]

def ask_ai(user_message):
    history.append({'role':'user','content':user_message})
    response= client.chat.completions.create( # send messages to real ai model
        model='llama-3.1-8b-instant',
         messages=history       ) # send full chat history every time
    reply=response.choices[0].message.content
    history.append({'role':'assistant','content':reply})
    print(reply)
    return reply

# test conversation memory
# print("ARIA:", ask_ai("My name is Umar and I love PC gaming."))
# print("ARIA:", ask_ai("What is my name and what do I love?"))

# BACKEND SETUP 
app=Flask(__name__)
app.secret_key='super_secret_key'

@app.route('/')
def home():
    # filter out system message for display
    display = [m for m in history if m["role"] != "system"]
    return render_template('index.html',history=display)

@app.route('/chat',methods=['POST'])
def chat():
    msg=request.form.get('message')
    ask_ai(msg)
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True)