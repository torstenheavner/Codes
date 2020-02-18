import turtle
from random import *

turtle.speed(1000000000)

while True:
    turtle.forward(randint(-25, 25))
    turtle.left(randint(-25, 25))

turtle.done()
