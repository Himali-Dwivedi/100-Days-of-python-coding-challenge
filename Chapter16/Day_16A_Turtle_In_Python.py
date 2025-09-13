# Write your code below this line 👇
# In this section we are going to use to build-in classes like Turtle() and Screen()
# Both Turtle() and Screen() belongs to the module trutle.
from turtle import Turtle, Screen;

# Screen() is responsible to create a canvas on which our Turtle() is going to be displayed
timmy = Turtle();
# Changing the shape of the Turtle()
timmy.shape("turtle");

# Changing the color of the Turtle()
timmy.color("coral");

# Moving the Turtle() by 100 paces
timmy.forward(100);


canvas = Screen();
# Printing the default dimensions of the canvas
print(f"Default height of the canvas is {canvas.canvheight}");
print(f"Default width of the canvas is {canvas.canvwidth}");

# The canvas should only close when we click on it
canvas.exitonclick();