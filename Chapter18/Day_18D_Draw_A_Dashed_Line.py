# Write your code below this line 👇
from turtle import Turtle, Screen;

turtle = Turtle();

number_of_paces = 50;

for _ in range(number_of_paces):
    turtle.penup();
    turtle.forward(10);
    turtle.pendown();
    turtle.forward(10);


screen = Screen()
screen.exitonclick();