import turtle

screen = turtle.Screen()

#initialize the turtle

def turtle_olympics(t: turtle.Turtle) -> None:
    def draw_circle(color: str):
        t.pendown()
        t.color(color)
        t.circle(40)
        t.penup()
    t.pensize(3)
    t.penup()
    t.goto(-60, 0)
    draw_circle("blue")
    t.goto(-30, -30)
    draw_circle("yellow")
    t.goto(0,0)
    draw_circle("black")
    t.goto(30,-30)
    draw_circle("green")
    t.goto(60, 0)
    draw_circle("red")
    t.penup()

t = turtle.Turtle()
turtle_olympics(t)

screen.mainloop()
