
import pygame
import snakeClass
import time
import random
import sys

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
pygame.init()
background_color = (234, 212, 252) 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake') 
screen.fill(background_color) 

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('SCORE', True, (0, 255, 0), (0, 0, 128))


snakeX = 50
snakeY = 150
snakeSize = 50
x_vel = 0
y_vel = 0
food = []

snake = snakeClass.Snake(50, 50)


keyPressed = "right"

#[] - [] - [] - []>

def tick(keyPressed):
    snake.move(keyPressed)
    if isCollided():
        gameOver()
    screen.fill(background_color)
    print(food)
    pygame.draw.rect(screen, (255 ,0 ,0), snake.head)
    for body in snake.body[::-1]:
        pygame.draw.rect(screen, (255, 0, 0), body)
    for f in food:
        pygame.draw.rect(screen, (0, 255, 0), f)
        if snake.isTouching(f.x, f.y, f.size[0]):
            snake.eat()
            food.remove(f)
        

def isCollided():
    if snake.touchingSelf() or snake.x > SCREEN_WIDTH - snake.size or snake.x < 0 or snake.y > SCREEN_HEIGHT - snake.size or snake.y < 0:
        return True
    return False

def gameOver():
    screen.fill(background_color)
    pygame.quit()
    sys.exit()


def spawnFood():
    global food
    randY = random.randint(1, SCREEN_HEIGHT / 50)
    randX = random.randint(1, SCREEN_WIDTH / 50)
    food.append(pygame.Rect(randX * 50, randY * 50, 50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyPressed = "left"
            if event.key == pygame.K_RIGHT:
                keyPressed = "right"
            if event.key == pygame.K_DOWN:
                keyPressed = "down"
            if event.key == pygame.K_UP:
                keyPressed = "up"
    
    #loop
    #change player x by xVel
    if pygame.time.get_ticks() % 50 == 0:
        tick(keyPressed)
    if len(food) < 3:
        spawnFood()

    
            
    #render
    


    pygame.display.flip()
