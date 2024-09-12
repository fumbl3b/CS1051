import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle object
t = turtle.Turtle()
t.speed(5)

# t.left(90)
# t.forward(100)

# Draw a square
for _ in range(36):
    t.circle(30)
    t.right(90)

# Keep the window open
screen.mainloop()
