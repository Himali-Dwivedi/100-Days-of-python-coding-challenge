# Write your code below this line 👇
import turtle as t;
import random;

turtle = t.Turtle();
t.colormode(255);
turtle.pensize(15);
turtle.speed("fastest");

directions= [0,90,180,270]

def random_color():
    r = random.randint(0,255);
    g = random.randint(0,255);
    b = random.randint(0,255);
    return (r, g, b);

for _ in range(200):
    turtle.pencolor(random_color());
    turtle.setheading(random.choice(directions));
    turtle.forward(30);

screen = t.Screen()
screen.exitonclick();