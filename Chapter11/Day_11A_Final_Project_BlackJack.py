# Write your code below this line 👇

# Instructions:
    # 1. Deal 2 cards to player and dealer (1 dealer card hidden).  
    # 2. Check for blackjack (Ace + 10 = 21) → payout or continue.  
    # 3. Player hits until stand or bust (>21).  
    # 4. Dealer reveals card, hits until 17+.  
    # 5. Compare totals → higher wins (unless bust).  
    # 6. Card values: 2–10 = face, J/Q/K = 10, Ace = 1 or 11 (whichever helps without busting). 

import Day_11A_Final_Project_BlackJack_Card_Details as card_details;
from Day_11A_Final_Project_BlackJack_Logo import logo;
import Day_11A_Final_Project_BlackJack_Functions as blackjack_functions;
# Below code is for testing pupose.
# It puts the cards side by side
# my_cards = [card_details.hidden_card["hidden"].splitlines(), card_details.cards["A♦"].splitlines()]

# for card in zip(*my_cards):
#     print(" ".join(card));

user_cards = [];
user_ranks  = [];

dealer_cards = [];
dealer_cards_with_one_hidden_card = [card_details.hidden_card["hidden"].splitlines()]
dealer_ranks = [];

user_balance = 1000;
bet = 0;

is_rematch = True;

while (is_rematch == True):
    print(logo);
    print("====================================");
    print("Welcome to the table!")
    print(f"Your balance is: ${user_balance}");
    print("------------------------------------");

    while True:
        try:
            bet = int(input(f"Place your bet between $1 - ${user_balance}: "))
            if(bet >= 1 and bet <= user_balance):
                break;
            else:
                print(f"Invalid bet! Please bet between $1 and ${user_balance}.");
        except ValueError:
            print("Invalid input! Please enter a number.");

    # =================================Initial Deal====================================
    # Dealer's cards
    print("Dealer's Hand:\n")
    blackjack_functions.create_cards(number_of_cards = 2, list_of_cards = dealer_cards, list_of_ranks = dealer_ranks);
    for i in range(len(dealer_cards) - 1):
        dealer_cards_with_one_hidden_card.append(dealer_cards[i]);

    blackjack_functions.print_cards(list_of_cards = dealer_cards_with_one_hidden_card);

    print("Your Hand:\n")
    # Your Card
    blackjack_functions.create_cards(number_of_cards = 2, list_of_cards = user_cards, list_of_ranks = user_ranks);

    blackjack_functions.print_cards(list_of_cards = user_cards);
    print(f"Your score = {blackjack_functions.calculate_score(list_of_ranks = user_ranks)}")

    # ====================================================================================


    # Keep asking for the user input until a valid input is found
    user_action = input("Choose an action:\n\t1. Hit\n\t2. Stand\n\t3. Double Down\n\t4. Split\n");
    while(user_action.lower() != "hit" and user_action.lower() != "stand" and user_action.lower() != "double down" and user_action.lower() != "split"):
        user_action = input("Invalid action! Choose an action:\n\t1. Hit\n\t2. Stand\n\t3. Double Down\n\t4. Split\n");

    if(user_action.lower() == "stand"):
        user_balance = blackjack_functions.stand(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance)

    elif(user_action.lower() == "hit"):
        user_balance = blackjack_functions.hit(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);

    elif(user_action.lower() == "double down"):
        user_balance = blackjack_functions.double_down(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);

    elif(user_action.lower() == "split"):
        user_balance = blackjack_functions.split(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);

    if (user_balance > 0):
        does_user_want_to_play_again = input(f"Do you want to play again? You still have ${user_balance} left (y/n):");
    elif(user_balance <= 0):
        print(f"You can play again. You balance is ${user_balance}");
        break;
    while(does_user_want_to_play_again not in ["y", "n"]):
        does_user_want_to_play_again = input(f"Invalid input! Please press 'y' if you want to play again. Otherwise press 'n'");
    if(does_user_want_to_play_again.lower() == "n"):
        is_rematch = False;
    elif(does_user_want_to_play_again.lower() == "y"):
        blackjack_functions.clear();
        is_rematch == True;
        dealer_cards = [];
        dealer_ranks = [];
        user_cards = [];
        user_ranks = [];
        for i in range(1, len(dealer_cards_with_one_hidden_card)):
            dealer_cards_with_one_hidden_card.pop(i);