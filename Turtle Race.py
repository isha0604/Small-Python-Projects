#Program to create a turtle race game

from turtle import *
from random import randint
speed(10)
penup()
goto(-140,140)
for step in range(10):
    write(step,align = 'center')
    right(90)
    forward(10)
    pendown()
    for i in range(10):

              forward(8)
              penup()
              forward(8)
              penup()
              forward(8)
              pendown()

    penup()
    backward(250)
    left(90)
    forward(30)
"""for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(30)"""



tur1 = Turtle()
tur1.color('red')
tur1.shape('turtle')
tur1.penup()
tur1.goto(-160,100)
tur1.pendown()

tur2 = Turtle()
tur2.color('violet')
tur2.shape('turtle')
tur2.penup()
tur2.goto(-160,70)
tur2.pendown()

tur3 = Turtle()
tur3.color('orange')
tur3.shape('turtle')
tur3.penup()
tur3.goto(-160,40)
tur3.pendown()

for turn in range(10):
    tur1.right(36)
    tur2.right(36)
    tur3.right(36)

for turn in range(100):
    tur1.forward(randint(1,5))
    tur2.forward(randint(1,5))
    tur3.forward(randint(1,5))






