# Write your code below this line 👇
import random;
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper,scissors];
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if(user_choice != "0" and user_choice != "1" and user_choice != "2"):
    print("Invalid user input");
else:
    computer_choice_int = random.randint(0,2);
    user_choice_int = int(user_choice);
    print(f"You choose:\n{options[user_choice_int]}");
    print(f"Computer choose:\n{options[computer_choice_int]}");
    if (computer_choice_int == user_choice_int):
        print("It's a tie");
    elif(computer_choice_int == 0 and user_choice_int == 1):
        print("You win");
    elif(computer_choice_int == 0 and user_choice_int == 2):
        print("Computer win");
    elif(computer_choice_int == 1 and user_choice_int == 0):
        print("Computer win");
    elif(computer_choice_int == 1 and user_choice_int == 2):
        print("You win");
    elif(computer_choice_int == 2 and user_choice_int == 0):
        print("You win");
    elif(computer_choice_int == 2 and user_choice_int == 1):
        print("Computer win");
