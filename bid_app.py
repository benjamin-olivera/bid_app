from art import logo
print(logo)
import os

def clear_console():
    os.system('cls')
bidders = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
  highest_bid = 0 
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not  bidding_finished:
    name =input("Welcome to the secret auction program.\nWhat is your name?\n")
    price = int(input("What's your bid?\n"))
    bidders[name] = price
    continue_bid = input("Are there any other bidders? Type 'yes'or 'no'"".\n")
    if continue_bid == "no":
       bidding_finished = True
       find_highest_bidder(bidders)
    elif continue_bid == "yes":
        clear_console()
print(bidders)
