import string
import random

def pass_gen(lenght):
     l=lenght
     # print(f'type of type( {type(l)})')
     letter=string.ascii_letters
     # print(f'type of {type(letter)} and {letter[:27]}')
     number=string.digits
     # print(f'\n type of numbers {type(number)} and {number[:10]}')
     symbols=string.punctuation
     # print(f'\n type of symbols {type(symbols)} and {symbols[:5]}')

     all_chars=letter+number+symbols
     # print(all_chars)

     password=[]
     password.append(random.choice(letter))
     password.append(random.choice(number))
     password.append(random.choice(symbols))
     for i in range(l-3):
          password.append(random.choice(all_chars))
          # print(password)

     # print(f'pass word before shuffling {password}')
     random.shuffle(password)
     com_pass=''.join(password)
     return com_pass

def no_pass_gen(counter,lenght):
     c=counter
     l=lenght
     no_pass=[]
     for i in range(c):
          m=pass_gen(l)
          # print(f'your complete password has been generated ===  {m} \n ')
          no_pass.append(m)
     # no_pass.append(com_pass)
     return no_pass

# p=no_pass_gen(3)
# print(p)

def inputt():
     length=(input('enter password length 1-8 for generation : \n'))
     if not length.strip():
          raise KeyboardInterrupt('cant be left empty or enter something please ,bakhchodi sy gurez kry')
    
     return int(length)



def counter():
     c=input('how many password you wanna generate\n')
     return int(c)
def working():
     try:
          ch=inputt()
          if ch<8:
               ch=8
               print('your password lenght was less than 8 , so it got set-up automatically to 8')
          c=counter() 
          p=no_pass_gen(c,ch)
          print('=============no of pass generated=============')
          for i, tasks in enumerate(p, start=1):
               print(f" {i}. {tasks}")


     except Exception as e:
       print(e)



print('Welcome to the CLI-BASED password generator app')
ch=int(input('enter 0 to start \n'))
while True:
     if ch==0:
          working()
          ch=1
     elif ch==1:
          option=input('wana create again yes/no')
          match option:
               case 'yes':
                    working()
               case 'no':
                    print(" Stay secure boss! bye")
                    break
     


