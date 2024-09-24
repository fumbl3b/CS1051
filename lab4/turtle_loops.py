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
        t.forward(size*squareSize)

        t.right(90)
        t.penup()
        t.forward(squareSize)
        t.pendown()
        t.right(90)


screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.speed(10)

drawGrid(my_turtle)
my_turtle.penup()
my_turtle.setpos(0,0)

# my_turtle.forward(50)
# my_turtle.right(90)

screen.mainloop()

# drawSquare(my_turtle, 50)
