

from turtle import *
penup()
for step in range(5):
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