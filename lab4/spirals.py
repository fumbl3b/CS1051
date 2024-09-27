import turtle
import math

screen = turtle.Screen()
turt = turtle.Turtle()
turt.speed(5)

def drawNgon(t: turtle.Turtle, numSides: int, sideLength: int) -> None:
    angle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(angle)

def drawNgonSpiral(t, numSides, sideLength, numShapes) -> None:
    for shape in range(numShapes):
        drawNgon(t, numSides, sideLength)
        offset = sideLength/numShapes
        t.right(2*math.tan(math.pi/numSides))
        t.forward(-offset)

def centerShape(t: turtle.Turtle, numSides: int, sideLength: int) -> None:
    radius = sideLength / (2 * math.sin(math.pi / numSides))
    t.penup()
    t.goto(-sideLength / 2, radius)  # Adjust the starting position
    t.setheading(0)  # Face to the right
    t.pendown()

side_length = 130
num_sides = 11
num_shapes = 3

centerShape(turt, num_sides, side_length)
drawNgonSpiral(turt, num_sides, side_length, num_shapes)

screen.mainloop()
