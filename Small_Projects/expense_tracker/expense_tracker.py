import json
from datetime import datetime
from pathlib import Path
import time

fp=Path('Small_Projects/expense_tracker')

File=fp/'expenses.json' #  file path in existing current folder
current_dir = Path.cwd() 
print(current_dir)  ## current directory fetching


def load(): # reading data
    if not File.exists():
        print('file not exist , for creation add something!!')
        return [] # to inform , no data loaded yet and return list
    with open(fp/'expenses.json' ,'r') as f:
        f.seek(0)
        data=json.load(f)
        return data 
    
def save(new_expens): # saving which gonna done automatically
    with open(fp/'expenses.json' ,'w') as f:
        json.dump(new_expens,f,indent=4)

def add(expens_data): # for adition
    print('\n-------- ADD EXPENSES---------\n')
    des= input("Description (e.g. lunch, petrol): ").strip()
    category = input("Category (food/transport/shopping/other): ").strip().lower()
      
    try:
        amount = float(input("Amount (Rs): ").strip())
    except ValueError:
        print("Invalid amount!")
        return

    expenses = {
        "desc"    : des,
        "category": category,
        "amount"  : amount,
        "date"    : datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    expens_data.append(expenses) # append with previously loaded data from expenses_file
    save(expens_data)
    print(f" Expense added: {des} — Rs {amount}")

def view(expenses_file):  # for viewing data
    if not expenses_file:
        print("\n📭 No expenses yet!")
        return
    print(f"\n{'='*80}")
    print(f"{'#':<4} {'Description':<20} {'Category':<12} {'Amount':>8}  {'Date':>12}")
    print(f"{'='*80}")
    total = 0
    for i, e in enumerate(expenses_file, start=1):
        print(f"{i:<4} {e['desc']:<20} {e['category']:<12} Rs{e['amount']:>7.0f}  {e['date']:>20}")
        total += e['amount']
    print(f"{'='*80}")
    print(f"{'TOTAL':>36} Rs{total:>7.0f}")
    print(f"{'='*80}\n")

def deletion(exp):
    data=view(exp)
    print('which one expense you want to delete!!!......')
    i=int(input('enter number  '))
    print(f'the item you access  that is :  \n {exp[i-1]}\n')
    del exp[i-1]
    print(exp,'\ndeletion successful')
    save(exp)

def file_deletion():
    if not (File.exists()):
        print('\nfile does not exist!!!!\n')
    else:
        Path(fp/'expenses.json').unlink()
        print('file deleted successfully!!')

def filter(exp):
    cat=input('enter category  that must be matched  ')
    sz=len(exp)
    print(f"\n{'='*80}")
    print(f"{'#':<4} {'Description':<20} {'Category':<12} {'Amount':>8}  {'Date':>12}")
    print(f"{'='*80}")
    total = 0
    for i, e in enumerate(exp, start=1):
        if(cat==exp[i-1]['category']):
            print(f"{i:<4} {exp[i-1]['desc']:<20} {exp[i-1]['category']:<12} Rs{exp[i-1]['amount']:>7.0f}  {exp[i-1]['date']:>20}")
            total += exp[i-1]['amount']
    print(f"{'='*80}")
    print(f"{'TOTAL':>36} Rs{total:>7.0f}")
    print(f"{'='*80}\n")


def show_menu():
    print('---------------------')
    print("Expense Tracker APP  |")
    print("1 - View  Expenses   |")
    print("2 - Add Expenses     |")
    print("3 - Delete Expenses  |")
    print("4 - Filter Category  |")
    print("5 - Delete File      |")
    print("6 - Quit             |")
    print('---------------------')
    choice=(input('\nEnter choice\n')).strip() # direct int krny sy wo empty ko handle nhi krtpa or value error deta hs isliya phle str then int
    # print(type(choice))
    if not choice:
        raise KeyboardInterrupt("\napp message : No input provided or being left epmty\n")
    
    return int(choice)

# starting main work from here

print('loading...')
for i in range(40):
    print('-',end='')
    time.sleep(0.05)
print()
print("Welcome to the Expense Tracker APP!!!!")
time.sleep(2)

expenses_file = load()

while True:
    try:
        chc=show_menu()
        match chc:
            case 1:
    
                view(expenses_file)
            case 2:
           
                add(expenses_file)
            case 3:
                deletion(expenses_file)
            case 4:
                filter(expenses_file)
            case 5:
                file_deletion()
            case 6:
                print('good to see you , Bye!!!')
                break
            case _:
                print("Unknown status : enter NUMBER (1-5) can be accepted")
    except KeyboardInterrupt as e:
        print(e)
    except ValueError as e:
        print(e,"\nApp Error: enter NUMBER (1-5) can be accepted, ABC or string lietral not worked!\n")




