import random;
import Day_11A_Final_Project_BlackJack_Card_Details as card_details;
from Day_11A_Final_Project_BlackJack_Logo import logo;
def create_cards(number_of_cards, list_of_cards, list_of_ranks):
    for i in range(number_of_cards):
        rank = random.choice(card_details.ranks);
        suit = random.choice(card_details.suits);
        card =  rank + suit;
        list_of_cards.append(card_details.cards[card].splitlines());
        list_of_ranks.append(rank);



def calculate_score(list_of_ranks):
    your_score = 0;
    for rank in list_of_ranks:
        your_score += card_details.card_values[rank];
    return your_score;



def print_cards(list_of_cards):
    for i in zip(*list_of_cards):
        print(" ".join(i));



def stand(dealer_cards, dealer_ranks, user_cards, user_ranks, bet, user_balance):
    # does_user_win can only have 3 values:
        # 0 = It's a tie
        # 1 = User wins
        # 2 = Dealer wins
    does_user_win = 0;
    print("Dealer reveals hand:")
    print_cards(list_of_cards = dealer_cards)
    user_score = calculate_score(user_ranks)
    dealer_score = calculate_score(dealer_ranks)
    while dealer_score < 17:
        print(f"Dealer's score = {dealer_score}")
        print("Dealer hits...")
        create_cards(number_of_cards = 1, list_of_cards = dealer_cards, list_of_ranks = dealer_ranks)
        dealer_score = calculate_score(list_of_ranks = dealer_ranks)
        print_cards(list_of_cards = dealer_cards)
    print("=" * 100)
    print("Dealer's Hand:\n")
    print_cards(list_of_cards = dealer_cards)
    print(f"Dealer's score = {dealer_score}")
    print("Your Hand:\n")
    print_cards(list_of_cards = user_cards)
    print(f"Your score = {user_score}")
    if(user_score <= 21 and dealer_score <= 21):
        if(user_score > dealer_score):
            print("You win!")
            user_balance += bet
            does_user_win = 1;
        elif(user_score < dealer_score):
            print("Dealer wins!")
            user_balance -= bet
            does_user_win = 2;
        else:
            print("It's a push");
            does_user_win = 0;
    elif(user_score > 21 and dealer_score > 21):
        print("You both are busted. It's a push");
        does_user_win = 0;
    elif(user_score > 21):
        print("You are busted. Dealer wins!")
        user_balance -= bet
        does_user_win = 2;
    else:
        print("Dealer is busted. You win!")
        does_user_win = 1
        user_balance += bet

    if(does_user_win == 0):
        print(f"You do not loose any bet. Your total balance is ${user_balance}");
    elif(does_user_win == 1):
        print(f"You won ${bet}. Your total balance is ${user_balance}");
    elif(does_user_win == 2):
        print(f"You loose ${bet}. Your total balance is ${user_balance}");

    print("=" * 100)
    return user_balance;

def hit(dealer_cards, dealer_ranks, user_cards, user_ranks, bet, user_balance):
    want_to_hit = True;
    while (want_to_hit == True):
        print("Your Hand:\n")
        create_cards(number_of_cards = 1, list_of_cards = user_cards, list_of_ranks = user_ranks);
        print_cards(list_of_cards = user_cards);
        user_score = calculate_score(list_of_ranks = user_ranks);
        print(f"Your score = {user_score}")
        if(user_score > 21):
            print("You are busted. Dealer wins!")
            user_balance -= bet;
            print(f"You loose ${bet}. Your total balance is ${user_balance}");
            break;
        hit_or_not_hit = input("Do you want to hit again? (y/n) : ");
        while(hit_or_not_hit.lower() not in ["y", "n"]):
            hit_or_not_hit = input("Invalid input! Press 'y' if you want to hit again. Otherwise press 'n': ");
        if(hit_or_not_hit == "n"):
            want_to_hit = False;
            user_balance = stand(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);
    return user_balance;

def double_down(dealer_cards, dealer_ranks, user_cards, user_ranks, bet, user_balance):
    bet *= 2
    if(bet > user_balance):
        print("You can't double down. You have insufficient balance");
    else:
        print(f"You doubled your bet! New bet: ${bet}");
        create_cards(number_of_cards = 1, list_of_cards = user_cards, list_of_ranks = user_ranks);
        user_balance = stand(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);
    return user_balance;


def split(user_cards, user_ranks, dealer_cards, dealer_ranks, bet, user_balance):
    splitted_hand = [];
    splitted_ranks = [];
    if(len(user_cards) > 2):
        print("Oops! You can’t split now. Splitting is only possible with your first two cards.");
    if(user_cards[0] != user_cards[1]):
        print("Oops! You can only split when your first two cards are the same.");
    elif(user_cards[0] == user_cards[1]):
        print(f"""
    Your bet: ${bet}
    You split your cards! A new hand is created.
    Each hand has its own bet: ${bet}
            """);
        first_hand_cards = [];
        first_hand_cards.append(user_cards[0]);

        first_hand_ranks = [];
        first_hand_ranks.append(user_ranks[0]);

        second_hand_cards = [];
        second_hand_cards.append(user_cards[1]);

        second_hand_ranks = [];
        second_hand_ranks.append(user_ranks[1])

        splitted_hand = [first_hand_cards, second_hand_cards];
        splitted_ranks = [first_hand_ranks, second_hand_ranks];
        print("Your Hand:\n");
        for i in range(len(splitted_hand)):
            print(f"Your Hand {i + 1}");
            user_cards = splitted_hand[i];
            user_ranks = splitted_ranks[i];
            create_cards(number_of_cards = 1, list_of_cards = user_cards, list_of_ranks = user_ranks);
            print_cards(list_of_cards = user_cards);
            
        for i in range(len(splitted_hand)):
            print(f"You are playing Hand {i + 1}");
            if(i > 0):
                dealer_cards = [];
                dealer_ranks = [];
                create_cards(number_of_cards = 2, list_of_cards = dealer_cards, list_of_ranks = dealer_ranks);
            user_cards = splitted_hand[i];
            user_ranks = splitted_ranks[i];
            print_cards(list_of_cards = user_cards);
            user_action = input("Choose an action:\n\t1. Hit\n\t2. Stand\n\t3. Double Down\n\t4. Split\n");
            if(user_action.lower() != "hit" and user_action.lower() != "stand" and user_action.lower() != "double down" and user_action.lower() != "split"):
                while(user_action.lower() != "hit" and user_action.lower() != "stand" and user_action.lower() != "double down" and user_action.lower() != "split"):
                    user_action = input("Invalid action! Choose an action:\n\t1. Hit\n\t2. Stand\n\t3. Double Down\n\t4. Split\n");

            elif(user_action.lower() == "stand"):
                user_balance = stand(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);

            elif(user_action.lower() == "hit"):
                user_balance = hit(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);

            elif(user_action.lower() == "double down"):
                user_balance = double_down(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);
            elif(user_action.lower() == "split"):
                user_balance = split(dealer_cards = dealer_cards, dealer_ranks = dealer_ranks, user_cards = user_cards, user_ranks = user_ranks, bet = bet, user_balance = user_balance);
    return user_balance;
