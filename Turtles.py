from turtle import *
from random import randint

speed(0)
penup()
goto(-120, 120)

for step in range(10):
    write(step, align='center')
    right(90)
    # forward(10)
    pendown()
    forward(150)
    penup()
    backward(150)
    left(90)
    forward(20)

    ada = Turtle()
    ada.color('red')
    ada.shape('turtle')

    ada.penup()
    ada.goto(-135, 100)
    ada.pendown()

    thy = Turtle()
    thy.color('black')
    thy.shape('turtle')

    thy.penup()
    thy.goto(-135, 75)
    thy.pendown()

    bob = Turtle()
    bob.color('blue')
    bob.shape('turtle')

    bob.penup()
    bob.goto(-135, 50)
    bob.pendown()

    sam = Turtle()
    sam.color('magenta')
    sam.shape('turtle')

    sam.penup()
    sam.goto(-135, 25)
    sam.pendown()

    that = Turtle()
    that.color('green')
    that.shape('turtle')

    that.penup()
    that.goto(-135, 0)
    that.pendown()

for turn in range(1):
    thy.left(360)
    bob.right(360)
    ada.right(360)
    sam.left(360)
    that.left(360)

for turn in range(60):
    ada.right(36)
    ada.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    sam.forward(randint(1, 5))
    that.forward(randint(1, 5))
    thy.forward(randint(1, 5))