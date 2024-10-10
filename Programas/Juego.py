
# Librerías

import pygame
import random
from Ventana import crear_ventana
from Personajes import crear_personajes
from Sonidos import sonido
from Acciones_Teclado import manejar_teclado
from Dibujar_Elementos import dibujar_personajes, mostrar_puntos
from Record import RecordLocal, RecordRemoto

# Instancia para acceder al record del juego 

guardar_record = RecordLocal()
guardar_record_remoto = RecordRemoto()

# Inicir pygame

pygame.init()
pygame.mixer.init()

ANCHO = 550
ALTO = 500

ventana = crear_ventana(ANCHO, ALTO)

# Crear personajes
manzana_img, manzana_rect, serpiente_rect, velocidad_x, velocidad_y = crear_personajes(ANCHO, ALTO)

puntos = 0
record = 0

run = True
reloj = pygame.time.Clock()

# Logica del juego

while run:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

        # Manejar acciones del teclado
        velocidad_x, velocidad_y = manejar_teclado(evento, velocidad_x, velocidad_y)
        sonido("Spinning")

    # Velocidad de la serpiente
    reloj.tick(40)

    # Mover la serpiente en cada iteración

    serpiente_rect.x += velocidad_x
    serpiente_rect.y += velocidad_y
    
    # Dibujar elementos
    dibujar_personajes(ventana, manzana_img, manzana_rect, serpiente_rect, (0, 255, 0))
    mostrar_puntos(ventana, puntos, record, guardar_record, (255, 255, 255))

    if serpiente_rect.colliderect(manzana_rect):
        sonido("Eating")

        nueva_posicion_x = random.randint(0, ANCHO - manzana_rect.width)
        nueva_posicion_y = random.randint(0, ALTO - manzana_rect.height)
        manzana_rect.topleft = (nueva_posicion_x, nueva_posicion_y)

        puntos += 1
        record = max(record, puntos)

        record_guardado = guardar_record.guardar_record(record)
        guardar_record_remoto.ingresar_datos(record_guardado)

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

        sonido("GameOver")
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