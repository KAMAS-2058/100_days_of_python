# Making a Blackjack game in python
#the cards represent an infinite deck
import random

is_game_over = False
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #an ace can be 11 or 1
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lost, Computer has blackjack"
    elif user_score == 0:
        return "You win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your Cards: {user_cards} \n Your score: {user_score}")
    print(f"Computer's First Card: {computer_cards[0]}")

    if user_score == 0 or computer_score ==0 or user_score>21:
        is_game_over = True


user_should_deal = input("Type 'y' to get another card or 'n' to pass:")
if user_should_deal == 'y':
    user_cards.append(deal_card())
elif user_should_deal == 'n':
    is_game_over = True

while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_cards = calculate_score(computer_cards)

compare(user_score,computer_score)