import turtle

screen = turtle.Screen()
t = turtle.Turtle()

def draw_triangle():
    t.pendown()
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)

draw_triangle()
t.goto(50, 86.6)
t.setheading(0)
draw_triangle()
t.setheading(300)
t.forward(100)
t.setheading(0)
draw_triangle()

screen.mainloop()
