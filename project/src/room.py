from src.index import store
class Room:
    def __init__(self, room_number, rate):
        room_id = len(store['rooms']) + 1
        store['rooms'][room_id] = self
        self.id = room_id
        self.room_number = room_number
        self.rate = rate

    def reservations(self):
        return [reservation for reservation in store['reservations'].values() if reservation.room.id == self.id]