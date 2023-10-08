import pygame
import sys

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAVITY = 0.5
MOVE_SPEED = 5
JUMP_HEIGHT = -10

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Advanced Platformer")

# Player properties
player_width = 50
player_height = 50
player_x = SCREEN_WIDTH // 2 - player_width // 2
player_y = SCREEN_HEIGHT - player_height - 20
player_x_speed = 0
player_y_speed = 0
on_ground = False

# Platforms
platforms = [
    pygame.Rect(100, 500, 200, 10),
    pygame.Rect(400, 400, 200, 10),
    pygame.Rect(200, 300, 200, 10),
    pygame.Rect(600, 200, 200, 10),
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x_speed = -MOVE_SPEED
    elif keys[pygame.K_RIGHT]:
        player_x_speed = MOVE_SPEED
    else:
        player_x_speed = 0

    if on_ground:
        if keys[pygame.K_SPACE]:
            player_y_speed = JUMP_HEIGHT
    else:
        player_y_speed += GRAVITY

    player_x += player_x_speed
    player_y += player_y_speed

    on_ground = False
    for platform in platforms:
        if player.colliderect(platform):
            if player_y_speed > 0:
                player_y = platform.top - player_height
                on_ground = True
                player_y_speed = 0
            elif player_y_speed < 0:
                player_y = platform.bottom
                player_y_speed = 0

    screen.fill((0, 0, 0))
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, RED, player)

    for platform in platforms:
        pygame.draw.rect(screen, BLUE, platform)

    pygame.display.update()
