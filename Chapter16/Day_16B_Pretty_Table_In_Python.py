# Write your code below this line 👇
from prettytable import PrettyTable

table = PrettyTable();

# Adding columns with the data
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]);
table.add_column("Type", ["Electric", "Water", "Fire"]);

# Setting the alignment of the text horizontally and vertically
table.align = "l";      # Horizontal alignment to left
table.valign = "m"      # Vertical alignment to middle

print(table);