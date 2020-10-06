class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("You are in an empty hallway with doors to the east, north, and west", 3, 1, None, 6)
    room_list.append(room)
    room = Room("", 3, 1, None, 6)
    room_list.append(room)
    print(room_list)
    current_room = 0


main()