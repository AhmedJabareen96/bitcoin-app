from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def index():
    redis.incr('hits')
    return 'Web App with Python Flask!' + str(redis.get('hits'), 'utf-8')

@app.route('/get')
def getData():
    return "get updated data"

@app.route("/getAvg")
def getAvgData():
    return "get avg data"

app.run(host='0.0.0.0', port=5000)
