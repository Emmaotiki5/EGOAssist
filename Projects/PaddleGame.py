import pygame
from pygame.locals import *
import random
def paddlegame():
    # Initialize Pygame
    pygame.init()

    # Set up the game window
    WIDTH = 800
    HEIGHT = 400
    FPS = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    # Set up colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Set up the paddles
    PADDLE_WIDTH = 10
    PADDLE_HEIGHT = 60
    PADDLE_SPEED = 5

    player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    computer_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # Set up the ball
    BALL_RADIUS = 8
    BALL_SPEED_X = 4
    BALL_SPEED_Y = 4

    ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
    ball_speed_x = random.choice([-1, 1]) * BALL_SPEED_X
    ball_speed_y = random.choice([-1, 1]) * BALL_SPEED_Y

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[K_UP] and player_paddle.top > 0:
            player_paddle.y -= PADDLE_SPEED
        if keys[K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.y += PADDLE_SPEED

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.left <= 0:
            ball_speed_x *= -1
        if ball.right >= WIDTH:
            ball_speed_x *= -1
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Paddle collision
        if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
            ball_speed_x *= -1

        # Computer paddle movement
        if computer_paddle.top < ball.y:
            computer_paddle.y += PADDLE_SPEED
        if computer_paddle.bottom > ball.y:
            computer_paddle.y -= PADDLE_SPEED

        # Clear the screen
        screen.fill(BLACK)

        # Draw the paddles and ball
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, computer_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # Draw the middle line
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

    # Quit the game
    pygame.quit()
