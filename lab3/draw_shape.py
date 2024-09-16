import turtle

screen = turtle.Screen()

t = turtle.Turtle()
t.shape("turtle")

while(True):
    sides = int(input("Please enter the number of sides of the shape: "))

    side_length = (2*3.1415*(100/sides))
    angle = 360/sides

    for n in range(sides):
        t.forward(side_length)
        t.left(angle)


screen.mainloop()
