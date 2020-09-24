import random

def main():
    miles_traveled = 0
    player_thirst = 0
    camel_fatigue = 0
    miles_traveled_natives = -20
    canteen_drinks = 3
    distance_between = miles_traveled - miles_traveled_natives

    # Introduction
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    #Instructions to game
    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        #If the user wants to quit
        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            print("You quit the game.")
            done = True

        #If the user wants to check status
        elif user_choice.upper() == "E":
            print("Miles Traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            print("The natives are", distance_between, "miles behind you")

        #If the user wants to stop for the night
        elif user_choice.upper() == "D":
            camel_fatigue = 0
            print("Your camel is happy!")
            miles_traveled_natives = miles_traveled_natives + random.randrange(7, 17)

        #If the user wants to travel full speed
        elif user_choice.upper() == "C":
            miles_traveled_today = random.randrange(10, 21)
            miles_traveled = miles_traveled_today + miles_traveled
            print("You traveled", miles_traveled_today, "miles")
            player_thirst = player_thirst + 1
            camel_fatigue = camel_fatigue + random.randrange(1, 4)
            miles_traveled_natives = miles_traveled_natives + random.randrange(7, 15)

        #If the user wants to travel moderate speed
        elif user_choice.upper() == "B":
            miles_traveled_today = random.randrange(5, 13)
            miles_traveled = miles_traveled_today + miles_traveled
            print("You traveled", miles_traveled_today, "miles")
            player_thirst = player_thirst + 1
            camel_fatigue = camel_fatigue + 1
            miles_traveled_natives = miles_traveled_natives + random.randrange(7, 15)

        elif user_choice.upper() == "A":
            if canteen_drinks > 1:
                print("You take a drink from your canteen")
                player_thirst = 0
                canteen_drinks = canteen_drinks - 1
            else:
                print("You have no more water left!")

        #Game mechanic comparisons
        if player_thirst > 4 and player_thirst <= 6:
            print("You are thirsty...")
        if player_thirst > 6:
            print("You have died of thirst!")
            done = True
        if miles_traveled >= 200:
            print("You beat the game!")
            done = True
        if distance_between == 0:
            print("The natives caught you!")
            done = True

main()