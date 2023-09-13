import os,sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from flask import Flask, render_template,jsonify
from routes import formHandlerBP
from utils.DataHandler import getTasks,addTask,deleteTask,updateTask,getBothTasks,analyzer
from prometheus_client import Counter, Histogram, generate_latest, REGISTRY
from rabbitmq.consume import get_message
from rabbitmq.rabbitMQ import sendMessage

app  = Flask(__name__,template_folder='../view/templates')

appRequest_counter = Counter('app_requests_total', 'Total number of requests received')
appRequest_duration = Histogram('app_request_duration_seconds', 'Request duration in seconds')
analyzeRequest_counter = Counter('analyze_requests_total', 'Total number of requests received')
analyzeRequest_duration = Histogram('analyze_request_duration_seconds', 'Request duration in seconds')

@app.route("/")
@appRequest_duration.time()
def home():
    appRequest_counter.inc()
    unfinishedTasks, completedTasks,dataLength = getBothTasks()
    totalCompletedTask = len(completedTasks)
    print(totalCompletedTask,dataLength)
    try:

        if totalCompletedTask == dataLength : 
            sendMessage()
            eventMessage = get_message()
            if(eventMessage): print("From APP",type(eventMessage),eventMessage)
    except:
        print("Rabbit MQ server isn't running ")
    return render_template('index.html',
                           toDoData=unfinishedTasks,
                           length=dataLength,
                           completedTasks=completedTasks,
                           completedLength=totalCompletedTask,
                           analyzedData = analyzer(),
                           eventMessage=eventMessage)


@app.route('/analyze')
@analyzeRequest_duration.time()
def analyzeRoute():
    analyzeRequest_counter.inc()
    return jsonify(analyzer())

@app.route('/metrics')
def metrics():
    return generate_latest(REGISTRY)

@app.route('/health')
def checkHealth():
    code = 200
    return jsonify({"status":code})
app.register_blueprint(formHandlerBP)

if __name__ == "__main__":
    app.run()    