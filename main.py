import flask
from flask import request
import datetime as dt
from functions import calculate_loan


app = flask.Flask(__name__)
app.config["DEBUG"] = True




@app.route('/', methods=['GET'])
def loan():

    budget = 0

    if "budget" in request.args:
        budget = int(request.args["budget"])
    
    result = calculate_loan(budget)

    data = {
        "result": result
    }

    return data

app.run()