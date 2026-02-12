from random import randint
import pgzrun
from time import time


WIDTH = 750
HEIGHT = 450
TITLE = "connecting satellites"

sat_list = [] #list of satellites
lines= [] #list of lines

no_of_sat = 8

start_time = 0
total_time = 0
end_time = 0


next_sat = 0

def satellite_setup():
    global start_time
    for i in range(no_of_sat):
        sat = Actor("satelite")
        sat.pos = randint(40, WIDTH - 40), randint(40, HEIGHT - 40) 
        sat_list.append(sat)
    start_time = time()
    


def draw():
    global total_time
    screen.blit("background", (0,0))

    num = 1 
    for sat in sat_list:
        sat.draw()
        screen.draw.text(str(num), (sat.pos[0], sat.pos[1] + 20), fontsize=30, color="white")
        num += 1
    for x in lines:
        screen.draw.line(x[0], x[1], color="white")



    if next_sat < no_of_sat:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time, 1)), (10, 10), fontsize=30, color="white")

    else:
        screen.draw.text(str(round(total_time, 1)), (10, 10), fontsize=30, color="white")





def update():
    pass

def on_mouse_down(pos):
    global next_sat, lines

    if next_sat < no_of_sat:
        if sat_list[next_sat].collidepoint(pos):
            if next_sat:
                lines.append((sat_list[next_sat - 1].pos, sat_list[next_sat].pos))
            next_sat += 1
        else:
            lines = []
            next_sat = 0



satellite_setup()
pgzrun.go()