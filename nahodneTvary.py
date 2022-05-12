import turtle
from random import *

po = 100  # sem zadaj svoj pocet opakovani
print("Nakreslim", po, "tvarov")

t = turtle.Turtle()
turtle.colormode(255)
t.speed(1000)


def random():
    t.left(randint(0, 360))
    a = randrange(-150, 150)
    b = randrange(-150, 150)
    dlzka = randrange(75)
    tvar = randrange(1, 5)
    print("Kreslim:", tvar)  # 1 = stvorec, 2 = trojuholnik, 3 = kruh, 4 = pentagon

    pohyb(a, b)

    if tvar == 1:
        stvorec(dlzka)
    elif tvar == 2:
        trojuholnik(dlzka)
    elif tvar == 3:
        dlzka = dlzka % 4
        kruh(dlzka)
    elif tvar == 4:
        pentagon(dlzka)


def kreslitvar(side, dlzka):
    ang = 360.0 / side
    for side in range(side):
        t.forward(dlzka)
        t.right(ang)


def pohyb(a, b):
    t.penup()
    t.goto(a, b)
    t.pendown()


def stvorec(dlzka):
    kreslitvar(4, dlzka)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


def trojuholnik(dlzka):
    kreslitvar(3, dlzka)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


def kruh(dlzka):
    kreslitvar(360, dlzka)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


def pentagon(dlzka):
    kreslitvar(5, dlzka)
    t.color(randint(0, 255), randint(0, 255), randint(0, 255))


for tvar in range(po):
    random()

turtle.exitonclick()
