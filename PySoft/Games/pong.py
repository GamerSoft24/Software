import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED = 7
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Initialize paddles and ball
paddle_width = 15
paddle_height = 100
ball_size = 20

left_paddle = pygame.Rect(50, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(SCREEN_WIDTH - 50 - paddle_width, SCREEN_HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_size // 2, SCREEN_HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))

left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    if ball.left <= 0:
        right_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_size // 2, SCREEN_HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    elif ball.right >= SCREEN_WIDTH:
        left_score += 1
        ball = pygame.Rect(SCREEN_WIDTH // 2 - ball_size // 2, SCREEN_HEIGHT // 2 - ball_size // 2, ball_size, ball_size)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (SCREEN_WIDTH // 4, 20))
    screen.blit(right_text, (3 * SCREEN_WIDTH // 4 - 20, 20))

    pygame.display.update()
