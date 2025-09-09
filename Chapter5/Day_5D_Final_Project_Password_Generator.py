# Write your code below this line 👇
import random;
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+'];

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"));
nr_symbols = int(input("How many symbols would you like?\n"));
nr_numbers = int(input("How many numbers would you like\n"));

nr_characters = nr_letters + nr_symbols + nr_numbers;

# Start with an empty password list of the correct length
password = [None] * nr_characters
output = "";

occupied_index = [];
i = 0;
j = 0;
k = 0;
while(i < nr_letters):
        random_index = random.randint(0, nr_characters - 1);
        if(random_index not in occupied_index):
            occupied_index.append(random_index);
            password[random_index] = random.choice(letters);
            i += 1;

while(j < nr_numbers):
        random_index = random.randint(0, nr_characters - 1);
        if(random_index not in occupied_index):
            occupied_index.append(random_index);
            password[random_index] = random.choice(numbers);   
            j += 1;    

while(k < nr_symbols):
        random_index = random.randint(0, nr_characters - 1);
        if(random_index not in occupied_index):
            occupied_index.append(random_index);
            password[random_index] = random.choice(symbols);
            k += 1;

for index in range(0, len(password)):
      output += password[index];

print(output);