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
morty = pygame.image.load("morty.png")
sanches = pygame.image.load("RICK.png")
#sanches.convert_alpha()    

class Balloon(pygame.sprite.Sprite):
    def __init__(self,image = "balloon"):
        pygame.sprite.Sprite.__init__(self)
        if image =="balloon":            
            self.image = choice(images)
        elif image == "morty":
            self.image = pygame.transform.scale(morty,(160,200))
        elif image == "rick":
            self.image = pygame.transform.scale(sanches,(160,200))
        self.rect = self.image.get_rect()
        self.speed  = 10
        self.rect.y = 750
        self.rect.x = randint (10,790)
        self.sanches_mode = False
        self.cick = 1
    def update(self):

        self.rect.y -= self.speed
    def check_pos (self):   
        if self.rect.bottom < 0:
            return False
        else:
            return True    

class Head(Balloon):
    def __init__(self):
        Balloon.__init__(self)
        self.image = pygame.image.load ("HEAD.png") 
        self.image = pygame.transform.scale(self.image,(190,220))
        self.rect = self.image.get_rect()
        self.speed  = 25
        self.rect.y = 750
        self.rect.x = randint (10,790)       
        self.cick = 666

class Jerry(Balloon):
    def __init__(self):
        Balloon.__init__(self)
        self.image = pygame.image.load ("Jerry.png") 
        self.image = pygame.transform.scale(self.image,(170,220))
        self.rect = self.image.get_rect()
        self.speed  = 1
        self.rect.y = 750
        self.rect.x = randint (10,790)       

class Summer(Balloon):
    def __init__(self):
        Balloon.__init__(self)
        self.image = pygame.image.load ("Summer.png") 
        self.image = pygame.transform.scale(self.image,(170,220))
        self.rect = self.image.get_rect()
        self.speed  = 9
        self.rect.y = 750
        self.rect.x = randint (10,790)

class Beth(Balloon):
    def __init__(self):
        Balloon.__init__(self)
        self.image = pygame.image.load ("Beth.png") 
        self.image = pygame.transform.scale(self.image,(170,220))
        self.rect = self.image.get_rect()
        self.speed  = 7
        self.rect.y = 750
        self.rect.x = randint (10,790)
