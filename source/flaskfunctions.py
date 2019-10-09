from flask import Flask, jsonify
from flask import request
from flask import render_template
from flask import redirect

import db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_home():
    return render_template("index.html", head_title="Briw", page_title="Briw")


@app.route('/people', methods=['GET'])
def get_people():
    if request.method == "GET":
        people_names = db.get_people_first_and_last_names()
        return render_template("people.html", head_title="People", page_title="People",
                               people_names=people_names)


@app.route('/people/add', methods=['GET', 'POST'])
def get_add_person_page_and_add_person():
    if request.method == 'GET':
        favourite_drinks = db.get_all_drinks()
        return render_template("addPerson.html", head_title="Add person", page_title="Add person",
                               favourite_drinks=favourite_drinks)
    elif request.method == 'POST':
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        favourite_drink = request.form.get('favourite-drink')
        db.insert_person(first_name, last_name, favourite_drink)
        return redirect('/people')


@app.route('/drinks', methods=['GET'])
def get_drinks():
    drink_names = db.get_drink_names()
    return render_template("drinks.html", head_title="Drinks", page_title="Drinks", drink_names=drink_names)


@app.route('/drinks/add', methods=['GET', 'POST'])
def get_add_drink_page_and_add_drink():
    if request.method == 'GET':
        return render_template("addDrink.html", head_title="Add drink", page_title="Add drink")
    if request.method == 'POST':
        drink_name = request.form.get("drink-name")
        db.insert_drink(drink_name)
        return redirect('/drinks')


@app.route('/rounds', methods=['GET'])
def get_rounds():
    rounds = db.get_initiators_first_and_last_name()
    return render_template("rounds.html", head_title="Rounds", page_title="Rounds", rounds=rounds)


@app.route('/rounds/add', methods=['GET', 'POST'])
def get_round_add_page_and_add_round():
    if request.method == 'GET':
        people = db.get_all_people()
        return render_template("addRound.html", head_title="Add round", page_title="Add round", people=people)
    elif request.method == 'POST':
        initiator_id = request.form.get("initiator")
        db.insert_round(initiator_id)
        return redirect('/rounds')


@app.route('/rounds/add/order', methods=['GET', 'POST'])
def get_order_add_page_and_add_order():
    if request.method == 'GET':
        people = db.get_all_people()
        drinks = db.get_all_drinks()
        rounds = db.get_all_rounds()
        initiators = db.get_initiators_first_and_last_name()
        return render_template("addOrder.html", head_title="Add order", page_title="Add order", people=people,
                               drinks=drinks, rounds=rounds, initiators=initiators)
    elif request.method == 'POST':
        pass


if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
