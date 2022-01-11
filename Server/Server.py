from flask import Flask, send_from_directory, jsonify, abort, Response, render_template, request
import requests
import mongoengine
import http
import json
import os
import pymongo

from pesticides import *
from bson.objectid import ObjectId
import http
import save_pesticides_csv
from save_pesticides_csv import *

# from users_login_and_logout import Register
from pesticiding_action import *

# Globals
app = Flask(__name__, template_folder='templates')

# Constants
ACTIVATE_SSL = False
app.config["MONGO_URI"] = "MONGO_URI"
app.config["MONGO_CLIENT"] = pymongo.MongoClient(app.config["MONGO_URI"])
app.config["PESTICIDES_CSV"] = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '..', 'assets', 'pesticides.csv'))
app.config['DEBUG'] = True

IP = "127.0.0.1"
PORT = 80
MONGO_DB_PORT = 27017
POST_TEST_URL = "http://localhost:80/update/{obj_id}".format(obj_id=ObjectId("61c4fe781a3e3f61c3acb97b"))

disconnect()
client = mongoengine.connect(host=IP, port=MONGO_DB_PORT)


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
            "additional_information": "abc"}
    """, "location": {"type": "Point", "coordinates":
             [location.latitude, location.longitude]}}"""

    res = requests.post(POST_TEST_URL, json=data)
    if res.status_code == 204:
        return "No content"

    elif res.ok:
        return "Worked" + res.text
    return str(res.ok)


"""
@app.route('/test_register', methods=['GET', 'POST'])
def register_to_the_site():
    form = Register()

    return render_template('register.html', Register=form)
    """


@app.route("/")
def hello_world():
    return send_from_directory("../assets", "Test.html")


@app.route("/save", methods=['POST'])
def save_db():
    data = request.json
    try:
        """add_pesticing_to_db = PesticidingAction(name=data['name'], license_type=data['license_type'],
                                            license_number=data['license_number'],
                                            place_type=data['place_type'], pest_type=data['pest_type'],
                                            pesticides_ID=data['pesticides_ID'],
                                            additional_information=data['additional_information'])"""
        add_pesticing_to_db = PesticidingAction(name=data['name'], license_type=data['license_type'],
                                                license_number=data['license_number'],
                                                place_type=data['place_type'], pest_type=data['pest_type'],
                                                pesticides_ID=data['pesticides_ID'],
                                                additional_information=data['additional_information'])
        add_pesticing_to_db.save()
        return jsonify(data)
    except ValueError:
        abort(400, description="invalid input")


@app.route("/update/<query_id>", methods=['POST'])
def update(query_id):
    try:
        obj_to_update_in_db = "aaa"
        obj_to_put_in_db = "abc"
        query = update_db(db=client.YatushaDebug, obj_to_change=obj_to_update_in_db,
                          obj_to_put=obj_to_put_in_db,
                          obj_id=query_id)
        temp_query = query
        temp_query.pop('_id')  # just to save the id
        query_as_str = json.dumps(temp_query)
        query_as_json = json.loads(query_as_str)
        return jsonify(query_as_json)
    except ValueError:
        abort(400, description="invalid update")


@app.route('/delete/<query_id>', methods=['POST'])
def delete(query_id):
    query_as_json = None
    try:
        query = delete_db(db=app.config["YatushaDB"], obj_id=query_id)
        temp_query = query
        if temp_query is not None:
            temp_query.pop('_id', None)
            query_as_str = json.dumps(temp_query)
            query_as_json = json.loads(query_as_str)
        else:
            return '', http.HTTPStatus.NO_CONTENT
    except ValueError:
        abort(400, description="invalid delete")

    return jsonify(query_as_json)


@app.route("/pesticides/<pesticide_id>")
def get_pesticide(pesticide_id: int) -> Response:
    """
    Url for accessing pesticidesDB, returns a Response with the pesticide corresponding to "pesticide_id".
    :raises: ValueError
    :param pesticide_id: int - id of the wanted pesticide
    :return: Response - the pesticide data as JSON
    """
    try:
        pesticide: Document = get_pesticide_by_id(db=app.config["YatushaDB"], _id=int(pesticide_id))
    except ValueError:
        invalid_id_response = Response()
        invalid_id_response.status_code = 400
        invalid_id_response.data = "invalid id"
        return invalid_id_response
    return jsonify(pesticide)


@app.route("/pesticides/<pesticide_id>/<field>")
def get_pesticide_value(pesticide_id: int, field: str) -> Response:
    """
    Url for accessing pesticidesDB, returns a Response with the value of the given field for the pesticide corresponding
     to "pesticide_id"
    :param pesticide_id: int - id of the wanted pesticide
    :param field: str - the wanted field
    :return: Response - the value of the pesticide's field as JSON
    """
    try:
        value = get_specific_pesticide_field(db=app.config["YatushaDB"], _id=int(pesticide_id), field=field)
    except ValueError:
        invalid_id_response = Response()
        invalid_id_response.status_code = 400
        invalid_id_response.data = "invalid id"
        return invalid_id_response
    except KeyError:
        invalid_id_response = Response()
        invalid_id_response.status_code = 400
        invalid_id_response.data = "invalid key"
        return invalid_id_response
    return jsonify(value)


def main():
    save_csv()  # added it to save the pesticides csv
    disconnect()
    mongoengine.connect(host=IP, port=MONGO_DB_PORT, name="YatushaDebug")
    client = pymongo.MongoClient('localhost', 27017)
    app.config["YatushaDB"] = client['YatushaDebug']
    csv_to_mondo(app.config["YatushaDB"], app.config["PESTICIDES_CSV"])
    if ACTIVATE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
