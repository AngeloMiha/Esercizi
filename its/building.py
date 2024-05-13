from room import Room

class Building:

    def __init__(self, name: str, address: str, floors: int) -> None:
        self.name: str = name
        self.address: address = address
        self.floors: int = floors
        self.rooms: list[Room] = []

    def add_room(self, room: Room) -> bool:
        if room not in self.get_rooms() and room.floor <= self.get_floors():
            self.rooms.append(room)
            return True
        return False

    def get_name(self) -> str:
        return self.name
        
    def get_address(self) -> str:
        return self.address

    def get_floors(self) -> int:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
    
    def __str__(self) -> str:
        s: str = f"Building(name={self.get_name}, address={self.get_address}, floors={self.get_floors})"
        s += "\nWith Rooms:\n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s[:-1]
