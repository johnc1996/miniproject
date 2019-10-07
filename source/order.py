class Order:
    def __init__(self, person, drink):
        self.person = person
        self.drink = drink

    def get_person(self):
        return self.person

    def get_drink(self):
        return self.drink
