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


def delete_person_from_database(person_id):
    sql_delete = """
    DELETE FROM tb_People
    WHERE person_id = (%s)
    """

    db_insert_or_update_record(sql_delete, person_id)


def delete_drink_from_database(drink_id):
    sql_delete = """
    DELETE FROM tb_Drinks
    WHERE drink_id = (%s)
    """

    db_insert_or_update_record(sql_delete, drink_id)


def update_favourite_pairing_of_person_id_and_drink_id(person_id, favourite_drink_id):
    sql_insert_pairing = """
    UPDATE tb_People
    SET Favourite_Drink_Id = %s
    WHERE %s
    """
    db_insert_or_update_record(sql_insert_pairing, (favourite_drink_id, person_id))


def get_person_id_and_person_name_from_people_database_table():
    sql_query = """
    SELECT * FROM tb_People
    """

    return db_return_rows(sql_query)


def get_people_names():
    sql_query = """
    SELECT name FROM tb_People
    """

    return db_return_rows(sql_query)


def get_drink_id_and_drink_name_from_drink_database_table():
    sql_query = """
    SELECT * FROM tb_Drinks
    """

    return db_return_rows(sql_query)


def get_person_and_favourite_drink_from_people_database_table():
    sql_query = """
    SELECT tb_People.name, tb_Drinks.name
    FROM tb_People, tb_Drinks
    WHERE tb_People.Favourite_Drink_Id=tb_Drinks.drink_id;
    """

    return db_return_rows(sql_query)


def get_rounds_info_from_rounds_database_table():
    sql_query = """
    SELECT * FROM tb_Rounds
    """

    return db_return_rows(sql_query)
