from src.index import store
class Guest:
    def __init__(self, name):
        guest_id = len(store['guests']) + 1
        store['guests'][guest_id] = self
        self.id = guest_id
        self.name = name

    def reservations(self):
        return [reservation for reservation in store['reservations'].values() if reservation.guest.id == self.id]

    def rooms(self):
        return [reservation.room for reservation in self.reservations()]
        