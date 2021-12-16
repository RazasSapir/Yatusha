from flask import Flask

app = Flask(__name__)

IP = "0.0.0.0"
PORT = 80


@app.route("/")
def hello_world():
    return "<p>Yatusha is Here!</p>"


def main():
    app.run(host=IP, port=PORT)


if __name__ == '__main__':
    main()
