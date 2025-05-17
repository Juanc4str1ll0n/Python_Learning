import pygame

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hola Mundo")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ventana.fill((0, 0, 0))
    pygame.display.flip()