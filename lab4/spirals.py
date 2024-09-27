import turtle
import math

screen = turtle.Screen()
turt = turtle.Turtle()
turt.speed(10)

def drawNgon(t: turtle.Turtle, numSides: int, sideLength: int, angleOffset: float) -> None:
    t.right(angleOffset)

    angle = 360 / numSides
    for _ in range(numSides):
        t.forward(sideLength)
        t.right(angle)

def drawNgonSpiral(t: turtle.Turtle, numSides: int, sideLength: int, numShapes: int) -> None:
    for i in range(numShapes):
        angleOffset = (360 / numShapes) * i

        # Center the turtle
        t.penup()
        t.goto(0, 0)
        t.setheading(0)
        t.pendown()

        drawNgon(t, numSides, sideLength, angleOffset)

# Parameters for the spiral
side_length = 60
num_sides = 17
num_shapes = 10

# Draw the spiral of polygons
drawNgonSpiral(turt, num_sides, side_length, num_shapes)

screen.mainloop()
