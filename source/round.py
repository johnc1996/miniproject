from datetime import datetime


class Round:
    active = True
    start_time = datetime.now().time()
    orders = {}

    def __init__(self, _id, initiator):
        self._id = _id
        self.initiator = initiator

    def get_id(self):
        return self._id

    def get_initiator(self):
        return self.initiator

    def set_initiator(self, new_initiator):
        self.initiator = new_initiator

    def get_active(self):
        return self.active

    def set_active(self):
        if self.active:
            self.active = False
        else:
            self.active = True

    def get_start_time(self):
        return self.start_time

    def get_orders(self):
        return self.orders
