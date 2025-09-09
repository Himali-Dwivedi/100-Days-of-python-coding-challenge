# Write your code below this line 👇

import os;
from Day_9C_Final_Project_Silent_Action_Logo import logo;

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac/Linux
    else:
        os.system('clear')

is_auction_over = False;
bidders_bid = {};
highest_bid = 0;
winner = "";

print(logo);

print("Welcome to the secret auction program");
while (is_auction_over == False):
    bidder_name = input("What is your name?: ");
    bid = int(input("What's you bid?: $"));

    bidders_bid[bidder_name] = bid;

    is_other_bidder = input("Are there any other bidders? Type 'yes' or 'no': ");

    if(is_other_bidder.lower() == "no"):
        is_auction_over = True;

    clear_console();

for bidder in bidders_bid:
    if(bidders_bid[bidder] > highest_bid):
        highest_bid = bidders_bid[bidder];
        winner = bidder;

print(f"The winner is {winner} with a bid of ${highest_bid}");
