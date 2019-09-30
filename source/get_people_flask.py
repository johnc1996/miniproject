from flask import Flask, jsonify
import database

app = Flask(__name__)


@app.route("/hello_world")
def hello_world():
    return "Hello world!"


@app.route('/people', methods=['GET'])
def get_people_names():
    people = database.get_people_names()
    for person in people:
        return person


if __name__ == "__main__":
    app.run("localhost", 64000)
