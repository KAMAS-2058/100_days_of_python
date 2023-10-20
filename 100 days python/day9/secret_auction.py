#making use of dictionaries and nesting we will create a secret auction program 
from clear import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the Secret Auction program")
bids = {}
bidding_finished = False

def highest_bidder(bidding_record):
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} witha bid of ${highest_bid}")
while not bidding_finished:
    name = input("What is your name?")
    price = input("What is your bid $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'")
    if should_continue == 'no':
        bidding_finished = True
    elif should_continue == 'yes':
        clear()





