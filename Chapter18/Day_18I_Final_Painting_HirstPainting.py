# Write your code below this line 👇

import turtle as t;
import random;
import colorgram as cg;

rgb_colors = [];

t.colormode(255);

turtle = t.Turtle();
turtle.speed("fastest");
turtle.hideturtle();

colors = cg.extract("Chapter18/Day_18I_Final_Project_HirstPainting_Inspiration.jpeg", 180);

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b));

print(rgb_colors);

# Bringing the turtle to the bottom left corner of the screen
turtle.penup()
turtle.setheading(225);
turtle.forward(350);
turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(rgb_colors));
        turtle.penup()
        turtle.forward(50);
    turtle.left(90);
    turtle.forward(50);
    turtle.left(90);
    turtle.forward(500);
    turtle.setheading(0);

screen = t.Screen();
screen.exitonclick();