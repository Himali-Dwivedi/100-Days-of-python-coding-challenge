# Write your code below this line 👇

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

is_rematch = True;

while (is_rematch == True):
    print(logo);
    print("====================================");
    print("Welcome to the table!")
    print(f"Your balance is: ${user_balance}");
    print("------------------------------------");
    try:
        bet = int(input("Place your bet: $"));
    except ValueError:
        print(f"Invalid bet! Please bet between $1 to ${user_balance}");

    if(bet <= 0 or bet > user_balance):
        while(bet <= 0 or bet > user_balance):
            try:
                bet = int(input(f"Invalid bet! Please bet between $1 to ${user_balance}: "));
            except ValueError:
                print(f"Invalid bet! Please bet between $1 to ${user_balance}");

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
    if(user_action.lower() != "hit" and user_action.lower() != "stand" and user_action.lower() != "double down" and user_action.lower() != "split"):
        while(user_action.lower() != "hit" and user_action.lower() != "stand" and user_action.lower() != "double down" and user_action.lower() != "split"):
            user_action = input("Invalid action! Choose an action:\n\t1. Hit\n\t2. Stand\n\t3. Double Down\n\t4. Split\n");

    elif(user_action.lower() == "stand"):
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
        is_rematch == True;
        dealer_cards = [];
        dealer_ranks = [];
        user_cards = [];
        user_ranks = [];
        for i in range(1, len(dealer_cards_with_one_hidden_card)):
            dealer_cards_with_one_hidden_card.pop(i);