
import pygame

def crear_ventana(ANCHO, ALTO):

	ventana = pygame.display.set_mode((ANCHO, ALTO))
	pygame.display.set_caption("SnakeGame")

	return ventana