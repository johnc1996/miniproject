from datetime import datetime

import database


class Round:
    def __init__(self, initiator, id_=-1):
        self.initiator = initiator
        self.orders = {}
        self.id = id_
        self.active = True
        self.start_time = datetime.now().time()

    def get_drink_maker(self):
        return self.initiator

    def add_to_order(self, person, drink):
        self.orders[person] = drink

    def amend_drink(self, person, drink):
        self.orders[person] = drink

    def get_drink_orders(self):
        return self.orders

    def get_drink_count(self):
        order_values = list(self.orders.values())
        unique_drinks = list(set(self.orders.values()))
        drink_value = {}
        for drink in unique_drinks:
            drink_value[drink] = order_values.count(drink)
        return drink_value

    def insert_round_into_database_and_update_id_with_database_value(self):
        sql_save = f"""
        INSERT INTO tb_Rounds (Round_Active, Round_StartTime, Round_Initiator)
        VALUES (%s, %s, %s)
        """

        sql__query_latest_id = """
        SELECT max(Round_Id) FROM tb_Rounds
        """

        parameters = (self.active, self.start_time, self.initiator)

        database.db_insert_or_update_record(sql_save, parameters)

        self.id = database.db_return_rows(sql__query_latest_id)
