import json

import requests
from flask import Flask, send_from_directory, request, jsonify, abort
from pymongo import MongoClient
import mongoengine

import pesticing
from secret_keys.Private_URIs import MONGO_URI

# Globals
app = Flask(__name__)

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/my_db"
app.config["MONGO_CLIENT"] = MongoClient(app.config["MONGO_URI"])

IP = "0.0.0.0"
PORT = 80


@app.route("/gsap.min.js")
def gasp_js():
    return send_from_directory("../assets", "gsap.min.js")


@app.route("/echo", methods=['POST'])
def echo_page():
    content = request.json
    return jsonify(content)


@app.route("/test_json")
def test_json():
    res = requests.post('http://localhost:80/save', json={"name": "lalala",
                                                          "license_type": "2",
                                                          "place_type": "Public Space",
                                                          "pest_type": "cricket",
                                                          "pesticides_ID": "1234",
                                                          "additional_information": "abc"})
    if res.ok:
        return "Worked" + res.text
    return str(res.text)


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")


@app.route("/save", methods=['POST'])
def save_db():
    content = request.json
    try:
        add_pesticing_to_db = pesticing.PesticingToDB(content["name"], content["license_type"],
                                                      content["place_type"], content["pest_type"],
                                                      content["pesticides_ID"],
                                                      content["additional_information"])
        add_pesticing_to_db.save()
    except ValueError:
        abort(400, description="invalid place type")
    return jsonify(content)


def main():
    mongoengine.connect(host=app.config["MONGO_URI"])
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
