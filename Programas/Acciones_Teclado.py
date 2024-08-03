
import pygame

def manejar_teclado(evento, velocidad_x, velocidad_y):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT and velocidad_x == 0:
            return -5, 0
        elif evento.key == pygame.K_RIGHT and velocidad_x == 0:
            return 5, 0
        elif evento.key == pygame.K_UP and velocidad_y == 0:
            return 0, -5
        elif evento.key == pygame.K_DOWN and velocidad_y == 0:
            return 0, 5
    
    return velocidad_x, velocidad_y