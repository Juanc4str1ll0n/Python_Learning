import pygame
import sys

# Inicializar pygame
pygame.init()

# Constantes
ANCHO, ALTO = 600, 600
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
FPS = 60

# Configurar pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Pac-Man")

# Reloj
clock = pygame.time.Clock()

# Jugador (Pac-Man)
pacman = pygame.Rect(50, 50, 30, 30)
velocidad = 5

# Paredes
paredes = [
    pygame.Rect(100, 100, 400, 20),
    pygame.Rect(100, 100, 20, 400),
    pygame.Rect(100, 480, 400, 20),
    pygame.Rect(480, 100, 20, 400)
]

# Comida
comida = pygame.Rect(300, 300, 10, 10)

def mover_pacman(teclas, pacman):
    if teclas[pygame.K_LEFT]:
        pacman.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        pacman.x += velocidad
    if teclas[pygame.K_UP]:
        pacman.y -= velocidad
    if teclas[pygame.K_DOWN]:
        pacman.y += velocidad

    # Colisión con paredes
    for pared in paredes:
        if pacman.colliderect(pared):
            if teclas[pygame.K_LEFT]:
                pacman.x += velocidad
            if teclas[pygame.K_RIGHT]:
                pacman.x -= velocidad
            if teclas[pygame.K_UP]:
                pacman.y += velocidad
            if teclas[pygame.K_DOWN]:
                pacman.y -= velocidad

# Bucle principal
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    teclas = pygame.key.get_pressed()
    mover_pacman(teclas, pacman)

    # Comer la comida
    if pacman.colliderect(comida):
        comida.x, comida.y = -100, -100  # la escondemos

    # Dibujar
    pantalla.fill(NEGRO)
    pygame.draw.rect(pantalla, AMARILLO, pacman)
    for pared in paredes:
        pygame.draw.rect(pantalla, AZUL, pared)
    pygame.draw.rect(pantalla, BLANCO, comida)

    pygame.display.flip()
