class Drink:
    def __init__(self, _id, name):
        self._id = _id
        self.name = name

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
