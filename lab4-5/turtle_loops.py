import turtle

def drawSquare(t: turtle.Turtle, squareSize: int = 50) -> None:
    for _ in range(4):
        t.forward(squareSize)
        t.right(90)

def drawRow(t: turtle.Turtle, length: int = 5, squareSize: int = 50):
    for _ in range(length):
        drawSquare(t, squareSize)
        t.forward(squareSize)

def drawGrid(t: turtle.Turtle, size: int = 5, squareSize: int = 50):
    for _ in range(size):
        drawRow(t, size, squareSize)
        t.left(180)
        t.forward(size * squareSize)

        t.right(90)
        t.penup()
        t.forward(squareSize)
        t.pendown()
        t.right(90)

def drawSquareStairs(t: turtle.Turtle, height: int = 5, squareSize: int = 50) -> None:
    for i in range(height, 0, -1):
        drawRow(t, i, squareSize)
        t.left(180)
        t.forward(squareSize * i)

        t.right(90)
        t.penup()
        t.forward(squareSize)
        t.pendown()
        t.right(90)

def moveToPosition(t: turtle.Turtle, x: int, y: int):
    """Move turtle to a specific position without drawing."""
    t.penup()
    t.goto(x, y)
    t.pendown()

# Set up the screen and turtle
screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.speed(10)

# Draw row in the top right corner
moveToPosition(my_turtle, 150, 200)
drawRow(my_turtle, length=5, squareSize=30)

# Draw grid in the top left corner
moveToPosition(my_turtle, -230, 200)
drawGrid(my_turtle, size=5, squareSize=30)

# Draw square stairs in the bottom right corner
moveToPosition(my_turtle, 100, -100)
drawSquareStairs(my_turtle, height=5, squareSize=30)

moveToPosition(my_turtle, 0, 0)

screen.mainloop()
