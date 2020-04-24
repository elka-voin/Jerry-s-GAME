import pygame
from random import choice, randint

#картинки
images = [] 
images.append (pygame.image.load("1.png"))  
images.append (pygame.image.load("2.png")) 
images.append (pygame.image.load("3.png")) 
for i in range (3):
    image = images[i]
    image = pygame.transform.scale(image,(160,200))
    images [i] = image 

class Balloon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = choice(images)
        self.rect = self.image.get_rect()
        self.speed  = 10
        self.rect.y = 750
        self.rect.x = randint (10,390)
    def update(self):
        self.rect.y -= self.speed
    def check_pos (self):   
        if self.rect.bottom < 0:
            return False
        else:
            return True    