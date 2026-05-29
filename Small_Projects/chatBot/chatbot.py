import random
import time

# each intent has keywords and multiple possible responses
keys = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "assalam", "salam", "sup"],
        "responses": ["Hey! What's up?", "Salam bro!", "Yo! How can I help?"]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "cya", "later", "khuda hafiz"],
        "responses": ["Take care boss!", "Khuda if!", "Later! 👋"]
    },
    "thanks": {
        "keywords": ["thanks", "thank you", "shukriya", "jazakallah"],
        "responses": ["Anytime brother!", "No problem!", "Happy to help 😊"]
    },
    "age": {
        "keywords": ["old", "age", "born"],
        "responses": ["I'm ageless — I run on Python! 🐍"]
    },
    # --- NAYE SECTIONS NEECHE HAIN ---
    "games": {
        "keywords": ["game", "gaming", "gta", "pubg", "cod", "playstation", "xbox", "pc"],
        "responses": ["GG! What are we playing today? 🎮", "Add me in your lobby! 🕹️", "PC master race or console? Let's go!"]
    },
    "guns": {
        "keywords": ["gun", "weapon", "ak47", "pistol", "rifle", "m416", "sniper", "shooting"],
        "responses": ["Locked and loaded! 🔫", "Always aim for the headshot! 🎯", "That's a powerful weapon, stay safe!"]
    },
    "movies": {
        "keywords": ["movie", "film", "cinema", "netflix", "hollywood", "bollywood", "season", "actor"],
        "responses": ["Grab the popcorn! 🍿", "Are we watching an action movie or a thriller? 🎬", "Netflix and chill mode activated! 📺"]
    },
        "goodbye": {
        "keywords": ["bye", "good to see you", "bye bye", "see you", "khuda hafiz", "cya",'exit'],
        "responses": [
            "Take care boss! Phir milte hain. 👋", 
            "Khuda Hafiz! Apna khayal rakhna. ✨", 
            "Later! Bada maza aaya baat kar ke. 😎",
            "See you soon brother! Allah hafiz. 🤝"
        ]
    }

}

memory={
    
}
def remem(key,value):
    memory[key]=value

def get_mem(key):
    return memory.get(key,None)

def user_handle(user):
    result=None
    if ('what is my name'in user or "my name" in user):
        key_value=user.split('my')[-1].strip().lower()
        print(f'the key value you enter is {key_value}')
        result=get_mem(key_value)
        if result:
            return f"Your name is {result}, I remember! 🧠"
    return None  # None means this function didn't handle it




# function for input checking
def detect_keys(user):

    for name,data in keys.items():
        for i in data['keywords']:
            # print(i)
            if i in user:
                
                return name,random.choice(data['responses'])

    return "unknown", "Hmm I didn't get that. Try again?"

def bot_res(user):
    user_input = user.lower().strip()
    if('name' in user_input or 'my name' in user_input):
        name_handle=user_handle(user_input)
        if(name_handle):
            return name_handle
    greet,res=detect_keys(user_input) 
    name = get_mem("name")
    if name and greet == "greeting":
        return f"Hey {name}! 👋 {res}"
    return res
  


print('loading...')
for i in range(40):
    print('-',end='')
    time.sleep(0.05)
print()
print("Welcome to the manual CHAT BOT!!!!")
time.sleep(2)

name=memory.get('name',None)
if(name):
    print('name available',name)
else:
    print('name is not availbe ask from user')
    name=input('Bot : what is your name?\nYou : ')
    f_name=name.split('my name is')[-1].lower().title()
    remem('name',f_name)
    print(f"Bot : Nice to meet you {f_name}! I'll remember that 😎")


while (True):
    user=input('You :  ')
    if( user in  keys['goodbye']['keywords']):
        output=bot_res(user)
        print(f'Bot : {output}')
        break
    output=bot_res(user)
    print(f'Bot : {output}')
