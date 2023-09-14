from flask import request, Blueprint,redirect
from utils.DataHandler import addTask,deleteTask,updateTask
formHandlerBP = Blueprint('add_todo', __name__)


@formHandlerBP.route('/addTask', methods=['POST'])
def addTodoHandler():
    if request.method == 'POST':
        task = request.form.get('task')
        if task != '':
            addTask({task:False})
        return redirect('/')
    
@formHandlerBP.route('/update',methods=['POST'])
def update():
    if request.method == "POST":
        task = request.form.get('task')
        print("Here")
        print(task)
        updateTask(task)
        return redirect('/')
        
