from flask import Flask
# from redis import Redis
import requests

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)


@app.route('/')
def index():
 #   redis.incr('hits')
    return 'Web App with Python Flask!'  # + str(redis.get('hits'), 'utf-8')


@app.route('/getNow')
def getData():
    return getData()


@app.route("/getAvg")
def getAvgData():
    data = requests.get(
        "https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10").json()
    prices = data["Data"]["Data"]
    avg = 0
    for i in prices:
        avg += i["close"]
    return "The average price of bitcoin in the last 10 minutes is: " + str(avg/10) + "$ as of now"


# This function gets the rate of bitcoin in USD as of now
# it then saves it to redis
#       key = time, value = rate
def getData():
    response = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    res = "1$ equals " + data["bpi"]["USD"]["rate"] + \
        ". updated at: " + data["time"]["updated"]
    return res


app.run(host='0.0.0.0', port=5000)
