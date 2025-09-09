# Write your code below this line 👇
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah",
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#printing the first element of the list
print(states_of_america[0]);

#printing the last element of the list
print(states_of_america[-1]);

#setting a new value to an item
states_of_america[1] = "Pencilvania";
print(states_of_america[1]);

#adding an item to the end of the list
states_of_america.append("AngelaLand");
print(states_of_america);

#adding a bunch of items to the list
states_of_america.extend(["AngelaLand2", "AngelaLand3"]);
print(states_of_america);

#Nested List
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"];
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"];
dirty_dozens = [fruits, vegetables];
print(dirty_dozens);