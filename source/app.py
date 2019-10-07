from person import Person
from drink import Drink
from round import Round
from prettytable import PrettyTable
import input_handle


# general
def get_id_of_list_item_in_list_and_add_one(_list):
    try:
        return _list[-1].get_id() + 1
    except IndexError:
        return 1


# people
def get_all_people(_people):
    people_table = PrettyTable()
    people_table.field_names = ["ID", "First Name", "Last Name", "Favourite Drink"]
    for person in _people:
        people_table.add_row(
            [person.get_id(), person.get_first_name().capitalize(), person.get_last_name().capitalize(),
             person.get_favourite_drink().get_name().capitalize()])
    return people_table


def create_person_and_add_to_list_and_return_new_list(_people, _drinks):
    # create person
    person_id = get_id_of_list_item_in_list_and_add_one(_people)
    first_name = input_handle.get_valid_name("first name").lower()
    last_name = input_handle.get_valid_name("last name").lower()
    favourite_drink = get_favourite_drink("favourite drink", _drinks)
    person = Person(person_id, first_name, last_name, favourite_drink)

    # add person to list
    _people.append(person)
    return _people


# drinks
def get_all_drinks(_drinks):
    drinks_table = PrettyTable()
    drinks_table.field_names = ["ID", "Drink"]
    for drink in _drinks:
        drinks_table.add_row([drink.get_id(), drink.get_name().capitalize()])
    return drinks_table


def get_drink_ids(_drinks):
    drinks_ids = []
    for drink in _drinks:
        drinks_ids.append(drink.get_id())
    return drinks_ids


def get_favourite_drink(id_to_enter, _drinks):
    drinks_ids = get_drink_ids(_drinks)
    favourite_drink_id = input_handle.get_valid_id(id_to_enter, drinks_ids)
    for drink in _drinks:
        if favourite_drink_id == drink.get_id():
            return drink


def create_drink_and_add_to_list_and_return_new_list(_drinks):
    # create drink
    drink_id = get_id_of_list_item_in_list_and_add_one(_drinks)
    drink_name = input_handle.get_valid_name("drink name").lower()
    drink = Drink(drink_id, drink_name)

    # add drink to list
    _drinks.append(drink)
    return _drinks


# rounds
def get_all_rounds(_rounds):
    rounds_table = PrettyTable()
    rounds_table.field_names = ["ID", "Initiator", "Active", "Start Time"]
    for _round in _rounds:
        rounds_table.add_row(
            [_round.get_id(), _round.get_initiator().get_full_name_and_capitalize(), _round.get_active(),
             _round.get_start_time()])
    return rounds_table


def get_people_ids(_people):
    people_ids = []
    for person in _people:
        people_ids.append(person.get_id())
    return people_ids


def get_initiator(id_to_enter, _people):
    people_ids = get_people_ids(_people)
    initiator_id = input_handle.get_valid_id(id_to_enter, people_ids)
    for person in _people:
        if initiator_id == person.get_id():
            return person


def create_round_and_add_to_list_and_return_new_list(_rounds, _people):
    round_id = get_id_of_list_item_in_list_and_add_one(_rounds)
    initiator = get_initiator("initiator", _people)
    _round = Round(round_id, initiator)

    _rounds.append(_round)
    return _rounds


people = []
drinks = []
rounds = []

drinks = create_drink_and_add_to_list_and_return_new_list(drinks)
print(get_all_drinks(drinks))

people = create_person_and_add_to_list_and_return_new_list(people, drinks)
print(get_all_people(people))

rounds = create_round_and_add_to_list_and_return_new_list(rounds, people)
print(get_all_rounds(rounds))
