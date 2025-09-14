# Write your code below this line 👇
from turtle import Turtle, Screen;
import random;

turtle = Turtle()
number_of_sides = [3,4,5,6,7,8,9,10];
colors = ["yellow4", "VioletRed", "turquoise", "SeaGreen", "orange", "IndianRed1", "chocolate", "cyan3"]

for sides in number_of_sides:
    turtle.pencolor(random.choice(colors));
    for i in range(sides):
        turtle.forward(100);
        turtle.left(360/sides);

screen = Screen();
screen.exitonclick();