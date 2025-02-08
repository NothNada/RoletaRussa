import pygame
from random import choice

class Arma():
    def __init__(self,img):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img,(140,120))

        self.rotated = None
        self.rotated_rect = None

        self.angle = 0
        self.angle_force = 30
        self.angle_force_add = choice((0.2,0.3,0.44,0.45))

        self.screen = pygame.display.get_surface()
    
    def restore(self):

        self.angle = 0
        self.angle_force = 30
        self.angle_force_add = choice((0.2,0.3,0.44,0.45))

        self.screen = pygame.display.get_surface()

    def update(self) -> int:
        self.rotated = pygame.transform.rotate(self.img,self.angle)
        self.rotated_rect = self.rotated.get_rect()
        self.rotated_rect.center = (self.screen.get_width()/2,(self.screen.get_height()/2)+100)

        if(self.angle>360):
            self.angle = 0
        
        self.angle += self.angle_force
        self.angle_force -= self.angle_force_add

        if(self.angle_force<=0):
            self.angle_force = 0
            if(self.angle > 180 and self.angle < 360):
                return 1
            else:
                return 0
        else:
            return 2



    def draw(self) -> None:
        self.screen.blit(self.rotated,self.rotated_rect.topleft)