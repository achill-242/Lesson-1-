import pgzrun
from random import randint

TITLE = "catch the zombie"
WIDTH = 600
HEIGHT = 600
message = ""
score = 0


white  = Actor("white")
zombie = Actor("zombie")
zombie_alive = True


white.pos = 200, 200




def zombie_spawn():
    zombie.pos = randint(50, WIDTH - 50), randint(50, HEIGHT - 50)

def draw():
    screen.clear()
    white.draw()
    zombie.draw()
    screen.draw.text(message, center = (WIDTH//2, 50), fontsize = 40, color = "red")
    screen.draw.text(f"score: {score}", topright = (WIDTH - 60, 20), fontsize = 30, color = "blue")




def on_mouse_down(pos):
    global message, score, zombie_alive
    if zombie.collidepoint(pos) and zombie_alive == True:
        message = "You caught the zombie!"
        score += 1
        zombie_spawn()
 
            
    else:
        message = "Missed! Try again."
        score -=1
        zombie_spawn()




zombie_spawn()    

pgzrun.go()