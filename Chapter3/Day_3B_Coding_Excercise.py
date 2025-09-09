# Write your code below this line 👇
print("Welcome to Python Pizza Deliveries!")
is_bill_generated = False;

while is_bill_generated == False:
    size = input("What size pizza do you want? S, M, L: ");
    bill = 0.00;
    #todo: work out how much they need to pay based on their size choice.
    if(size.upper() == "S"):
        print("Small size pizza would cost $15");
        bill = 15.00;
    elif(size.upper() == "M"):
        print("Medium size pizza would cost $20");
        bill = 20.00
    elif(size.upper() == "L"):
        print("Large size pizza would cost $25");
        bill = 25.00
    else:
        print("Invalid input");
        continue;

    #todo: work out how much to add to their bill based on their pepperoni choice.
    pepperoni = input("Do you want pepperoni on your pizza? Y or N:");
    if(pepperoni.upper() == "Y"):
        if(size.upper() == "S"):
            print("pepperoni on small size pizza would cost extra $2")
            bill += 2;
        else:
            print("pepperoni on medium or large size pizza would cost extra $3")
            bill += 3;
    elif(pepperoni.upper() == "N"):
        print("No pepperoni it is");
    else:
        print("Invalid input");
        continue;

    #todo: work out their final amount based on whether if they want extra cheese
    extra_cheese = input("Do you want extra cheese? Y or N: ");
    if(extra_cheese.upper() == "Y"):
        print("Extra cheese would cost $1 extra");
        bill += 1;
    elif(extra_cheese == "N"):
        print("No extra cheese on your pizza");
    else:
        print("Invalid input");
        continue;

    print(f"Your total bill is: ${bill}");
    is_bill_generated = True;