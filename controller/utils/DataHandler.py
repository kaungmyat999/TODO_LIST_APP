import sys,os 

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandParent = os.path.dirname(parent)
sys.path.append(grandParent)
print(grandParent)
print(sys.path)
from model.db import DB



def getCollection(DBName='Users',collection='tasks'):
    db = DB(DBName,collection)
    collection = db.getCollection()
    return collection

collection = getCollection()

def getTasks():
    collection = getCollection()
    for data in collection.find():
        print(data)
        return data['tasks']
        

def updator(InputData,collection=collection):
    for data in collection.find():
        collection.update_one(
            {'_id': data['_id']},
            {'$set': {'tasks':InputData}}
        )

def addTask(newTask):
    data = getTasks()
    print("Here in add Task")
    
    data.update(newTask)
    updator(data)


#Updating
def updateTask(taskName):
    data = getTasks()
    print('updateTask')
    if taskName in data:
        print("Task Name")
        print(data[taskName])
        data[taskName] = not data[taskName]
    updator(data)

##Deleting
def deleteTask(taskName):
    data = getTasks()
    if taskName in data:
        del data[taskName]
    
    updator(data)

def getBothTasks():
    data = getTasks()
    unfinishedTasks = []; completedTasks = []
    for key,value in data.items():
        if value:
            completedTasks.append(key)
            
        else:
            unfinishedTasks.append(key)

    return [unfinishedTasks,completedTasks,len(data)]

def percentageCalculator(completedTasks, TotalTasks):
    if(TotalTasks > 0):
        return round((completedTasks/TotalTasks)*100,2)

def analyzer():
    unfinishedTasks, completedTasks, TotalTasks = getBothTasks()
    finishedPercentage = percentageCalculator(len(completedTasks),TotalTasks)
    return {'Total_Tasks':TotalTasks,"Finished_Tasks":finishedPercentage}
    
