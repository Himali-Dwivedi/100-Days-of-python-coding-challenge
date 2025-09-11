# Write your code below this line 👇
from Day_10B_Final_Project_Calculator_Logo import logo;

def addition(a, b):
    return(a + b);

def substraction(a, b):
    return(a - b);

def multiplication(a, b):
    return(a * b);

def division(a, b):
    return(round(a / b, 2));

result = 0.0;
is_calculation_over = False;

print(logo);
number1 = int(input("What's the first number?: "));
while(is_calculation_over == False):
    print("+\n-\n*\n/");
    operation = input("Pick an operation: ");
    if(operation != "+" and operation != "-" and operation != "*" and operation != "/"):
        print("Invalid Operation");
    number2 = int(input("What's the second number?: "))

    if(operation == "+"):
        result = float(addition(a = number1, b = number2));
    elif(operation == "-"):
        result = float(substraction(a = number1, b = number2));
    elif(operation == "*"):
        result = float(multiplication(a = number1, b = number2));
    elif(operation == "/"):
        result = float(division(a = number1, b = number2));

    print(f"{float(number1)} {operation} {float(number2)} = {result}");

    want_to_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ");
    if(want_to_continue.lower() == "n"):
        is_calculation_over = True;
    elif(want_to_continue.lower() == "y"):
        number1 = result;
    else:
        break;