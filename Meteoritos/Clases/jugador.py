import pygame


class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagennave = pygame.image.load("imagenes/Nave.png")
        #tomamos rectangulo imagen
        self.rect = self.imagennave.get_rect()
        #posicion inicial nave
        self.rect.centerx= 240
        self.rect.centery= 790
        self.velocidad= 10
        self.vida= True
        self.listaDisparo=[]
    def mover(self):
        if self.vida== True:
            if self.rect.left<=0:
               self.rect.left=0
            elif self.rect.right>490:
                self.rect.right=490
    def disparar(self):
        print("estoy disparando")  
    def dibujar(self, superficie):
        superficie.blit(self.imagennave, self.rect)                      