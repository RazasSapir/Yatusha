from flask import Flask, send_from_directory
from pymongo import MongoClient

# Globals
app = Flask(__name__)

# Constants
MONGO_URI = "mongodb://yatusha-db" \
            ":1kkJmFQS0AMP2wN1l0bRrdSdB2C8SRDCqNpv1BmmctOuiCYYZ7mDhV88EKeB6xOV0i1kkFWsn0Yr18UfsRmyrg==@yatusha-db" \
            ".mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000" \
            "&appName=@yatusha-db@ "
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
    app.run(host=IP, port=PORT, debug=True)


if __name__ == '__main__':
    main()
