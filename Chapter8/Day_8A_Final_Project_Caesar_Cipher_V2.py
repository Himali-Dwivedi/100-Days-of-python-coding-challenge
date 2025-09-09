# Write your code below this line 👇
from Day_8A_Final_Project_Caesar_Cipher_logo import logo;

small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

special_characters = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' '];

print(logo);

is_game_continued = True;

while is_game_continued == True:
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt\n");
    if(action.lower() != "encode" and action.lower() != "decode"):
        print("Invalid action.")
        break;

    user_input = input("Type your message:\n");
    shift_number = int(input("Type the shift number:\n"));

    if(action.lower() == "encode"):
        encrypted_message = "";
        for char in user_input:
            if char in small_letters:
                index = small_letters.index(char);
                new_index = (index + shift_number) % len(small_letters) 
                encrypted_message += small_letters[new_index];

            
            elif char in capital_letters:
                index = capital_letters.index(char);
                new_index = (index + shift_number) % len(capital_letters);
                encrypted_message += capital_letters[new_index];

            elif char in numbers:
                index = numbers.index(char);
                new_index = (index + shift_number) % len(numbers);
                encrypted_message += numbers[new_index];

            elif char in special_characters:
                index = special_characters.index(char);
                new_index = (index + shift_number) % len(special_characters) 
                encrypted_message += special_characters[new_index];
        
            else:
                encrypted_message +=char;


        print(f"Here's the encoded result: {encrypted_message}");

    elif(action.lower() == "decode"):
        decrypted_message = "";
        for char in user_input:
            if char in small_letters:
                index = small_letters.index(char);
                new_index = (index - shift_number) % len(small_letters)
                decrypted_message += small_letters[new_index];
        
            elif char in capital_letters:
                index = capital_letters.index(char);
                new_index = (index - shift_number) % len(capital_letters)
                decrypted_message += capital_letters[new_index];
        
            elif char in numbers:
                index = numbers.index(char);
                new_index = (index - shift_number) % len(numbers)
                decrypted_message += numbers[new_index];
        
            elif char in special_characters:
                index = special_characters.index(char);
                new_index = (index - shift_number) % len(special_characters)
                decrypted_message += special_characters[new_index];
        
            else:
                decrypted_message += char;
        print(f"Here's your decoded result: {decrypted_message}");

    do_want_to_continue = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n");
    if(do_want_to_continue.lower() == "no"):
        is_game_continued = False;