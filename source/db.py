from os import environ
import pymysql


def get_connection():
    db = pymysql.connect(
            environ.get('DB_HOST'),  # host
            environ.get('DB_USER'),  # username
            environ.get('DB_PASSWORD'),  # password
            environ.get('DB_NAME')  # database
    )
    return db


def db_insert_or_update_record(command, parameters):
    with get_connection() as cursor:
        cursor.execute(command, parameters)


def db_return_rows(query):
    with get_connection() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def get_all_people():
    query = "SELECT * FROM People"
    people = db_return_rows(query)
    return people


def get_all_drinks():
    query = "SELECT * FROM Drinks"
    drinks = db_return_rows(query)
    return drinks


def get_all_rounds():
    query = "SELECT * FROM Rounds"
    return db_return_rows(query)


def get_people_first_and_last_names():
    query = "SELECT FirstName, LastName FROM People"
    first_and_last_names = db_return_rows(query)
    return first_and_last_names


def get_drink_names():
    query = "SELECT Name FROM Drinks"
    drink_names = db_return_rows(query)
    return drink_names


def get_initiators_first_and_last_name():
    query = """
    SELECT P.FirstName, P.LastName
    FROM Rounds as R
    JOIN People as P ON R.InitiatorID = P.PersonID
    """
    return db_return_rows(query)


def insert_drink(drink_name):
    query = """
    INSERT INTO Drinks(Name)
    VALUES (%s)
    """

    parameters = drink_name.lower()

    return db_insert_or_update_record(query, parameters)


def insert_person(first_name, last_name, favourite_drink_id):
    query = """
    INSERT INTO People(FirstName, LastName, FavouriteDrinkID)
    VALUES (%s, %s, %s)
    """

    parameters = (first_name.lower(), last_name.lower(), favourite_drink_id)

    return db_insert_or_update_record(query, parameters)


def delete_person(person_id):
    query = """
    DELETE FROM People
    WHERE PersonID = %s
    """

    parameters = person_id

    return db_insert_or_update_record(query, parameters)


def insert_round(initiator_id):
    query = """
    INSERT INTO Rounds(InitiatorID)
    VALUES (%s)
    """

    parameters = initiator_id

    return db_insert_or_update_record(query, parameters)
