# Write your code below this line 👇
import Day_15A_Final_Project_CoffeeMachine_Data as data;
import Day_15A_Final_Project_CoffeeMachine_Functions as functions;

quantity_of_water = data.resources["water"];
quantity_of_milk = data.resources["milk"];
quantity_of_coffee = data.resources["coffee"];
amount_earned = 0; 

cost_of_espresso = data.MENU["espresso"]["cost"];
cost_of_latte = data.MENU["latte"]["cost"];
cost_of_cappuccino = data.MENU["cappuccino"]["cost"];

number_of_quarters = 0;
number_of_dimes = 0;
number_of_nickles = 0;
number_of_pennies = 0;

total_amount_paid = 0;

choosen_coffee = "";

while True:
    print("=" * 45);
    print("\t☕ WELCOME TO PYCOFFEE ☕");
    print("=" *45);

    print("What would you like to do?");
    operation = input("\tPress '1' to print the report\n\tPress '2' to order a coffee\n");

    while(operation not in ["1", "2"]):
        operation = input("Invalid input!\n\tPress '1' to print the report\n\tPress '2' to order a coffee\n");

    if(operation == "1"):
        print("=" * 45);
        print("\t☕ RESOURCES AVAILABLE ☕");
        print("=" *45);
        print(f"\t\tWater: {quantity_of_water}ml\n\t\tMilk: {quantity_of_milk}ml\n\t\tCoffee: {quantity_of_coffee}g\n\t\tMoney: ${amount_earned}")
        
        does_user_want_coffee = input("Would you like to order a coffee? Press 'y' to order a coffee. Otherwise, press 'n': ");
        while(does_user_want_coffee.lower() not in ["y", "n"]):
            does_user_want_coffee = input("Invalid input!\nWould you like to order a coffee? Press 'y' to order a coffee. Otherwise, press 'n': ");
        
        if(does_user_want_coffee.lower() == "y"):
            quantity_of_water, quantity_of_milk, quantity_of_coffee, amount_earned = functions.order_a_coffee(cost_of_espresso = cost_of_espresso, cost_of_latte = cost_of_latte, cost_of_cappuccino = cost_of_cappuccino, quantity_of_water = quantity_of_water, quantity_of_milk = quantity_of_milk, quantity_of_coffee = quantity_of_coffee, amount_earned = amount_earned);
        else:
            print("Thank you for using Pycoffee. Have a great day!");

    elif(operation == "2"):
        quantity_of_water, quantity_of_milk, quantity_of_coffee, amount_earned = functions.order_a_coffee(cost_of_espresso = cost_of_espresso, cost_of_latte = cost_of_latte, cost_of_cappuccino = cost_of_cappuccino, quantity_of_water = quantity_of_water, quantity_of_milk = quantity_of_milk, quantity_of_coffee = quantity_of_coffee, amount_earned = amount_earned);

    does_user_want_to_use_it_again = input("Do you want to use it again? (y/n): ")
    while(does_user_want_to_use_it_again.lower() not in ["y", "n"]):
        does_user_want_to_use_it_again = input("Invalid input!\nDo you want to use it again? (y/n): ");

    if(does_user_want_to_use_it_again.lower() == "n"):
        break;
    elif(does_user_want_to_use_it_again.lower() == "y"):
        functions.clear();