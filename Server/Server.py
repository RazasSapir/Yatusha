from flask import Flask, send_from_directory, request, jsonify, abort, abort
import requests
import mongoengine
import json
from pesticing import *
from pesticides import *
from bson.objectid import ObjectId
import http

# Globals
app = Flask(__name__)

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = "MONGO_URI"
app.config["MONGO_CLIENT"] = MongoClient(app.config["MONGO_URI"])

IP = "127.0.0.1"
PORT = 80
MONGO_DB_PORT = 27017
POST_TEST_URL = "http://localhost:80/delete/{obj_id}".format(obj_id=ObjectId("61c4fe681a3e3f61c3acb979"))

disconnect()
mongoengine.connect(host=IP, port=MONGO_DB_PORT)
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
    # location = nominatim(user_agent="GetLoc")
    data = {"name": "lalala", "license_type": 2,
            "license_number": "1234",
            "place_type": "Public Space", "pest_type": "cricket", "pesticides_ID": "1234",
            "additional_information": "abc"}  # , "location": {"type": "Point", "coordinates": [location.latitude, location.longitude]}}
    res = requests.post(POST_TEST_URL, json=data)
    if res.status_code == 204:
        return "No content"

    elif res.ok:
        return "Worked" + res.text
    return str(res.ok)


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")


@app.route("/save", methods=['POST'])
def save_db():
    data = request.json
    try:
        add_pesticing_to_db = PesticingToDB(name=data['name'], license_type=data['license_type'],
                                            license_number=data['license_number'], \
                                            place_type=data['place_type'], pest_type=data['pest_type'],
                                            pesticides_ID=data['pesticides_ID'], \
                                            additional_information=data['additional_information'])
    except ValueError:
        abort(400, description="invalid input")
    add_pesticing_to_db.save()
    return jsonify(data)


@app.route("/update/<query_id>", methods=['POST'])
def update_db(query_id):
    try:
        obj_to_update_in_db = "additional_information"
        obj_to_put_in_db = "additional_information"
        query = Update_and_delete.update_DB(obj_to_change=obj_to_update_in_db, \
                                            obj_to_put=obj_to_put_in_db, \
                                            obj_id=query_id)
        temp_query = query
        fixed_query = temp_query.pop('_id', None)
        query_as_str = json.dumps(fixed_query)
        query_as_json = json.loads(query_as_str)
    except ValueError:
        abort(400, description="invalid update")

    return jsonify(query_as_json)


@app.route('/delete/<query_id>', methods=['POST'])
def delete(query_id):
    try:
        query = Update_and_delete.delete_DB(obj_id=query_id)
        temp_query = query
        query_as_json = None
        if temp_query is not None:
            fixed_query = temp_query.pop('_id', None)
            query_as_str = json.dumps(temp_query)
            query_as_json = json.loads(query_as_str)
        else:
            return '', http.HTTPStatus.NO_CONTENT
    except ValueError:
        abort(400, description="invalid delete")

    return jsonify(query_as_json)


@app.route("/pesticides/<pesticide_id>")
def get_pesticide(pesticide_id):
    try:
        pesticide = get_pesticide_by_id(int(pesticide_id))
    except ValueError as e:
        return "invalid id"
    return jsonify(pesticide)


@app.route("/pesticides/<pesticide_id>/<field>")
def get_pesticide_value(pesticide_id, field):
    try:
        value = get_specific_pesticide_field(int(pesticide_id), field)
    except ValueError as e:
        return "invalid id"
    except KeyError as e:
        return "invalid key"
    return jsonify(value)


def main():
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
