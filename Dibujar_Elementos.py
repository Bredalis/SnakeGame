
import pygame

def dibujar_personajes(ventana, manzana_img, manzana_rect, serpiente_rect, color_serpiente):
    ventana.fill((0, 0, 0))
    ventana.blit(manzana_img, manzana_rect)
    pygame.draw.rect(ventana, color_serpiente, serpiente_rect)

def mostrar_puntos(ventana, puntos, record, guardar_record, color_texto):
    fuente = pygame.font.Font(None, 20)
    texto_puntos = fuente.render(f"Puntos:  {puntos}", True, color_texto)
    texto_record = fuente.render(f"Record:  {record}", True, color_texto)
    texto_record_maximo = fuente.render(f"Maximo Record:  {guardar_record.mostrar_record()}", True, color_texto)

    ventana.blit(texto_puntos, (30, 30))
    ventana.blit(texto_record, (130, 30))
    ventana.blit(texto_record_maximo, (230, 30))