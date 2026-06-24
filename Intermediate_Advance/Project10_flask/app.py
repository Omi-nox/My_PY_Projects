import json
from datetime import datetime
from pathlib import Path
from flask import Flask , render_template , request , redirect , url_for ,flash

app=Flask(__name__) # create Flask app

app.secret_key='super_secret_key' # flassh messages key

file=Path('details.json')
def load(): # fecth data from json
    if not file.exists() or file.stat().st_size == 0:
        return []
    with open(file,'r') as f:
        f.seek(0)
        data=json.load(f)
        return data

def save_data(): # save to it
    with open(file, 'w') as f:
        json.dump(tasks, f, indent=4)

tasks=load()
print('printing outside the home',tasks)
@app.route('/') # local host 5000 home page
def home():
    print('the tasks values are',tasks)
    sz=len(tasks)
    print(sz)
    if not tasks:
        print('inside the task')
        return render_template('index.html',lent=sz,msg='  >> Please enter some task!! no task added yet')
    return render_template('index.html',lent=sz)

@app.route('/show',methods=['POST']) # SHOW PAGE
def show():
    show_req=request.form.get('show')
    sz=len(tasks)
    if not tasks:
        print('inside the task')
        return render_template('index.html',lent=sz,msg='  >> Please enter some task!! no task added yet')
    return render_template('index.html',tasks=tasks,lent=sz)

@app.route('/add',methods=['POST']) # for adding PAGE
def add_task():
    task=request.form.get('task') # the name label of attribute in html form , fetch that element
    if task and task.strip():
        tasks.append({'task':task.strip(),'time':datetime.now().strftime("%Y-%m-%d %H:%M")})
        flash("Task added successfully! CLick on the show button")
    return redirect(url_for('home'))

@app.route('/save',methods=['POST']) 
def save_data():
    with open(file, 'w') as f:
        json.dump(tasks, f, indent=4)
    return redirect(url_for('home'))   

@app.route('/delete')
def delete(): # deletion page part 2
    sz=len(tasks)
    return render_template('index.html',tasks=tasks,lent=sz)

@app.route('/delete/<int:index>',methods=['POST']) # DELETE TASK PAGE with a connection part 2
def dlt_task(index):
    print(tasks)
    if 0<= index<len(tasks):
        tasks.pop(index)
    return redirect(url_for('delete'))

if __name__=="__main__":
    app.run(debug=True)