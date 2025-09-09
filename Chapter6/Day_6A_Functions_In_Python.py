# Write your code below this line 👇
def add(a, b):
    return a + b

# Positional arguments
result = add(5, 7)
print(result)

def greet_with(name, location):
    print(f"Hello, {name}");
    print(f"How's the wether there in {location}");

# Keyword Arguments
greet_with(name= "Himali", location="Mumbai");

# Converts the name into title case
def format_name(name):
    formatted = "";
    name = name.strip();
    print(f"name.strip() = {name}");
    for index in range(0, len(name)):
        if(index == 0):
            formatted = name[index].upper();
        else:
            if(name[index - 1] == " "):
                formatted += name[index].upper();
            else:
                formatted += name[index].lower();
    return formatted;

print(format_name("   hIMALI dwiVedi   "));


# Is leap year
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
print(is_leap_year(2024));