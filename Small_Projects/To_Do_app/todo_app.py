# later jb ayi exception handle krli iski
#file opening with path
from pathlib import Path
folder=Path('To_Do_app')
my_path = folder/"report.txt"
task_no=1

def inputting():
    global task_no
    task=input(f'\n{task_no} enter task  \n')
    return task

def read_file():
    global task_no
    if not (my_path.exists()):
        print(f"\nno tasks file  created or added something!\n")
    elif (my_path.exists()):    
        with open(folder/'report.txt','r') as f:
            data=f.read().split('.')   
         
            if not data:
                print("\nNo tasks yet!")
            else:
                # print('we are well and done',data)
                for i in range(0,len(data),2):  
                    
                    # print(data[i])
                    num=data[i].strip()
                    # print('numbers',num)
                    if num.isdigit():
                        # print('it is fucking good',type(num))
                        n1=int(num)
                        # print(type(n1))
                        task_no=n1                 
    print(f'final last task no is  {task_no}')

def deleting():
    new_data=None
    choice=(input('\nenter task no for deleting\n')) 
    if (my_path.exists()):
        with open(folder/'report.txt','r') as f:
            data=f.read().splitlines() # break those lines who have \n
            # print(data)
            # print('\n')
            # print('now print that fucking data')
            # print(data)
            for i in data:
                if  i.startswith(choice + "."):
                    data.remove(i)
                    print('\n Task deleted Successfully!!!! \n')
                    # print(data)
                    new_str=None
                    for i in data:
                        # print(i)
                        new_str='\n'.join(data)
                    t=True
                    break
                 
                else:
                    t=False
            if t:
                
                # print('split scene enter hogya ha ')
                new_data=new_str.split('.') # facing problem that it add number with previous text and \n so i have to put . again at the end of text 
                # print(new_data)
                new_list_data=[]
                for i in range(1,len(new_data),2):
                   new_list_data.append(new_data[i])
                   
                # print(f'final new data list \n {new_list_data}')
                #writing again with same index and the same data
                with open(folder/'report.txt','w') as f:
                    no=1
                    for i in range(0,len(new_list_data)):
                        f.write(f'{str(no)}. {new_list_data[i]}.\n')
                        no+=1
            else:
                print('\nnothing to delete or task already deleted\n')
            print('\n')
    else:
        print('\nfiles not found sorry \n')        

def adding_appending():
    global task_no
    read_file()
    task_no+=1
    if (my_path.exists()):
        print(f'appending method called and task_no is {task_no}')
        tsk=inputting()
        with open(folder/'report.txt','a') as f:
            f.write(f'{str(task_no)}. {tsk}.\n')
def file_deletion():
    if not (my_path.exists()):
        print('\nfile does not exist!!!!\n')
    else:
        Path(folder/'report.txt').unlink()

def adding():
    global task_no
    if not (my_path.exists()):
        tks=inputting()
        with open(folder/'report.txt','w') as f:
            print('\ntask added successfully......\n')
            f.write(f'{str(task_no)}. {tks}.\n')
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
    # read_file()
    if (my_path.exists()):
        with open(folder/'report.txt','r') as f:
            data=f.read().splitlines()
            # print(data)
            print('\n')
            for i in data:
                print(i)
            print('\n')
    else:
        print('\nfiles not found for view ,sorry \n')


def show_menu():
    print("TO-DO LIST APP")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Delete task")
    print("4 - Delete File")
    print("5 - Quit")
    choice=(input('\nEnter choice\n')).strip() # direct int krny sy wo empty ko handle nhi krtpa or value error deta hs isliya phle str then int
    # print(type(choice))
    if not choice:
        raise KeyboardInterrupt("\napp message : No input provided or being left epmty\n")
    
    return int(choice)
   
# # # 
# show_menu()
# file_checking()
# view()
read_file()
while True:
    try:
        chc=show_menu()
        match chc:
            case 1:
    
                view()
            case 2:
           
                adding()
            case 3:
                deleting()
            case 4:
                file_deletion()
            case 5:
                print('good to see you , Bye!!!')
                break
            case _:
                print("Unknown status : enter NUMBER (1-5) can be accepted")
    except KeyboardInterrupt as e:
        print(e)
    except ValueError as e:
        print(e,"\nApp Error: enter NUMBER (1-5) can be accepted, ABC or string lietral not worked!\n")

