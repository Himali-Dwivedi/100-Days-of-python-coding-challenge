# Write your code below this line 👇
import random;

#randInt() generates a random number between the given range, including the lower and upper limit.
random_integer = random.randint(1, 10);
print(random_integer);

#random() generates a random float number between 0 and 1, including 0 and excluding 1.
random_number_0_to_1 = random.random();
print(random_number_0_to_1);

#uniform() generates a random floating number between the given range, including the lower and upper limit.
random_float = random.uniform(1, 10);
print(random_float);

#Code that generates a random Heads and Tails value
random_value = random.randint(1,2);
if(random_value == 1):
    print("Heads");
else:
    print("Tails");