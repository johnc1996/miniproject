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


def get_people_first_and_last_names():
    query = "SELECT FirstName, LastName FROM People"
    first_and_last_names = db_return_rows(query)
    return first_and_last_names


def get_drink_names():
    query = "SELECT Name FROM Drinks"
    drink_names = db_return_rows(query)
    return drink_names
