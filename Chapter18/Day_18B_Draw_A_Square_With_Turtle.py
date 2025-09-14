# Write your code below this line 👇
from turtle import Turtle, Screen;

turtle = Turtle();

for _ in range (4):
    turtle.right(90);
    turtle.forward(100);

screen = Screen();
screen.exitonclick();