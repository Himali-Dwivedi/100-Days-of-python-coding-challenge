# Write your code below this line 👇
# Converts the name into title case
def format_name(name):
    # Below is the docString that appears when we hover over the function name
    # This can also be used to create multi-line comments
    """Takes a name and
      format it to return the 
      tittle case version of the name"""

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