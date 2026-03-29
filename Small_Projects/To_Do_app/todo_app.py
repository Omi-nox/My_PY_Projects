#file opening with path
from pathlib import Path
folder=Path('To_Do_app')
my_path = folder/"report.txt"
task_no=1

def inputting():
    global task_no
    task=input(f'{task_no} enter task  ')
    return task

def read_file():
    global task_no
    if not (my_path.exists()):
        print(f"\nno tasks file  created or added something!")
    elif (my_path.exists()):    
        with open(folder/'report.txt','r') as f:
            data=f.read().split('.')   
        if not data:
            print("\nNo tasks yet!")
        else:
            print('we are well and done')
            task_no=int(data[0])
           

def adding_appending():
    global task_no
    if (my_path.exists()):
        tsk=inputting()
        with open(folder/'report.txt','a') as f:
            f.write(f'{str(task_no)}. {tsk}\n')
            task_no+=1

def adding():
    global task_no
    if not (my_path.exists()):
        tks=inputting()
        with open(folder/'report.txt','w') as f:
            f.write(f'{str(task_no)}. {tks}\n')
        print('task added successfully......')
        task_no+=1
    else:
      adding_appending()
        
        




# def file_checking(): # file checking
#     if (my_path.exists()):
#         print('we are good , we got the folder')
#         adding_appending()
#         # Path(folder/'report.txt').unlink()
#     else:
#         print('no, there is no such kind folder that and so i created it ')
#         adding_appending()

def view():  #viewinf file content
    if (my_path.exists()):
        with open(folder/'report.txt','r') as f:
            data=f.read().splitlines()
           
            print('\n')
            for i in data:
                print(i)
            print('\n')
    else:
        print('files not found sorry ')


def show_menu():
    print("TO-DO LIST APP")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("4 - Quit")
    choice=int(input('Enter choice'))
    match choice:
        case 1:
           print('this is case 1 ')
           view()
        case 2:
           print('this is case 2')
           adding()
        case 3:
            pass
        case 4:
            pass
        case _:
            return "Unknown status"
# # Path(folder/'report.txt').unlink()
# show_menu()
# file_checking()
# view()
read_file()
while True:
    show_menu()

