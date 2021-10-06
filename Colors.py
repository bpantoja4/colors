#Initialization
import turtle
import random
brianna=turtle.Turtle()
brianna.colormode(255)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
#Functions
def randomDot():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    brianna.color(r,g,b)
    brianna.begin_fill()
    brianna.circle(100)
    brianna.end_fill()
#Main
for i in range(5):
	randomDot()
