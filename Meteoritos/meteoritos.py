import pygame 
import sys
from pygame.locals import *
# importar clases
from Clases import jugador
# variables
ANCHO = 480
ALTO = 700
#booleano juego
jugando = True
# funcion principal


def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # imagen de fondo
    fondo = pygame.image.load("imagenes/fondo2.png")
    ventana.blit(fondo,(0, 0))
    # titulo
    pygame.display.set_caption("Meteoritos")
    #crea objeto jugador
    nave = jugador.Nave()
    #ciclo de juego
    while True:

        ventana.blit(fondo,(0, 0))
        nave.dibujar(ventana)
        nave.mover()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# llamada a funcion principal
meteoritos()                
