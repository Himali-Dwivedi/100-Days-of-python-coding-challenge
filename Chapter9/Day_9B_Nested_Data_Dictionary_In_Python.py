# Write your code below this line 👇

# Nested Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

for places in travel_log:
    print("I have visited:")
    for destinations in travel_log[places]:
        print(f"\t{destinations}");
    print(f"in {places}");

print(f"My Favorite place in France is {travel_log["France"][2]}");
print(f"My Favorite place in Germany is {travel_log["Germany"][1]}");


# Printing items from a nested list
nested_list = ["A", "B", ["C", "D"]];
print(nested_list[2][1]);



# Nested dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    }
}

for places in travel_log:
    print(f"I have visited {places} {travel_log[places]["total_visits"]} times and I really liked")
    for destinations in travel_log[places]["cities_visited"]:
        print(f"\t{destinations}");

print(f"My Favorite place in France is {travel_log["France"]["cities_visited"][2]}");
print(f"My Favorite place in Germany is {travel_log["Germany"]["cities_visited"][0]}");