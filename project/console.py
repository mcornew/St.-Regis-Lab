from src.index import store
from src.reservation import Reservation
from src.guest import Guest
from src.room import Room

prem_room = Room(401, 'premium')
bob = Guest('bob')


basic_room = Room(402, 'basic')
basic_first_floor = Room(401, 'basic')
sam = Guest('sam')


reservation_two = Reservation(basic_room, sam, 20, 25)
res_one = Reservation(prem_room, bob, 10, 20)
reservation_three = Reservation(prem_room, sam, 26, 30)

# sam.reservations()
# sam.rooms()
# prem_room.reservations()