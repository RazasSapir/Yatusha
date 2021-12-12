from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Yatusha is on the Web!</p>"


def main():
    app.run()


if __name__ == '__main__':
    main()
