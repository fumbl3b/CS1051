import turtle

screen = turtle.Screen()

def turtle_initials(t: turtle.Turtle) -> None:
    t.goto(0,0)
    t.pensize(4)

    # draw H
    t.left(90)
    t.forward(50)
    t.right(180)
    t.forward(100)
    t.left(180)
    t.forward(50)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(50)
    t.right(180)
    t.forward(100)
    t.penup()

    # draw W
    t.goto(80,50)
    t.setheading(286)
    t.pendown()
    t.forward(104)
    t.setheading(60)
    t.forward(104)
    t.setheading(286)
    t.forward(104)
    t.setheading(73.3)
    t.forward(104)

t = turtle.Turtle()
t.speed(10)

turtle_initials(t)

screen.mainloop()
