# import string
import random

won = 0
played = 0
tie = 0

while True:

    user_choice = str(input("Foot, Nuke or Cockroach? (Quit ends): "))

    if user_choice == "Quit":
        print("You played " + str(played) + " rounds, and won " + str(won) + " rounds, playing tie in " + str(tie) + " rounds.")
        exit()

    if user_choice != "Foot" and user_choice != "Nuke" and user_choice != "Cockroach":
        print("Incorrect selection.")
        continue

    else:
        computer_choice = random.randint(0, 3)
        if computer_choice == 1:
            computer_choice = "Foot"
        elif computer_choice == 2:
            computer_choice = "Nuke"
        else:
            computer_choice = "Cockroach"

        print("You chose: " + user_choice + "\nComputer chose: " + computer_choice)

        if user_choice == "Nuke" and computer_choice == "Nuke":
            print("Both LOSE!")
        elif user_choice == computer_choice:
            print("It is a tie!")
            tie = tie + 1
        elif user_choice == "Nuke" and computer_choice == "Foot":
            print("You WIN!")
            won = won + 1
        elif user_choice == "Foot" and computer_choice == "Cockroach":
            print("You WIN!")
            won = won + 1
        elif user_choice == "Cockroach" and computer_choice == "Nuke":
            print("You WIN!")
            won = won + 1
        else:
            print("You LOSE!")

        played = played + 1


