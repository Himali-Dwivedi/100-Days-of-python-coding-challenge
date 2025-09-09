# Write your code below this line 👇
#For loop with range()
#range() itself doesn't do anything. We have to use it in conjunction with for loop. For example,
print(range(1, 10));

#range() includes the lower limit but not the upper limit
sum = 0;
for number in range(1, 101):
    sum += number;
print(f"The sum of numbers between 1 to 100 is: {sum}");

#range() can also include steps which basically means how much to increase/decrease each time (default = 1)
for number in range(1, 11, 3):
    print(number);