import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():

    value = 0

    if "id" in request.args:
        value = int(request.args["id"])

    data = {
        "someValue": "goo@.com",
        "otherValue": "foo@.com",
        "budget": value
    }

    return data

app.run()