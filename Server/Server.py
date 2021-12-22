from flask import Flask, send_from_directory, request, jsonify, abort, abort
import requests
from pymongo import MongoClient
from secret_keys.Private_URIs import MONGO_URI
import flask_pymongo
import mongoengine
import json
from pesticing import *

# Globals
app = Flask(__name__)

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = "MONGO_URI"
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
    res = requests.post('http://localhost:80/save', json={"name": "lalala", "license_type" : 2,\
     "license_number" : "1234", \
        "place_type": "Public Space", "pest_type": "cricket", "pesticides_ID" : "1234",\
            "additional_information": "abc"})
    if res.ok:
        return "Worked" + res.text
    return str(res.ok)


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")

@app.route("/save", methods=['POST'])
def save_db():
    content_as_dict = request.json
    content = json.dumps(content_as_dict)
    data = json.loads(content)
    try:
        add_pesticing_to_db = PesticingToDB(name = data["name"], license_type = data["license_type"], license_number = data["license_number"],\
            place_type = data["place_type"], pest_type = data["pest_type"], pesticides_ID = data["pesticides_ID"],\
             additional_information = data["additional_information"])
    except ValueError:
        print("Error")
        abort(400, description="invalid place type")
    add_pesticing_to_db.save()
    return jsonify(content)
    

def main():
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()