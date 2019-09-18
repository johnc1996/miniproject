class Drink:
    def __init__(self, name, unique_id):
        self.name = name
        self.id = unique_id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id
