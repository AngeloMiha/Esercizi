from room import Room
from building import Building
r = Room(name="123", floor=2, num_seats=30)
r1 = Room(name="321", floor=3, num_seats=10)
r2 = Room(name="111", floor=1, num_seats=20)

print(r)
print(r1)
print(r2)

b = Building(name="SMI", address="Via Sierra Nevada 60", floors=[-2, 2])

print("#" * 30)

print(b)
print(len(b.get_rooms()))
b.add_room(r)
b.add_room(r1)
b.add_room(r2)

print("#" * 30)

print(b)
print(len(b.get_rooms()))
