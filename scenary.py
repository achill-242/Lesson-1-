import pgzrun
from random import randint
from PIL import Image
img = Image.open("Images/sunset.avif")
img.save("Images/sunset.png")

game_over = False
WIDTH = 750
HEIGHT = 450
TITLE = "sunset"

sunset = Actor("sunset")
sunset.pos = 375,225

dog = Actor("dog")
dog.pos = 300, 350

ball = Actor("ball")
ball.pos = randint(50 , WIDTH -50) , randint(50, HEIGHT - 50)

score = 0

def draw():
    global score
    screen.clear()
    sunset.draw()
    dog.draw()
    ball.draw()
    screen.draw.text(f"score = {score}", color = "white" , topright = (700, 30) )
    if game_over:
        screen.fill("black")
        screen.draw.text("Game Over", color = "white", center = (375, 225)  , fontsize = 60)
        screen.draw.text(f"score = {score}", color = "white" , topright = (700, 30) , fontsize = 40)


def update():
    global score
    if keyboard.a:
        dog.x -= 15
        if dog.x < 10:
            dog.x = 10
    elif keyboard.d:
        dog.x += 15    
        if dog.x > WIDTH -10:
            dog.x = WIDTH -10
    elif keyboard.s:
        dog.y +=15
        if dog.y > HEIGHT -10:
            dog.y = HEIGHT -10
    elif keyboard.w:
        dog.y -=15
        if dog.y < 10:
            dog.y =10

    if dog.colliderect(ball):
        ball.pos = randint(50 , WIDTH -50) , randint(50, HEIGHT - 50)
        score += 1

def time_up():
    global game_over
    game_over = True

clock.schedule(time_up , 10.0)

pgzrun.go()    