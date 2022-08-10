from src.index import store
class Reservation:
    def __init__(self, room, guest, start_day, end_day):
        reservation_id = len(store['reservations']) + 1
        self.id = reservation_id
        store['reservations'][reservation_id] = self
        self.room = room
        self.guest = guest
        self.start_day = start_day
        self.end_day = end_day

        