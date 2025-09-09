# Write your code below this line 👇
def convertStringToBoolean(userResponse):
    if(userResponse.upper() == "Y" or userResponse.upper() == "YES"):
        return True;
    elif(userResponse.upper() == "N" or userResponse.upper() == "NO"):
        return False;

print("Welcome to the rollercoaster!");
payment = 0;
height = int(input("What's your height in cm? "));
if(height <= 120):
    print("Sorry, you have to grow taller before you can ride");
else:
    print("You can ride the rollercoaster");
    age = int(input("What's your age? "));
    if(age < 12):
        print("Child tickets are $5");
        payment = 5;
    elif(age >= 12 and age <= 18):
        print("Youth tickets are $7");
        payment = 7
    else:
        print("Adult tickets are $12");
        payment = 12;
    want_photo = convertStringToBoolean(input("Do you want to purchase a ticket that includes photo. It would cost $3 extra? (Y/N)"));
    if(want_photo == True):
        payment += 3;
    print(f"please pay {payment}"); 


# Logical Operators:
# and
# or
# not