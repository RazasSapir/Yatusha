from flask import Flask, send_from_directory, request, jsonify, abort, abort
import requests
from pymongo import MongoClient
from secret_keys.Private_URIs import MONGO_URI
import flask_pymongo
import mongoengine
import json
from pesticing import *
from bson.objectid import ObjectId


# Globals
app = Flask(__name__)

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = "MONGO_URI"
app.config["MONGO_CLIENT"] = MongoClient(app.config["MONGO_URI"])

IP = "127.0.0.1"
PORT = 80
MONGO_DB_PORT = 27017
POST_TEST_URL = "http://localhost:80/update/61c4376fae925beab16149b7"

mongoengine.connect(host = IP, port = MONGO_DB_PORT)
client = MongoClient(IP, MONGO_DB_PORT)

@app.route("/gsap.min.js")
def gasp_js():
    return send_from_directory("../assets", "gsap.min.js")


@app.route("/echo", methods=['POST'])
def echo_page():
    content = request.json
    return jsonify(content)


@app.route("/test_json")
def test_json():
    data = {"name": "lalala", "license_type" : 2,
     "license_number" : "1234", 
        "place_type": "Public Space", "pest_type": "cricket", "pesticides_ID" : "1234",
            "additional_information": "abc"}
    res = requests.post(POST_TEST_URL, json=data)
    if res.ok:
        return "Worked" + res.text
    return str(res.ok)


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")

@app.route("/save", methods=['POST'])
def save_db():
    data = request.json
    try:
        add_pesticing_to_db = PesticingToDB(name = data['name'], license_type = data['license_type'], license_number = data['license_number'],\
            place_type = data['place_type'], pest_type = data['pest_type'], pesticides_ID = data['pesticides_ID'],\
             additional_information = data['additional_information'])
    except ValueError:
        abort(400, description="invalid input")
    add_pesticing_to_db.save()
    return jsonify(data)

@app.route("/update/<query_id>", methods=['POST'])
def update_db(query_id):
    data = request.json
    try:
        obj_to_update_in_db = "additional_information"
        obj_to_put_in_db = "additional_information"
        Update_and_delete.update_DB(obj_to_change=obj_to_update_in_db, \
                                    obj_to_put=obj_to_put_in_db, \
                                    obj_id=query_id)
    except ValueError:
        abort(400, description="invalid update")

    return jsonify(data)
    

def main():
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()