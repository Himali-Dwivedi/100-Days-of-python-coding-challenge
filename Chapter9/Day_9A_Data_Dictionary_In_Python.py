# Write your code below this line 👇
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

# Printing an item from the dictionary
print(programming_dictionary["Bug"]);

# Adding a new item to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary);

# Creating an empty dictionary
empty_dictionary = {};
print(empty_dictionary);

# Wiping an existing dictionary
programming_dictionary = {}
print(programming_dictionary);

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"]);



# Loop through a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
}

for key in programming_dictionary:
    print(f"\"{key}\" : \"{programming_dictionary[key]}\"")