import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Turtle WASD Control")
wn.bgcolor("white")

# Create the turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()

# Define the movement functions
def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Listen for keypresses
wn.listen()
wn.onkey(move_up, "w")
wn.onkey(move_left, "a")
wn.onkey(move_down, "s")
wn.onkey(move_right, "d")

# Main loop
wn.mainloop()
