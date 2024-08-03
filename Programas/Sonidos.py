
import pygame

def sonido(nombre_sonido):
	pygame.mixer.music.load(f"../Audio/{nombre_sonido}.mp3")
	pygame.mixer.music.play()