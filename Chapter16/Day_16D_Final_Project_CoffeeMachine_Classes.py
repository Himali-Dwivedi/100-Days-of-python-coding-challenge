# Write your code below this line 👇
import os;

class Coffee:
    # Creating a constructor
    def __init__(self, name, ingredients = {"water": 0, "milk": 0, "coffee": 0}, cost = 0):
        self.__name = name;
        self.__ingredients = ingredients;       # Setting private attributes
        self.__cost = cost;                     # Setting private attributes

    # Defining Getters and Setters
    def set_name(self, name):
        self.__name = name;
    
    def get_name(self):
        return self.__name;

    def set_ingredients(self, ingredients):
        self.__ingredients = ingredients;

    def get_ingredients(self):
        return self.__ingredients;

    def set_cost(self, cost):
        self.__cost = cost;

    def get_cost(self):
        return self.__cost;

class CoffeeMachine:
    # Creating a static attribute
    __list_of_coffees = [];
    __money_earned = 0;
    __available_water = 300;
    __available_milk = 200;
    __available_coffee = 100;
    __choosen_coffee = "";

    @classmethod
    def set_available_water(cls, available_water):
        cls.__available_water = available_water;
    
    @classmethod
    def get_available_water(cls):
        return cls.__available_water;

    @classmethod
    def set_available_milk(cls, available_milk):
        cls.__available_milk = available_milk;
    
    @classmethod
    def get_available_milk(cls):
        return cls.__available_milk;

    @classmethod
    def set_available_coffee(cls, available_coffee):
        cls.__available_coffee = available_coffee;

    @classmethod
    def get_available_coffee(cls):
        return cls.__available_coffee;

    @classmethod
    def set_money_earned(cls, money_earned):
        cls.__money_earned = money_earned;

    @classmethod
    def get_money_earned(cls):
        return cls.__money_earned;

    @classmethod
    def set_choosen_coffee(cls, choosen_coffee):
        cls.__choosen_coffee = choosen_coffee;
    
    @classmethod
    def get_choosen_coffee(cls):
        return cls.__choosen_coffee;

    @classmethod
    def set_list_of_coffees(cls, list_of_coffees):
        cls.__list_of_coffees = list_of_coffees;

    @classmethod
    def get_list_of_coffees(cls):
        return cls.__list_of_coffees;

    @classmethod
    def print_welcome_screen(cls):
        print("=" * 45);
        print("\t☕ WELCOME TO PYCOFFEE ☕");
        print("=" *45);

        print("What would you like to do?");
        operation = input("\tPress '1' to print the report\n\tPress '2' to order a coffee\n");

        while(operation not in ["1", "2"]):
            operation = input("Invalid input!\n\tPress '1' to print the report\n\tPress '2' to order a coffee\n");
        return operation;

    @classmethod
    def print_report(cls):
        print("=" * 45);
        print("\t☕ RESOURCES AVAILABLE ☕");
        print("=" *45);
        print(f"\t\tWater: {cls.get_available_water()}ml\n\t\tMilk: {cls.get_available_milk()}ml\n\t\tCoffee: {cls.get_available_coffee()}g\n\t\tMoney: ${cls.get_money_earned()}");
        does_user_want_coffee = input("Would you like to order a coffee? Press 'y' to order a coffee. Otherwise, press 'n': ");
        while(does_user_want_coffee.lower() not in ["y", "n"]):
            does_user_want_coffee = input("Invalid input!\nWould you like to order a coffee? Press 'y' to order a coffee. Otherwise, press 'n': ");
        return does_user_want_coffee.lower();

    @classmethod
    def take_order(cls):
        counter = 1;
        print("Select your drink:");
        for coffee in cls.get_list_of_coffees():
            print(f"\t[{counter}] ☕ {coffee.get_name()} \t\t${coffee.get_cost()}");
            counter += 1;
        user_coffee = input("\nInsert your choice: ");

        counter = 1;
        while(user_coffee.lower() not in ["1", "2", "3", "espresso", "latte", "cappuccino"]):
            print("Select your drink:");
            for coffee in cls.get_list_of_coffees():
                print(f"\t[{counter}] ☕ {coffee.get_name()} \t\t${coffee.get_cost()}");
                counter += 1;
            user_coffee = input("\nInsert your choice: ");

        if(user_coffee.lower() == "1" or user_coffee.lower() == "espresso"):
            choosen_coffee = "espresso"
        elif(user_coffee.lower() == "2" or user_coffee.lower() == "latte"):
            choosen_coffee = "latte"
        elif(user_coffee.lower() == "3" or user_coffee.lower() == "cappuccino"):
            choosen_coffee = "cappuccino"
        cls.set_choosen_coffee(choosen_coffee = choosen_coffee);

    @classmethod
    def are_resources_sufficient(cls):
        choosen_coffee = cls.get_choosen_coffee();
        for coffee in cls.get_list_of_coffees():
            if(choosen_coffee == coffee.get_name()):
                if(cls.get_available_water() < coffee.get_ingredients()["water"]):
                    print("Sorry, there is not enough water.");
                    return False;
                elif(cls.get_available_milk() < coffee.get_ingredients()["milk"]):
                    print("Sorry, there is not enough milk.");
                    return False;
                elif(cls.get_available_coffee() < coffee.get_ingredients()["coffee"]):
                    print("Sorry, there is not enough coffee.");
                    return False;
        return True;

    @classmethod
    def handle_transaction(cls):
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

        print(f"You paid ${round(total_amount_paid, 2)}");
        
        for coffee in cls.get_list_of_coffees():
            if(coffee.get_name() == cls.get_choosen_coffee()):
                if(total_amount_paid < coffee.get_cost()):
                    print("Sorry, that's not enough money. Money refunded.");
                else:
                    if(total_amount_paid > coffee.get_cost()):
                        print(f"Here is ${round(total_amount_paid - coffee.get_cost(), 2)} in change");
                        cls.set_available_water(cls.get_available_water() - coffee.get_ingredients()["water"]);
                        cls.set_available_water(cls.get_available_milk() - coffee.get_ingredients()["milk"]);
                        cls.set_available_water(cls.get_available_coffee() - coffee.get_ingredients()["coffee"]);
                        cls.set_money_earned(cls.get_money_earned() + coffee.get_cost());
                        print(f"Here is your {cls.get_choosen_coffee()}☕ Enjoy!");

    @classmethod
    def clear(cls):
        if(os.name == "nt"):
            os.system("cls");
        else:
            os.system("clear");

    @classmethod
    def does_user_want_to_continue(cls):
        does_user_want_to_use_it_again = input("Do you want to use it again? (y/n): ")
        while(does_user_want_to_use_it_again.lower() not in ["y", "n"]):
            does_user_want_to_use_it_again = input("Invalid input!\nDo you want to use it again? (y/n): ");

        if(does_user_want_to_use_it_again.lower() == "n"):
            return False;
        elif(does_user_want_to_use_it_again.lower() == "y"):
            cls.clear();
            return True;
        
