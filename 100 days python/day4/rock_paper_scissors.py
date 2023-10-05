#making rock paper scissors
import random

#competitors
user_choice = input("what do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n")
user_choice = int(user_choice)
computer_choice = random.randint(0,2)

if user_choice>=3:
    print("invalid input, you lose")
elif user_choice == 0 and computer_choice == 2:
    print("Player Wins!")
elif computer_choice > user_choice:
    print("computer wins")
elif user_choice > computer_choice:
    print("Player Wins!")
elif user_choice == computer_choice:
    print("draw")
    




