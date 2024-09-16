import turtle

screen = turtle.Screen()

#initialize the turtle

def turtle_clock(t: turtle.Turtle) -> None:
    t.penup()
    t.color("black")
    t.goto(0,0)
    step = 360 / 12
    for i in range(12):
        t.forward(90)
        t.pendown()
        t.forward(20)
        t.stamp()
        t.penup()
        t.left(180)
        t.forward(110)
        t.left(180)
        t.right(step)

t = turtle.Turtle()
t.speed(10)

turtle_clock(t)

screen.mainloop()
