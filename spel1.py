# used as global variables in the functions, 0 means that something is dealt with or
# that the user doesen't have the items
sword = 0
climb_tools = 0
candle = 0
candle_light = 0
bear = 1

# middle area of the map, the forest.
def area1():
    print("Welcome to the forest area!")
    print("You see 2 paths and a bear blocking the western path. What do you do?")
    print("1. Go east.")
    print("2. Go west.")
    print("3. Try to kill the bear.")
    print("4. Display information again.")

    my_bool = True

    global candle
    global candle_light
    global bear
    global sword

    while my_bool == True:

        choice1 = input("> ")

        # user goes east to the cliffs
        if choice1 == "1":
            area2()

        elif choice1 == "2":

            # goes west to the house if the bear is dealt with
            if bear == 0:
                print("You go west.")
                area3()
            # player gets killed by the bear
            else:
                print("You try to sneak through the bear, the bear mauls you to death. You lose!")
                input("Press any button to exit...")
                quit()

        # the player tries to kill the bear, if he has a sword he kills the bear...
        elif choice1 == "3":
            if bear == 0:
                print("The bear is already gone/dead.")

            elif sword == 1:
                print("You kill the bear!")
                bear = 0

            else:
                print("You wound the bear, but the bear knocks you down and eats your face off. You lose!")
                input("Press any button to exit...")
                quit()

        # Starts the function all over again to show the different choices
        elif choice1 == "4":
            area1()

        # else if statement that puts out the candle light if the user has one
        elif choice1 == "put out":
            if candle == 0:
                print("You dont have a candle to light up...")

            else:
                print("You put out the light...")
                candle_light = 0

        # else if statement that lights the candle if the player has one
        elif choice1 == "light":
            if candle == 1:
                if candle_light == 1:
                    print("The candle is already lit...")

                elif candle_light == 0:
                    print("You light the candle...")
                    candle_light = 1

            else:
                print("You dont have a candle to light.")

        else:
            if bear == 0:
                print("You already dealt with the bear...")

            else:
                print("You wait for a while and the bear finally leaves...")
                bear = 0


# the 2nd area of the map, the cliffs east of the forest
def area2():
    print("Welcome to the cliffs!")
    print("You see a rocky climbing path downwards into the canyon and a sword.")
    print("1. Climb down the rocky path.")
    print("2. Go west.")
    print("3. Take the sword.")
    print("4. Display information again.")

    global climb_tools
    global sword
    global candle
    global candle_light

    my_bool = True

    while my_bool == True:
        choice2 = input("> ")

        if choice2 == "1":

            if climb_tools == 1:
                print("You climb down to the canyon!")
                area6()

            print("You fall down to your death.")
            input("Press any button to exit...")
            quit()

        elif choice2 == "2":
            area1()

        elif choice2 == "3":
            if sword == 1:
                print("You already have the sword...")

            else:
                print("You picked up the sword!")
                sword = 1

        elif choice2 == "4":
            area2()

        elif choice2 == "put out":
            if candle == 0:
                print("You dont have a candle to light...")

            else:
                print("You put out the light...")
                candle_light = 0

        elif choice2 == "light":
            if candle == 1:
                if candle_light == 1:
                    print("The candle is already lit...")

                elif candle_light == 0:
                    print("You light the candle...")
                    candle_light = 1

            else:
                print("You dont have a candle to light.")

        else:
            print("Please choose a valid option...")


# The 3rd area of the map, the house west of the forest
def area3():
    print("""You are now at the house.
    You see a ladder leading up to the attic,
    and you also see a carpet and a candle.

    1. Go up the ladder
    2. Look at the carpet
    3. Take the candle
    4. Go east
    5. Display information""")


    carpet_choice = 0
    carpet = 1
    global candle
    global candle_light

    my_bool = True

    if carpet == 0:
        print("The trap door is where the carpet was before. Press 2 to go down the trap door...")

    while my_bool == True:
        choice3 = input("> ")

        if choice3 == "1":
            area4()

        elif choice3 == "2":
            if carpet == 1:
                print("You look at the carpet...")
                print("1. Step away from the carpet.")
                print("2. Try to move the carpet")

                carpet_choice = input("> ")

                if carpet_choice == "1":
                    print("You step away from the carpet.")
                    area3()

                elif carpet_choice == "2":
                    print("You move the carpet and find a trap door!")
                    carpet = 0

            elif carpet == 0:
                print("You go down the trap hole...")
                area5()

        elif choice3 == "3":
            print("You take the candle...")
            candle = 1

        elif choice3 == "4":
            area1()

        elif choice3 == "5":
            area3()

        elif choice3 == "put out":
            if candle == 0:
                print("You dont have a candle to put out the light of...")

            else:
                print("You put out the light...")
                candle_light = 0

        elif choice3 == "light":
            if candle == 1:
                if candle_light == 1:
                    print("The candle is already lit...")

                elif candle_light == 0:
                    print("You light the candle...")
                    candle_light = 1

            else:
                print("You dont have a candle to light.")

# The attic above the house
def area4():
    print("The attic")
    print("It's too dark to see in here, try to light a candle or something.")


    my_bool = True
    global climb_tools
    global candle_light
    global candle

    while my_bool == True:
        if candle_light == 1:
            print("""
            1. Take the climbing tools
            2. Look out from the hole
            3. Go down the stairs
            """)

            choice4 = input()

            if choice4 == "1":
                if climb_tools == 1:
                    print("You already have the climbing tools...")

                else:
                    print("You take the climbing tools.")
                    climb_tools = 1

            elif choice4 == "2":
                print("You take a look outside of the hole.")
                print("You feel someone pushing you and you fall down from the house and break your neck.")
                print("You died.")
                input("Press any button to exit...")
                quit()

            elif choice4 == "3":
                area3()

        elif candle == 1:
            light_candle = input()
            if light_candle == "light candle" or "light the candle" or "light":
                print("You light your candle...")
                candle_light = 1

            else:
                print("you didnt light your candle...")
                area3()

        else:
            print("You have nothing to light and its too dark in here.")
            area3()


# the basement of the house
def area5():
    print("The basement")
    print("It's very dark down here, try to light something.")

    global sword
    global candle
    global candle_light

    my_bool = True

    while my_bool == True:
        if candle_light == 1:
            print("You see a big troll at the end of the room. Behind it you see a small light.")
            if sword == 1:
                print("What do you want to do?")
                print("1. try to run away.")
                print("2. Attack the troll witth the sword.")

                choice_troll = input("> ")

                if choice_troll == "1":
                    print("You try to run away from the troll, you feel something cutting through your back.")
                    print("You died!")
                    input("Press any button to exit...")
                    quit

                elif choice_troll == "2":
                    print("You swing your sword at the troll, the troll bleeds to death.")
                    print("You win!")
                    input("Press any button to exit...")
                    quit()

        elif candle_light == 0:
            if candle == 1:
                print("You light the candle.")
                candle = 1
            else:
                print("Something swings at you in the dark. You died!")
                input("Press any button to exit...")
                quit()

# Canyon, down path from cliffs
def area6():
    print("You have finally reached the great canyone. God blesses you with a seat besides him for eternity.")
    print("You win!")

# The first choice function where to start on the map, 3 beinning choices
def area_choice():
    print("1. The forest area.")
    print("2. Cliff.")
    print("3. House.")
    area = input("> ")

    if area == "1":
        area1()

    elif area == "2":
        area2()

    elif area == "3":
        area3()

    else:
        print("That is an invalid area, please choose one of the following.")
        area_choice()

def main():

    print("Welcome to the Vukmir game, in this game we go through different areas.")
    area_choice()


main()
