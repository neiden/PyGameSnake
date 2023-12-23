
import pygame

class Snake:

    x_vel = 0
    y_vel = 0
    x = 150
    y = 150
    direction = ""
    size = 50
    speed = 5
    body = [pygame.Rect(x - size * 3, y, size, size), pygame.Rect(x - size * 2, y, size, size), pygame.Rect(x - size, y, size, size)]
    head = pygame.Rect(x, y, size, size)

    
    def __init__(self, size, speed):
        self.size = size
        self.speed = speed
    
    def isTouching(self, x, y, size):
        if self.x + (self.size // 2)  >= x and self.x + (self.size // 2) <= x + size and self.y + self.size >= y and self.y + self.size <= y + size:
            return True
        return False


    def move(self, keyPressed):
        if keyPressed == "right" and self.direction != "left":
            self.x_vel = self.speed
            self.y_vel = 0
            self.direction = "right"
        if keyPressed == "left" and self.direction != "right":
            self.x_vel = -self.speed
            self.y_vel = 0
            self.direction = "left"
        if keyPressed == "down" and self.direction != "up":
            self.x_vel = 0
            self.y_vel = self.speed
            self.direction = "down"
        if keyPressed == "up" and self.direction != "down":
            self.x_vel = 0
            self.y_vel = -self.speed
            self.direction = "up"
        
        self.x += self.x_vel
        self.y += self.y_vel

        self.render()

    def touchingSelf(self):
        if self.head in self.body:
            return True
        return False

    def render(self):
        tempx = self.head.x
        tempy = self.head.y 
        self.head = pygame.Rect(self.x, self.y, self.size, self.size)
        self.body[-1].x = tempx
        self.body[-1].y = tempy
        for i in range(len(self.body) - 1):
            self.body[i].x = self.body[i + 1].x
            self.body[i].y = self.body[i + 1].y

    def eat(self):
        self.body.append(pygame.Rect(5000, self.body[0].y, self.size, self.size))
    




    

