# Write your code below this line 👇
import random;

print("Welcome to the Number Guessing Game!");
print("Computer is thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100);

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ");
number_of_guesses = 0;
does_user_win = False;

while(difficulty_level.lower() not in ["easy", "hard"]):
    difficulty_level = input("Invalid input!\nChoose a difficulty. Type 'easy' or 'hard': ");

if(difficulty_level.lower() == "easy"):
    number_of_guesses = 10;
elif(difficulty_level.lower() == "hard"):
    number_of_guesses = 5;

while(number_of_guesses > 0):
    print(f"You have {number_of_guesses} attempts remaining to guess a number.")
    user_guess = 0;
    try:
        user_guess = int(input("Make a guess: "));
    except ValueError:
        print("Invalid input");
    while(user_guess < 1 or user_guess > 100):
        try:
            user_guess = int(input("Make a guess: "));
        except ValueError:
            print("Invalid input");

    if(user_guess > secret_number):
        print("Too High!");
    elif(user_guess < secret_number):
        print("Too Low!");
    elif(user_guess == secret_number):
        print(f"You got it! The answer was {secret_number}")
        does_user_win = True;
        break;
    
    if(number_of_guesses > 1 and (user_guess != secret_number)):
        print("Guess again.")
    number_of_guesses -= 1;

if(does_user_win == False):
    print("You've run out of guesses, you lose");
