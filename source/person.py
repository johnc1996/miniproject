class Person:
    def __init__(self, _id, first_name, last_name, favourite_drink):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.favourite_drink = favourite_drink

    def get_id(self):
        return self._id

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, new_first_name):
        self.first_name = new_first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, new_last_name):
        self.last_name = new_last_name

    def get_full_name_and_capitalize(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"

    def get_favourite_drink(self):
        return self.favourite_drink
