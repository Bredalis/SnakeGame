
# Librerias

import pygame
import random
from Record import *

# Instancia para acceder 
# al record del juego 

guardar_record = Record()

# Inicir pygame

pygame.init()
pygame.mixer.init()

# Tamaño de la ventana

ANCHO, ALTO = 550, 500

# Colores

VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("SnakeGame")

# Crear imagen de la manzana

manzana_img = pygame.image.load("Apple.png")
manzana_rect = manzana_img.get_rect()
manzana_rect.center = (ANCHO // 2, ALTO // 2) # Posicion

# Crear serpiente

serpiente_rect = pygame.Rect(100, 100, 30, 20)
velocidad_x = 5
velocidad_y = 0

puntos = 0
record = 0

run = True
reloj = pygame.time.Clock()

# Logica del juego

while run:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        elif evento.type == pygame.KEYDOWN:
        	if evento.key == pygame.K_LEFT:
        		pygame.mixer.music.load("Spinning.mp3")
        		pygame.mixer.music.play()
        		if velocidad_x == 0:  
        			velocidad_x = -5
        			velocidad_y = 0

        	elif evento.key == pygame.K_RIGHT:
        		pygame.mixer.music.load("Spinning.mp3")
        		pygame.mixer.music.play()
        		if velocidad_x == 0:
        			velocidad_x = 5
        			velocidad_y = 0

        	elif evento.key == pygame.K_UP:
        		pygame.mixer.music.load("Spinning.mp3")
        		pygame.mixer.music.play()
        		if velocidad_y == 0:  
        			velocidad_x = 0
        			velocidad_y = -5

        	elif evento.key == pygame.K_DOWN:
        		pygame.mixer.music.load("Spinning.mp3")
        		pygame.mixer.music.play()
        		if velocidad_y == 0:
        			velocidad_x = 0
        			velocidad_y = 5

    # Velocidad de la serpiente

    reloj.tick(40)

    # Mover la serpiente en cada iteración

    serpiente_rect.x += velocidad_x
    serpiente_rect.y += velocidad_y

    # Dibujar los personajes

    ventana.fill((0, 0, 0))
    ventana.blit(manzana_img, manzana_rect)
    pygame.draw.rect(ventana, VERDE, serpiente_rect)

    # Mostrar puntos

    fuente = pygame.font.Font(None, 20)
    texto_puntos = fuente.render(f"Puntos:  {puntos}", True, BLANCO)
    texto_record = fuente.render(f"Record:  {record}", True, BLANCO)
    texto_record_maximo = fuente.render(f"Maximo Record:  {guardar_record.mostrar_record()}", True, BLANCO)

    ventana.blit(texto_puntos, (30, 30))
    ventana.blit(texto_record, (130, 30))
    ventana.blit(texto_record_maximo, (230, 30))

    if serpiente_rect.colliderect(manzana_rect):
        pygame.mixer.music.load("Eating.mp3")
        pygame.mixer.music.play()

        nueva_posicion_x = random.randint(0, ANCHO - manzana_rect.width)
        nueva_posicion_y = random.randint(0, ALTO - manzana_rect.height)
        manzana_rect.topleft = (nueva_posicion_x, nueva_posicion_y)

        puntos += 1
        record = max(record, puntos)

        guardar_record.guardar_record(record)

    # Ajustar las dimensiones de la serpiente para que se doble

    if velocidad_x != 0:
    	serpiente_rect.width = 30 + puntos * 10
    	serpiente_rect.height = 20 

    elif velocidad_y != 0:
        serpiente_rect.width = 20
        serpiente_rect.height = 30 + puntos * 10

    # Fin del juego

    if (serpiente_rect.left < 0 or serpiente_rect.right > ANCHO or
            serpiente_rect.top < 0 or serpiente_rect.bottom > ALTO):

        pygame.mixer.music.load("GameOver.mp3")
        pygame.mixer.music.play()
        run = False

        if run != True:
            puntos = 0
            serpiente_rect = pygame.Rect(100, 100, 30, 20)
            run = True

    pygame.display.flip()

# Guardar cambios y cerrar bddd

guardar_record.guardar_cambios()
guardar_record.cerrar_bbdd()

pygame.quit()