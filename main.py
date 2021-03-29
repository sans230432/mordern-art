import turtle 
import random

turtle.shape("turtle")
turtle.speed(0)

for i in range(1500):
  red = random.randint(0, 255)
  blue = random.randint(0, 255)
  green = random.randint(0,255)

  turtle.color(red, green, blue)
  turtle.forward(10)

  x =  random.randint(-300, 300)
  y = random.randint(-300, 300)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()

  l = random.randint(10, 100)
  h = random.randint(10, 100)
  turtle.begin_fill()
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(h)
  turtle.right(90)
  turtle.forward(l)
  turtle.right(90)
  turtle.forward(h)
  turtle.right(90)
  turtle.end_fill()

ex = random.randint(-300, 300)
why = random.randint(-300, 300)
turtle.penup()
turtle.goto(x,y)
turtle.pendown()

radius = random.randint(10, 50)
turtle.being_fill()
turtle.circle(radius)
turtle.end_fill()

