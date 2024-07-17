
import pygame

def crear_personajes(ANCHO, ALTO):

	# Crear imagen de la manzana

	manzana_img = pygame.image.load("Apple.png")
	manzana_rect = manzana_img.get_rect()
	manzana_rect.center = (ANCHO // 2, ALTO // 2) # Posicion

	# Crear serpiente y su velocidad

	serpiente_rect = pygame.Rect(100, 100, 30, 20)
	velocidad_x = 5
	velocidad_y = 0

	return manzana_img, manzana_rect, serpiente_rect, velocidad_x, velocidad_y