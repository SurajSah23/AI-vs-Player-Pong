import pygame
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH = 600
HEIGHT = 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI vs Player Pong Game")

# Paddle and ball settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 60
BALL_RADIUS = 10

# Speeds
player_speed = 7
ai_speed = 7
ball_speed_x = 5
ball_speed_y = 5

# Font for score
font = pygame.font.SysFont("Arial", 32)

# Function to draw paddles, ball, and score
def draw(player_y, ai_y, ball_x, ball_y, player_score, ai_score):
    screen.fill(BLACK)

    # Draw paddles
    pygame.draw.rect(screen, WHITE, (10, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # Player paddle
    pygame.draw.rect(screen, WHITE, (WIDTH - 20, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))  # AI paddle

    # Draw ball
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

    # Draw scores
    player_score_text = font.render(str(player_score), True, WHITE)
    ai_score_text = font.render(str(ai_score), True, WHITE)
    screen.blit(player_score_text, (WIDTH // 4, 20))
    screen.blit(ai_score_text, (WIDTH * 3 // 4, 20))

    pygame.display.update()

# Function to handle AI movement
def ai_move(ball_y, ai_y):
    if ai_y + PADDLE_HEIGHT // 2 < ball_y:
        ai_y += ai_speed
    elif ai_y + PADDLE_HEIGHT // 2 > ball_y:
        ai_y -= ai_speed

    # Keep AI paddle within the screen bounds
    if ai_y < 0:
        ai_y = 0
    elif ai_y > HEIGHT - PADDLE_HEIGHT:
        ai_y = HEIGHT - PADDLE_HEIGHT
    return ai_y

# Main game loop
def game():
    player_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ai_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_dx = random.choice([ball_speed_x, -ball_speed_x])
    ball_dy = random.choice([ball_speed_y, -ball_speed_y])

    player_score = 0
    ai_score = 0

    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get the keys pressed by the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - PADDLE_HEIGHT:
            player_y += player_speed

        # Move the ball
        ball_x += ball_dx
        ball_y += ball_dy

        # Check for ball collision with top and bottom walls
        if ball_y <= BALL_RADIUS or ball_y >= HEIGHT - BALL_RADIUS:
            ball_dy = -ball_dy

        # Check for ball collision with paddles
        if ball_x <= 10 + PADDLE_WIDTH and player_y < ball_y < player_y + PADDLE_HEIGHT:
            ball_dx = -ball_dx
        elif ball_x >= WIDTH - 20 - PADDLE_WIDTH and ai_y < ball_y < ai_y + PADDLE_HEIGHT:
            ball_dx = -ball_dx

        # Update AI movement
        ai_y = ai_move(ball_y, ai_y)

        # Check for scoring
        if ball_x <= 0:
            ai_score += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dx = random.choice([ball_speed_x, -ball_speed_x])
            ball_dy = random.choice([ball_speed_y, -ball_speed_y])

        if ball_x >= WIDTH:
            player_score += 1
            ball_x = WIDTH // 2
            ball_y = HEIGHT // 2
            ball_dx = random.choice([ball_speed_x, -ball_speed_x])
            ball_dy = random.choice([ball_speed_y, -ball_speed_y])

        # Draw everything
        draw(player_y, ai_y, ball_x, ball_y, player_score, ai_score)

    pygame.quit()

# Start the game
game()
