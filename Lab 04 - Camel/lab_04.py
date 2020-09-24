import random


def main():
    miles_traveled = 0
    player_thirst = 0
    camel_fatigue = 0
    miles_traveled_natives = -20
    canteen_drinks = 3

    # Introduction
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    # Instructions to game
    done = False
    while not done:
        print()
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        # If the user wants to quit
        user_choice = input("What is your choice? ")
        print()
        if user_choice.upper() == "Q":
            print("You quit the game.")
            done = True

        # If the user wants to check status
        elif user_choice.upper() == "E":
            print("Miles Traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            distance_between = miles_traveled - miles_traveled_natives
            print("The natives are", distance_between, "miles behind you.")

        # If the user wants to stop for the night
        elif not done and user_choice.upper() == "D":
            camel_fatigue = 0
            print("Your camel is happy!")
            miles_traveled_natives = miles_traveled_natives + random.randrange(7, 17)

        # If the user wants to travel full speed
        elif user_choice.upper() == "C":
            if random.randrange(21) == 0:
                print("You found an oasis!")
                player_thirst = 0
                canteen_drinks = 0
                camel_fatigue = 0
            else:
                miles_traveled_today = random.randrange(10, 21)
                miles_traveled = miles_traveled_today + miles_traveled
                print("You traveled", miles_traveled_today, "miles.")
                player_thirst = player_thirst + 1
                camel_fatigue = camel_fatigue + random.randrange(1, 4)
                miles_traveled_natives = miles_traveled_natives + random.randrange(7, 15)

        # If the user wants to travel moderate speed
        elif user_choice.upper() == "B":
            if random.randrange(21) == 0:
                print("You found an oasis!")
                player_thirst = 0
                canteen_drinks = 0
                camel_fatigue = 0
            else:
                miles_traveled_today = random.randrange(5, 13)
                miles_traveled = miles_traveled_today + miles_traveled
                print("You traveled", miles_traveled_today, "miles.")
                player_thirst = player_thirst + 1
                camel_fatigue = camel_fatigue + 1
                miles_traveled_natives = miles_traveled_natives + random.randrange(7, 15)

        # If the user wants to take a drink from the canteen
        elif user_choice.upper() == "A":
            if canteen_drinks >= 1:
                print("You take a drink from your canteen.")
                player_thirst = 0
                canteen_drinks = canteen_drinks - 1
            else:
                print("You have no more water left!")

        # Thirst mechanics
        if not done and player_thirst > 4 and player_thirst <= 6:
            print("You are thirsty...")
        elif player_thirst > 6:
            print("You have died of thirst!")
            done = True

        # Winning via crossing the desert
        if miles_traveled >= 200:
            print("You traversed the desert!")
            done = True

        # Natives catching player mechanics
        if not done and miles_traveled - miles_traveled_natives <= 0:
            print("The natives have caught you, you lost!")
            done = True
        elif miles_traveled - miles_traveled_natives <= 15:
            print("The natives are getting close!")

        # Camel dying of fatigue mechanics
        if not done and camel_fatigue >= 5 and camel_fatigue <= 8:
            print("Your camel is getting tired.")
        if camel_fatigue > 8:
            print("Your camel died of exhaustion!")
            done = True


main()