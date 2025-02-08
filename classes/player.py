import pygame

class Player():
    def __init__(self,img):
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img,(32*10,32*10))

        self.heart = pygame.image.load("imgs/heart.png")
        self.heart = pygame.transform.scale(self.heart,(32*1,32*1))

        self.screen = pygame.display.get_surface()

        self.life = 3

        self.choiced_time = 0

        self.choiced = False
        self.choiced_bullet = False
        self.b = None

        self.who = 2

        self.font = pygame.font.Font(None,36)
    
    def restore(self):
        self.choiced_time = 0

        self.choiced = False
        self.choiced_bullet = False
        self.b = None

        self.who = 2

    def draw(self):
        largura = self.screen.get_width()
        altura = self.screen.get_height()

        self.screen.blit(self.img,((largura/2)-(self.img.get_width()/2),(altura/2)))

        for x in range(0,self.life):
            self.screen.blit(self.heart,((largura/2)+(self.img.get_width()/2)+(self.heart.get_width())*(x),(altura/2)+(self.img.get_height()/2)))
    
    def escolha(self,balas,pc) -> int:
        """
        0 - atira nele
        1 - atira no oponente
        """
        if self.choiced == False:
            text = self.font.render("Mouse esquerdo atira em vc",True,(200,200,200))
            textR = text.get_rect()
            largura = self.screen.get_width()
            altura = self.screen.get_height()
            self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))

            text = self.font.render("Mouse direito atira nele",True,(200,200,200))
            textR = text.get_rect()
            largura = self.screen.get_width()
            altura = self.screen.get_height()
            self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)+(textR.height/2)))

            if pygame.mouse.get_pressed()[0]:
                self.choiced = True
                self.who = 0
                self.choiced_time = pygame.time.get_ticks()
            elif pygame.mouse.get_pressed()[2]:
                self.choiced = True
                self.who = 1
                self.choiced_time = pygame.time.get_ticks()
            
        if self.who == 0:
            if (pygame.time.get_ticks()-self.choiced_time)<2000:
                text = self.font.render("Vc atirou em vc",True,(200,200,200))
                textR = text.get_rect()
                largura = self.screen.get_width()
                altura = self.screen.get_height()
                self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
            if (pygame.time.get_ticks()-self.choiced_time)>2000 and (pygame.time.get_ticks()-self.choiced_time)<4000:
                if self.choiced_bullet == False:
                    self.b = balas.escolhe()
                    self.choiced_bullet = True
                    if self.b == 1:
                        self.life -= 1
                if self.b==1:
                    text = self.font.render("Era uma bala",True,(200,200,200))
                    textR = text.get_rect()
                    largura = self.screen.get_width()
                    altura = self.screen.get_height()
                    self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
                    
                elif self.b==0:
                    text = self.font.render("Nao era uma bala",True,(200,200,200))
                    textR = text.get_rect()
                    largura = self.screen.get_width()
                    altura = self.screen.get_height()
                    self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
            if (pygame.time.get_ticks()-self.choiced_time)>4000 and self.b == 0:
                return 0
            if (pygame.time.get_ticks()-self.choiced_time)>4000 and self.b == 1:
                return 1
        
        if self.who == 1:
            if (pygame.time.get_ticks()-self.choiced_time)<2000:
                text = self.font.render("Vc atirou nele",True,(200,200,200))
                textR = text.get_rect()
                largura = self.screen.get_width()
                altura = self.screen.get_height()
                self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
            if (pygame.time.get_ticks()-self.choiced_time)>2000 and (pygame.time.get_ticks()-self.choiced_time)<4000:
                if self.choiced_bullet == False:
                    self.b = balas.escolhe()
                    self.choiced_bullet = True
                    if self.b == 1:
                        pc.life -= 1
                if self.b==1:
                    text = self.font.render("Era uma bala",True,(200,200,200))
                    textR = text.get_rect()
                    largura = self.screen.get_width()
                    altura = self.screen.get_height()
                    self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
                    
                elif self.b==0:
                    text = self.font.render("Nao era uma bala",True,(200,200,200))
                    textR = text.get_rect()
                    largura = self.screen.get_width()
                    altura = self.screen.get_height()
                    self.screen.blit(text,((largura/2)-(textR.width/2),(altura/2)-(textR.height)))
            if (pygame.time.get_ticks()-self.choiced_time)>4000:
                return 1
        return 2
        