# Write your code below this line 👇
import os;
import Day_15A_Final_Project_CoffeeMachine_Data as data;

def order_a_coffee(cost_of_espresso, cost_of_latte, cost_of_cappuccino,
                   quantity_of_water, quantity_of_milk, quantity_of_coffee, amount_earned):
    are_resources_sufficient = True;
    user_coffee = input(
        f"Select your drink:\n\t[1] ☕ Espresso \t\t${cost_of_espresso}"
        f"\n\t[2] 🍵 Latte \t\t\t${cost_of_latte}"
        f"\n\t[3] 🥛 Cappuccino\t\t${cost_of_cappuccino}\nInsert your choice: ")

    while(user_coffee.lower() not in ["1", "2", "3", "espresso", "latte", "cappuccino"]):
        user_coffee = input(
            f"Invalid input!\nSelect your drink:\n\t[1] ☕ Espresso \t\t${cost_of_espresso}"
            f"\n\t[2] 🍵 Latte \t\t\t${cost_of_latte}"
            f"\n\t[3] 🥛 Cappuccino\t\t${cost_of_cappuccino}\nInsert your choice: ")

    if(user_coffee.lower() == "1" or user_coffee.lower() == "espresso"):
        choosen_coffee = "espresso"
    elif(user_coffee.lower() == "2" or user_coffee.lower() == "latte"):
        choosen_coffee = "latte"
    elif(user_coffee.lower() == "3" or user_coffee.lower() == "cappuccino"):
        choosen_coffee = "cappuccino"

    if(quantity_of_water < data.MENU[choosen_coffee]["ingredients"]["water"]):
        print("Sorry, there is not enough water.")
        are_resources_sufficient = False;
    elif(quantity_of_milk < data.MENU[choosen_coffee]["ingredients"]["milk"]):
        print("Sorry, there is not enough milk.")
        are_resources_sufficient = False;
    elif(quantity_of_coffee < data.MENU[choosen_coffee]["ingredients"]["coffee"]):
        print("Sorry, there is not enough coffee.")
        are_resources_sufficient = False;
    else:
        print("Please insert coins.")
        while True:
            try:
                inserted_quarters = int(input("How many quarters?: "))
                break
            except ValueError:
                print("Invalid input!")

        while True:
            try:
                inserted_dimes = int(input("How many dimes?: "))
                break
            except ValueError:
                print("Invalid input!")

        while True:
            try:
                inserted_nickles = int(input("How many nickles?: "))
                break
            except ValueError:
                print("Invalid input!")

        while True:
            try:
                inserted_pennis = int(input("How many pennis?: "))
                break
            except ValueError:
                print("Invalid input!")

        total_amount_paid = (inserted_quarters * 0.25) + \
                            (inserted_dimes * 0.10) + \
                            (inserted_nickles * 0.05) + \
                            (inserted_pennis * 0.01)

        print(f"You paid ${round(total_amount_paid, 2)}")

        cost_of_choosen_coffee = data.MENU[choosen_coffee]["cost"]
        water_for_choosen_coffee = data.MENU[choosen_coffee]["ingredients"]["water"]
        milk_for_choosen_coffee = data.MENU[choosen_coffee]["ingredients"]["milk"]
        coffee_for_choosen_coffee = data.MENU[choosen_coffee]["ingredients"]["coffee"]

        if(total_amount_paid < cost_of_choosen_coffee):
            print("Sorry, that's not enough money. Money refunded.")
        else:
            if(total_amount_paid > cost_of_choosen_coffee):
                print(f"Here is ${round(total_amount_paid - cost_of_choosen_coffee, 2)} in change")
            quantity_of_water -= water_for_choosen_coffee
            quantity_of_milk -= milk_for_choosen_coffee
            quantity_of_coffee -= coffee_for_choosen_coffee
            amount_earned += cost_of_choosen_coffee;
            print(f"Here is your {choosen_coffee}☕ Enjoy!")

    # return updated resources if needed
    return quantity_of_water, quantity_of_milk, quantity_of_coffee, amount_earned, are_resources_sufficient;


def clear():
    if(os.name == "nt"):
        os.system("cls");
    else:
        os.system("clear");