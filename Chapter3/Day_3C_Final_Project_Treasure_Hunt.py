# Write your code below this line 👇
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''');
is_game_completed = False;
print("Welcome to Treasure Island.");
print("Your mission is to find the treasure.");
while(is_game_completed == False):
    question1 = input("You're at a cross road. Where do you want to go? \n\tType \"left\" or \"right\" \n");
    if(question1.upper() == "RIGHT"):
        print("You fell into a hole. Game over");
        is_game_completed = True;
    elif(question1.upper() == "LEFT"):
        question2 = input("You've come to a lake. There is an island in the middle of the lake.\n\tType \"wait\" to wait for a boat. Type \"swim\" to swim across.\n");
        if(question2.upper() == "WAIT"):
            question3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yelllow and one blue.\n\tWhich door you want to choose?\n");
            if(question3.upper() == "RED"):
                print("It's a room full of fire. Game over.");
                is_game_completed = True;
            elif(question3.upper() == "YELLOW"):
                print("Congratulations! You found the treasure. You win!");
                is_game_completed = True;
            elif(question3.upper() == "BLUE"):
                print("You enter a room of beasts. Game over.");
                is_game_completed = True;
            else:
                print("You entered an invalid input. Let's start over.");
                continue;
        elif(question2.upper() == "SWIM"):
            print("You got attacked by an angry trout. Game over.");
            is_game_completed = True;
        else:
            print("You entered an invalid input. Let's start over.");
            continue;
    else:
        print("You entered an invalid input. Let's start over.");
        continue;