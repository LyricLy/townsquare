import flask
import json


app = flask.Flask(__name__)


@app.route("/")
def get_data():
    return flask.send_file("state.json")

@app.route("/", methods=["POST"])
def write_data():
    with open("state.json", "wb") as f:
        f.write(flask.request.get_data())
    return "", 204
