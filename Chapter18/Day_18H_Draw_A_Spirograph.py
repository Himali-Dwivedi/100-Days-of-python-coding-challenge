# Write your code below this line 👇

import turtle as t;
import random;

def random_color():
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);
    return (r, g, b);

turtle = t.Turtle()
turtle.speed("fastest");
turtle.pensize(2);
t.colormode(255);

def draw_spirograph(size_of_gap):
    for _ in range(360//size_of_gap):
        turtle.pencolor(random_color());
        turtle.circle(100);
        current_heading = turtle.heading();
        turtle.setheading(current_heading + size_of_gap);


draw_spirograph(5);

screen = t.Screen();
screen.exitonclick();