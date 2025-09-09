# Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"));
tip_in_percentage = int(input("How much tip would you like to give? 10, 12 or 15? "));
number_of_people = int(input("How many people to split the bill? "));

actual_tip = (tip_in_percentage/100) * bill;
total_bill = bill + actual_tip;
bill_per_person = total_bill/number_of_people;

print(f"Each person should pay: ${round(bill_per_person, 2)}");