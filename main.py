import pygame
import random

# Inicializar pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Definir tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Crear la ventana
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Atrapando Estrellas")

# Definir velocidad de las estrellas
star_speed = 0.1

# Definir posición inicial de la estrella
star_x = random.randint(0, SCREEN_WIDTH - 20)
star_y = 0

# Definir posición inicial del personaje
player_x = SCREEN_WIDTH / 2
player_y = SCREEN_HEIGHT - 100

# Definir tamaño del personaje
player_size = 50

# Definir fuente para el texto
font = pygame.font.Font(None, 36)
font_max_score = pygame.font.Font(None, 100)

# Definir puntaje
score = 0
max_score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 30
            elif event.key == pygame.K_RIGHT:
                player_x += 30

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Mover la estrella hacia abajo
    star_y += star_speed

    # Dibujar la estrella
    pygame.draw.rect(screen, YELLOW, (star_x, star_y, 20, 20))

    # Dibujar al personaje
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Verificar si la estrella ha alcanzado el fondo de la pantalla
    if star_y > SCREEN_HEIGHT:
        star_x = random.randint(0, SCREEN_WIDTH - 20)
        star_y = 0
        if score > max_score:
            max_score = score
        score = 0
        star_speed = 0.1

    # Verificar si el jugador ha atrapado la estrella
    if star_y + 20 >= player_y and star_x >= player_x and star_x <= player_x + player_size:
        if score % 5 == 0:
            star_speed += 0.05
        star_x = random.randint(0, SCREEN_WIDTH - 20)
        star_y = 0
        score += 1

    # Dibujar el puntaje
    text = font.render("Puntaje: " + str(score) + "            Mejor: " + str(max_score), True, WHITE)
    screen.blit(text, (10, 10))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()