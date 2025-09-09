# Write your code below this line 👇
# Write a program that randomly prints a value from a list
import random;

friends = ["Rachel", "Monica", "Pheobe", "Ross", "Chandler", "Joey"];

#Approach 1
random_index = random.randint(0, len(friends) - 1);
print(f"{friends[random_index]} should pay the bill.");

#Approach 2
print(f"{random.choice(friends)} should pay the bill");