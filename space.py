import pgzrun
from random import randint
from PIL import Image
# img = Image.open("Images/sunset.avif")
# img.save("Images/sunset.png")

game_over = False
WIDTH = 1550
HEIGHT = 750
TITLE = "space"

space = Actor("space")
space.pos = 375,225

ufo = Actor("ufo")
ufo.pos = 300, 350

star = Actor("star")
star.pos = randint(50 , WIDTH -50) , randint(50, HEIGHT - 50)

score = 0

def draw():
    global score
    screen.clear()
    space.draw()
    ufo.draw()
    star.draw()
    screen.draw.text(f"score = {score}", color = "white" , topright = (700, 30) )
    if game_over:
        screen.fill("black")
        screen.draw.text("Game Over", color = "white", center = (WIDTH//2, HEIGHT//2)  , fontsize = 60)
        screen.draw.text(f"score = {score}", color = "pink" , topright = (700, 30) , fontsize = 40)


def update():
    global score
    if keyboard.a:
        ufo.x -= 15
        if ufo.x < 10:
            ufo.x = 10
    elif keyboard.d:
        ufo.x += 15    
        if ufo.x > WIDTH -10:
            ufo.x = WIDTH -10
    elif keyboard.s:
        ufo.y +=15
        if ufo.y > HEIGHT -10:
            ufo.y = HEIGHT -10
    elif keyboard.w:
        ufo.y -=15
        if ufo.y < 10:
            ufo.y =10
    if ufo.colliderect(star):
        star.pos = randint(50 , WIDTH -50) , randint(50, HEIGHT - 50)
        score += 1

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up , 15.0)

pgzrun.go()    