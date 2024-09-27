import turtle
import math
# from turtle_loops import moveToPosition

screen = turtle.Screen()
turt = turtle.Turtle()
turt.speed(5)

def drawNgon(t: turtle.Turtle, numSides: int, sideLength: int) -> None:
    angle = 360/numSides

    for side in range(numSides):
        t.forward(sideLength)
        t.right(angle)

def centerShape(t: turtle.Turtle, numSides: int, sideLength: int) -> None:
    # Calculate the radius of the polygon
    radius = sideLength / (2 * math.sin(math.pi/ numSides))

    # Move to the starting position for centering
    t.penup()
    t.setheading(0)
    t.left(360/(numSides*2))
    t.forward(radius)
    t.setheading(90)
    t.pendown()

side_length = 100
num_sides = 8
centerShape(turt, num_sides, side_length)
drawNgon(turt, num_sides, side_length)

screen.mainloop()
