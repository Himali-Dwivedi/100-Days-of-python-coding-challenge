# Write your code below this line 👇
from turtle import Turtle, Screen;
import random;

turtle = Turtle();
turtle.pensize(15);
turtle.speed("fastest");

list_of_functions = [turtle.left, turtle.right];
colors = ["yellow4", "VioletRed", "turquoise", "SeaGreen", "orange", "IndianRed1", "chocolate", "cyan3"];

for _ in range(200):
    turtle.pencolor(random.choice(colors));
    random.choice(list_of_functions)(90);
    turtle.forward(30);

screen = Screen()
screen.exitonclick();