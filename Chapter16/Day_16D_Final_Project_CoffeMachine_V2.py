# Write your code below this line 👇
import Day_16D_Final_Project_CoffeeMachine_Classes as blueprints;

choosen_coffee = "";

# Creating 3 objects of Coffee()
espresso = blueprints.Coffee(name = "espresso", ingredients = {"water": 50,"milk":0,"coffee": 18}, cost = 1.5);
latte = blueprints.Coffee(name = "latte", ingredients = {"water": 200,"milk":150,"coffee": 24}, cost = 2.5);
cappuccino = blueprints.Coffee(name = "cappuccino", ingredients = {"water": 250,"milk":100,"coffee": 24}, cost = 3);

# Adding Coffee() objects to the CoffeeMachine
blueprints.CoffeeMachine.set_list_of_coffees([espresso, latte, cappuccino]);

while True:
    operation = blueprints.CoffeeMachine.print_welcome_screen();

    if(operation == "1"):
        does_user_want_coffee = blueprints.CoffeeMachine.print_report();
        if(does_user_want_coffee == "y"):
            blueprints.CoffeeMachine.take_order();
            are_resources_sufficient = blueprints.CoffeeMachine.are_resources_sufficient();
            if(are_resources_sufficient == True):
                blueprints.CoffeeMachine.handle_transaction();
            else:
                print("Ran out of resources. Can't make coffee.");
                break;
        else:
            print("Thank you for using Pycoffee. Have a great day!");
    
    elif(operation == "2"):
        blueprints.CoffeeMachine.take_order();
        are_resources_sufficient = blueprints.CoffeeMachine.are_resources_sufficient();
        if(are_resources_sufficient == True):
            blueprints.CoffeeMachine.handle_transaction();
        else:
            print("Ran out of resources. Can't make coffee.");
            break;
    if(blueprints.CoffeeMachine.does_user_want_to_continue() == False):
        break;