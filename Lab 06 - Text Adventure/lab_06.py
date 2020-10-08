# Create Room class
class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    # Creating instances of rooms
    room_list = []
    room = Room("You are in an empty hallway with doors to the east, north, and west.", 3, 6, None, 1)
    room_list.append(room)
    room = Room("You are in an a dilapidated old living room with doors to go north or east.", 2, 0, None, None)
    room_list.append(room)
    room = Room("You are in a bathroom that has no doors except the one you came in from south.", None, None, 1, None)
    room_list.append(room)
    room = Room("You are in a hall with creepy paintings. Doors are to the north and south.", 4, None, 0, None)
    room_list.append(room)
    room = Room("You are in an old kitchen. The south door slams shut! You can only go east.", None, 5, None, None)
    room_list.append(room)
    room = Room("You are in a dining room. Dust sits on the plates. You can go south or west.", None, None, 6, 4)
    room_list.append(room)
    room = Room("You are in a bedroom with bad vibes. You feel you should flee. Go north or east.", 5, 0, None, None)
    room_list.append(room)

    # Set up game
    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        user_choice = input("Where do you want to go? ")

        # If the user wants to go north
        if user_choice.upper() == "NORTH" or user_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You cannot go that way.")
            else:
                current_room = next_room

        # If the user wants to go east
        elif user_choice.upper() == "EAST" or user_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You cannot go that way.")
            else:
                current_room = next_room

        # If the user wants to go south
        elif user_choice.upper() == "SOUTH" or user_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You cannot go that way.")
            else:
                current_room = next_room

        # If the user wants to go west
        elif user_choice.upper() == "WEST" or user_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You cannot go that way.")
            else:
                current_room = next_room

        # If the user wants to quit
        elif user_choice.upper() == "QUIT" or user_choice.upper() == "Q":
            print()
            print("You quit the game.")
            done = True
        # If the user's directions were not recognized
        else:
            print()
            print("Your directions were unclear. Use the name of the direction or first letter, \"north\" or \"n\".")


main()