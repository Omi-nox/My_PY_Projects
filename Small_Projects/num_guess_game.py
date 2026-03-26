import random
import time

def starting():
    start_now=time.time()
    formatted=time.strftime('%H:%M') # 24 hour format 
    print('game started at >>>: ',formatted)
    return start_now

def ending(time_end):
  end=time.time()
  diff=end-time_end
  left_time=time.strftime('%H:%M')
  print(f'total time game played > {diff:.2f}  seconds')
  print(f'exit time >>>:  {left_time}')

def diff_lvl():
    print("\nChoose difficulty:\n")
    print("1 - Easy   (10 guesses)\n")
    print("2 - Medium (5 guesses)\n")
    print("3 - Hard   (3 guesses)\n")
    choice = input("Enter 1 / 2 / 3: ").strip()
    if choice == "1":
        return 10
    elif choice == "3":
        return 3
    else:
        return 5  # default to medium for any other input
def guess_game(df_l):
    time_end=starting()
    l=df_l
    try:
        user_name=str(input('enter your name\n'))
    except KeyboardInterrupt as e:
        print(e)
        l=0
    print(f"WELCOME TO COMPUTER GUESSING GAME , YOU HAVE TOTAL {l} GUESSES ,SO CHOOSE WISELY\n")
    num=random.randint(1,100)
   
    while l>0:
        try:
            user=int(input('enter the number own your guess\n'))
        except ValueError as e:
            print(f"invalid input try again , {e}\n")
        l=l-1
        if(user==num):
            print(f'congratulatoin\'s!!! {user_name} you guess the correct number , you WON a game\n')
            break
        elif(user>num and l>0):
            print(f'number too much greater, guess wisely!!!!!, you have {l} guesses left ')
        elif(user<num and l>0):
           print(f"guess again,the number is small,  you have {l} guesses left ")
        else:
            print(f'you have {l} guesses left , you lose the game\n ')
    ending(time_end)

ch=0
df_l=diff_lvl()
while True:
  if(ch==0): # if game starting first time
    guess_game(df_l)
    ch=1
  elif(ch==1):
    choice=input('wana play again : yes/no\n')
    if(choice=='yes'):
       df_l=diff_lvl()
       guess_game(df_l)
    else:
        print('thanks for playing with me  boss!!!')
        break
