import turtle
t = turtle.Turtle()

def hexagon():
    for i in range(6):
        t.forward(60)
        t.left(60)
def plast():
    for i in range(6):
        t.forward(60)
        t.left(60)
    t.penup()
    t.forward(60)
    t.pendown()
    t.right(60)

for f in range(6):
    plast()

turtle.exitonclick()
