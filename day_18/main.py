from turtle import Turtle, Screen


# Initialize the turtle
timmy_turtle = Turtle()

# Draw with the turtle
timmy_turtle.forward(100)
timmy_turtle.shape("turtle")
timmy_turtle.color("red")
timmy_turtle.forward(100)
timmy_turtle.right(90)
timmy_turtle.forward(100)
timmy_turtle.right(90)
timmy_turtle.forward(200)
timmy_turtle.right(90)
timmy_turtle.forward(100)

# Set up the screen
screen = Screen()
screen.exitonclick()  # Call the function properly