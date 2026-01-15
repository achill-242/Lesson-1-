import pgzrun

from random import randint


# width and height of the output window
WIDTH = 700
HEIGHT = 700

TITLE = "Drawing"

def draw():
    R = 255
    G = randint(1,255)
    B = 125

    # width and height of the rectangle
    width = WIDTH
    height = HEIGHT


    for i in range(40):
        rect = Rect((0,0),(width, height))

        rect.center = 350,350

        screen.draw.rect(rect,(R,G,B))

        R -= 5 
        B += 3
        width -= 10
        height -= 10


pgzrun.go()