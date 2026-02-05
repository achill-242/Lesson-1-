import turtle
import random

screen = turtle.Screen()
actor = turtle.Turtle()
actor.shape("circle")
actor.shapesize(40)
actor.penup()

def move_and_change(x, y):
    actor.goto(x, y)
    actor.color(random.choice(["red", "blue", "green", "yellow", "purple"]))

screen.onclick(move_and_change)
turtle.done()
