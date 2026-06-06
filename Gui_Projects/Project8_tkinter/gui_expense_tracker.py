import tkinter as tk
import json
from pathlib import Path
from datetime import datetime
import os

fp=Path('Gui_Projects/Project8_tkinter')
file=fp/'expense_tracker.json' #  file path in existing current folder
def load(): # reading data from the file
    if not file.exists() or file.stat().st_size==0:
        print('file not exist , for creation add something!!')
        return [] # to inform , no data loaded yet and return list
    with open(file, 'r') as f:
        f.seek(0)
        data=json.load(f)
        return data 
    
def save(new_expens): # saving which gonna done automatically
    with open(file, 'w') as f:
        json.dump(new_expens,f,indent=4)
    
# create the main window
root=tk.Tk()
root.title('Expense Tracker')
root.geometry('600x400') # width x height in pixels
root.resizable(False,False) # lock window size
root.configure(bg="#1e1e1e") 

# label display text 
title_label=tk.Label(
    root,text='💰 Expense Tracker',
    font=('Arial',20,'bold')
)
title_label.pack(pady=20)

#  frame like small window inside main window to hold input fields
frame_inp=tk.Frame(root,padx=20,pady=10)
frame_inp.pack()
# description label
tk.Label(frame_inp,text='Description:',font=('Arial',12),bg="#1e1e1e", fg="white").grid(row=0,column=0,sticky='e',)
entry_desc=tk.Entry(frame_inp,font=('Arial',9),width=30)
entry_desc.grid(row=0,column=1,padx=10,pady=5)

# Category field
tk.Label(frame_inp, text="Category:", font=("Arial", 11),bg="#1e1e1e", fg="white").grid(row=1, column=0, padx=10, pady=5, sticky="e",)
entry_cat = tk.Entry(frame_inp, width=25, font=("Arial", 9))
entry_cat.grid(row=1, column=1, padx=10, pady=5)

# Amount field
tk.Label(frame_inp, text="Amount (Rs):", font=("Arial", 9),bg="#1e1e1e", fg="white").grid(row=2, column=0, padx=10, pady=5, sticky="e",)
entry_amount = tk.Entry(frame_inp, width=25, font=("Arial", 11))
entry_amount.grid(row=2, column=1, padx=10, pady=5)

# table frame to hold table of expenses
frame_table=tk.Frame(root,padx=20,pady=10)
frame_table.pack()

# table headers
total=0
headers = ["#", "Description", "Category", "Amount", "Date"]
# label at bottom showing total
total_label = tk.Label(root, text="Total: Rs 0", font=("Arial", 12, "bold"),bg="#1e1e1e", fg="white")
total_label.pack(pady=5)



def refresh_table():
    # clear old rows first
    for widget in frame_table.winfo_children():
        widget.grid_forget()   
    for col, header in enumerate(headers):
        tk.Label(frame_table, text=header, font=("Arial", 10, "bold"),
             borderwidth=1, relief="solid", width=14, bg="#333", fg="white"
    ).grid(row=0, column=col, sticky="nsew")
    values=load()
    total = 0
    for i,e in enumerate(values,start=1):
        print(values)
        val=[i,e['desc'],e['category'],f"Rs {e['amount']:.2f}",e['date']]
        for j,v in enumerate(val):
            tk.Label(frame_table, text=v, font=("Arial", 10, "bold"),
                     borderwidth=1, relief="solid", width=13).grid(row=i, column=j, sticky="nsew")
        total +=e['amount']
    total_label.config(text=f"Total: Rs {total:.2f}")





def add_expense():
    desc   = entry_desc.get().strip()
    cat    = entry_cat.get().strip()
    amount = entry_amount.get().strip()
    print(f"DESC: {desc} | CAT: {cat} | AMOUNT: {amount}")

    if not desc or not cat or not amount:
        print("Fill all fields!")
        return
    
    expenses = load()
    expenses.append({
        "desc": desc, "category": cat,
        "amount": float(amount),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save(expenses)
    
  
    
    # clear fields after adding
    entry_desc.delete(0, tk.END)
    entry_cat.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    refresh_table()

def show_exp():
    refresh_table()


def delete_last():
    expenses=load()
    if expenses:
        expenses.pop()
        save(expenses)
        refresh_table()
        
btn_show=tk.Button(frame_inp, text="📋 show expenses", font=("Arial", 11), bg="#5ca1e6",            # Light Blue color
    fg="white", activebackground="#4a8cc7", # Click hone par thoda dark blue
    relief="flat",           # Borderline ko clean aur flat rakhne ke liye
    cursor="hand2", command=show_exp)
btn_show.grid(row=3, column=0, columnspan=1, pady=10 )

btn_add = tk.Button(frame_inp, text="➕ Add Expense", font=("Arial", 11), bg="#2ed573",            # Beautiful Green color
    fg="white",activebackground="#26af5f", 
    relief="flat",
    cursor="hand2", command=add_expense)
btn_add.grid(row=3, column=1, columnspan=2, pady=10)

btn_delete = tk.Button(frame_inp, text='Delete last item', font=('Arial', 11), bg="#ff4757",            # Soft Crimson Red color
    fg="white",activebackground="#e03d4b", 
    relief="flat",
    cursor="hand2", command=delete_last)
btn_delete.grid(row=3, column=4, columnspan=2, pady=10)

# start the window — this line keeps window open
root.mainloop()
