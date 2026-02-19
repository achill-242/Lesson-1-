from random import randint
from tracemalloc import start
import pgzrun
from time import time


WIDTH = 750
HEIGHT = 450
TITLE = "constellation of stars"

star_list = [] #list of star
lines= [] #list of lines

no_of_star = 10

start_time = 0
total_time = 0
end_time = 0


next_star = 0

def star_setup():
    global start_time
    for i in range(no_of_star):
        star = Actor("star")

        star.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40) 
        star_list.append(star)
    start_time = time()
    


def draw():
    global total_time
    screen.blit("background", (0,0))

    num = 1 
    for star in star_list:
        star.draw()
        screen.draw.text(str(num), (star.pos[0], star.pos[1] + 20), fontsize=30, color="white")
        num += 1
    for x in lines:
        screen.draw.line(x[0], x[1], color="white")



    if next_star < no_of_star:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)), (10, 10), fontsize=30, color="white")

    else:
        screen.draw.text(str(round(total_time, 1)), (10, 10), fontsize=30, color="white")





def update():
    pass

def on_mouse_down(pos):
    global next_star, lines

    if next_star < no_of_star:
        if star_list[next_star].collidepoint(pos):
            if next_star:
                lines.append((star_list[next_star - 1].pos, star_list[next_star].pos))
            next_star += 1
        else:
            lines = []
            next_star = 0



star_setup()
pgzrun.go()