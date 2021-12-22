from flask import Flask, send_from_directory, request, jsonify, abort, abort
import requests
from pymongo import MongoClient
from secret_keys.Private_URIs import MONGO_URI
import flask_pymongo
import mongoengine
import json

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


@app.route("/echo", methods=['POST'])
def echo_page():
    content = request.json
    return jsonify(content)


@app.route("/test_json")
def test_json():
    res = requests.post('http://localhost:80/save', json={"name": 'lalala', "license_type" : '2',\
     "location" : {"type": "Point", "coordinates": [81.4471435546875, 23.61432859499169]},\
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
    content = request.json
    data = json.loads(str(content))
    try:
        add_pesticing_to_db = PesticingToDB(data["name"], data["license_type"], data["location"], \
            data["place_type"], data["pest_type"], data["pesticides_ID"], data["additional_information"])
    except ValueError:
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