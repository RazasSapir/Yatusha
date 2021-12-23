import mongoengine
import requests
from flask import Flask, send_from_directory, request, jsonify, abort

from ServerSettings import IP, PORT, USE_REMOTE_DB, USE_SSL, LOCAL_DB_URI
from pesticing import *
from secret_keys.Private_URIs import MONGO_URI

# Globals
app = Flask(__name__)


def config_server():
    if USE_REMOTE_DB:
        app.config["MONGO_URI"] = MONGO_URI
    else:
        app.config["MONGO_URI"] = LOCAL_DB_URI
    mongoengine.connect(host=IP, port=app.config["MONGO_URI"])


@app.route("/<asset>")
def gasp_js(asset):
    return send_from_directory("../assets", asset)


@app.route("/echo", methods=['POST'])
def echo_page():
    content = request.json
    return jsonify(content)


@app.route("/test_json")
def test_json():
    res = requests.post('http://localhost:80/save', json={"name": "lalala", "license_type": 2,
                                                          "license_number": "1234",
                                                          "place_type": "Public Space", "pest_type": "cricket",
                                                          "pesticides_ID": "1234",
                                                          "additional_information": "abc"})
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
        add_pesticing_to_db = PesticingToDB(name=data["name"], license_type=data["license_type"],
                                            license_number=data["license_number"],
                                            place_type=data["place_type"], pest_type=data["pest_type"],
                                            pesticides_ID=data["pesticides_ID"],
                                            additional_information=data["additional_information"])
        add_pesticing_to_db.save()
    except ValueError as e:
        print("Error:", e)
        abort(400, description="invalid place type")
    return jsonify(data)


@app.route("/update/<query_id>", methods=['POST'])
def update_db(query_id):
    data = request.json
    try:
        obj_to_update_in_db = "additional_information"
        obj_to_put_in_db = "additional_information"
        Update_and_delete.update_DB(obj_to_change=obj_to_update_in_db,
                                    obj_to_put=obj_to_put_in_db,
                                    obj_id=query_id)
    except ValueError:
        abort(400, description="invalid update")

    return jsonify(data)


def main():
    config_server()
    if USE_SSL:
        context = ("../secret_keys/server.crt", "../secret_keys/server.key")
        app.run(host=IP, port=PORT, debug=True, ssl_context=context)
    else:
        app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
