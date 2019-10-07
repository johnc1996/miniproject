from flask import Flask, jsonify
from flask import request
from flask import render_template

import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return render_template("index.html", head_title="Briw", page_title="Briw")


@app.route('/people', methods=['GET'])
def get_people_home():
    people_first_and_last_names = db.get_people_first_and_last_names()
    return render_template("people.html", head_title="People", page_title="People", people=people_first_and_last_names)


@app.route('/drinks', methods=['GET'])
def get_drinks_home():
    drink_names = db.get_drink_names()
    return render_template("drinks.html", head_title="Drinks", page_title="Drinks", drink_names=drink_names)


@app.route('/people/view', methods=['GET'])
def get_people():
    return render_template("viewPeople.html", head_title="View People", page_title="View People")


@app.route('/people/add', methods=['GET', 'POST'])
def add_person():
    if request.method == "GET":
        return render_template("addPerson.html", head_title="Add People", page_title="Add Person")
    elif request.method == "POST":
        first_name = request.form.get("first-name")
        last_name = request.form.get("last-name")

        return render_template("personAdded.html", head_title="Add People", page_title="Person Added",
                               first_name=first_name, last_name=last_name)


@app.route('/drinks/view', methods=['GET'])
def get_drinks():
    return render_template("viewDrinks.html", head_title="View Drinks", page_title="View Drinks")


@app.route('/drinks/add', methods=['GET', 'POST'])
def add_drink():
    if request.method == "GET":
        return render_template("addDrink.html", head_title="Add Drink", page_title="Add Drink")
    elif request.method == "POST":
        drink_name = request.form.get("drink-name")

        return render_template("drinkAdded.html", head_title="Add Drink", page_title="Drink Added", drink=drink_name)


@app.route('/rounds/view', methods=['GET'])
def get_rounds():
    return render_template("viewRounds.html", head_title="View Rounds", page_title="View Rounds")


@app.route('/rounds/add', methods=['GET', 'POST'])
def add_round():
    if request.method == "GET":
        return render_template("addRound.html", head_title="Add Round", page_title="Add Round")
    elif request.method == "POST":
        initiator = request.form.get("round-initiator")

        return render_template("roundAdded.html", head_title="Add Round", page_title="Round Added",
                               round_initiator=initiator)


@app.route('/order/add', methods=['GET', 'POST'])
def add_order():
    if request.method == "GET":
        return render_template("addOrder.html", head_title="Add Order", page_title="Add Order")
    elif request.method == "POST":
        person_name = request.form.get("person-name")
        drink_name = request.form.get("drink-name")

        return render_template("orderAdded.html", head_title="Add Order", page_title="Confirm Order",
                               person=person_name, drink=drink_name)


if __name__ == "__main__":
    app.run(host='localhost', port=15000, debug=True)
