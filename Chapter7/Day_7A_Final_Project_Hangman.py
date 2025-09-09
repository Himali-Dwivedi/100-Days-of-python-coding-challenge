# Write your code below this line 👇
import random;
from Day_7A_Final_Project_Hangman_States import hangman, logo;
from Day_7A_Final_Project_Hangman_Words import word_list as words;

print(logo + "\n");

random_word = random.choice(words);

number_of_lives = 6;

is_game_completed = False;

hangman_state = 0;

# Creating an empty list of guessed characters
guessed_chars = ["_"] * len(random_word);

# Printing the hint to guess the word
output_string = "";
for index in range(0, len(guessed_chars)):
    output_string += guessed_chars[index];
print(f"Your word is: {output_string}\n");

while(number_of_lives > 0 and is_game_completed == False):
    print(f"*********************{number_of_lives}/6 LIVES LEFT*********************")
    letter_index = [];
    user_input = input("Guess the letter:\n").lower();
    if user_input in random_word:
        for index in range(0, len(random_word)):
            # Capturing the occurences of a character that matches the user input
            if(random_word[index] == user_input):
                letter_index.append(index);
        
        # Setting the user input to the right positions
        for index in letter_index:
            guessed_chars[index] = user_input;
        output_string = "";

        for index in range(0, len(guessed_chars)):
            output_string += guessed_chars[index];
        print(f"Your word is: {output_string}");
        print(hangman[hangman_state]);

        if(random_word == output_string):
            print("*********************YOU WIN*********************");
            is_game_completed = True;
    else:
        number_of_lives -= 1;
        print(f"You gussed {user_input}, that's not in the word. You loose a life,")
        print(f"Your word is {output_string}");
        if(number_of_lives > 0):
            hangman_state  = 6 - number_of_lives
            print(hangman[hangman_state]);
        elif(number_of_lives == 0):
            hangman_state = 6;
            print(hangman[hangman_state]);
            print(f"Correct word was \"{random_word}\"");
            print("*********************YOU LOOSE*********************");