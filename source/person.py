import database


class Person:
    def __init__(self, name, id_=-1):
        self.name = name
        self.id_ = id_

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id_

    def insert_person_into_database_and_update_id_with_database_value(self):
        sql_save = """
        INSERT into tb_People (name)
        VALUES (%s)
        """

        sql_query_latest_id = """
        SELECT max(person_id) FROM tb_People
        """

        parameters = (self.name)

        database.db_insert_or_update_record(sql_save, parameters)

        self.id_ = database.db_return_rows(sql_query_latest_id)
