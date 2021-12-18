from flask import Flask, send_from_directory
from pymongo import MongoClient
from secret_keys.Private_URIs import MONGO_URI
import flask_pymongo
import mongoengine

# Globals
app = Flask(__name__)

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = MONGO_URI
app.config["MONGO_CLIENT"] = MongoClient(app.config["MONGO_URI"])

IP = "0.0.0.0"
PORT = 80


@app.route("/gsap.min.js")
def gasp_js():
    return send_from_directory("../assets", "gsap.min.js")


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")


def main():
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
