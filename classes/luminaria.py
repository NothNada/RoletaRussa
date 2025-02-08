from math import sin,cos,radians
import pygame

class Luminaria():
    def __init__(self,img):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img,(32*10,32*10))
        self.angle = 0
        self.screen = pygame.display.get_surface()

        self.amplitude = 8
        self.frequencia = 0.02

        self.rotated = None
        self.rotated_rect = None
    
    def rotate(self, pivot, offset):
        rotated_image = pygame.transform.rotozoom(self.img, -self.angle, 1)
        rotated_offset = offset.rotate(self.angle)
        rect = rotated_image.get_rect(center=pivot+rotated_offset)
        return rotated_image, rect
    def draw(self):
        self.rotated,self.rotated_rect = self.rotate((self.screen.get_width()/2,-50),pygame.math.Vector2(0,165))
        self.screen.blit(self.rotated,self.rotated_rect)

    def update(self):
        self.angle = self.amplitude * sin(self.frequencia*pygame.time.get_ticks()/30)
    
    def draw_light(self,dark):
        ang = self.angle + 90
        fov = 45
        ang -= fov/2
        for a in range(0,fov):
            x = self.rotated_rect.centerx
            y = self.rotated_rect.centery - (40 * sin(radians(ang+a)))
            start = (x,y)
            x += 500 * cos(radians(ang+a))
            y += 500 * sin(radians(ang+a))
            pygame.draw.line(dark,(0,0,0),start,(x,y),10)
