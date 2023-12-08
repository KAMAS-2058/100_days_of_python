#number guessing game
import random
print("hello, welcome to number guesser\n I'm thinking of a number between 1 and 100")

EASY = 5
HARD = 10

def guessing(guess,answer,p_l):
    player_guess = int(input("Guess a number between 1 and 100!\n"))
    if player_guess > answer:
        print("that was too high!\n guess again!")
        p_l -= 1
    elif player_guess < answer:
        print("that was too low!\n guess again!")
        p_l -= 1
    elif player_guess == answer:
        print(f"Right on Target! you win\n the number was {answer}")    
    else:
        print("invalid input")
        p_l -= 1

def game_diff(diff):
    number = random.randint(1,100)
    if diff == 'easy':
        return EASY
    elif diff == 'hard':
        return HARD
    else:
        print("invalid input")

def game():
    answer = random.randint(1,100)
    guess = int(input("Make a Guess:"))
    turns = game_diff()
    print(f"you have {turns} lives")

    while guess !=  answer:
       pass