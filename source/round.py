class Round:
    def __init__(self, brew_master):
        self.brew_master = brew_master
        self.orders = {}

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

    #TODO random number generator to determine who makes round
