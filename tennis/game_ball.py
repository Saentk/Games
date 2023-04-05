import pygame

pygame.init()

# Set up the screen
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the paddles
paddle_width = 15
paddle_height = 60
paddle_speed = 0.2

left_paddle_x = 25
left_paddle_y = (height / 2) - (paddle_height / 2)

right_paddle_x = width - 40
right_paddle_y = (height / 2) - (paddle_height / 2)

# Set up the ball
ball_x = width / 2
ball_y = height / 2
ball_speed_x = 0.1
ball_speed_y = 0.1
ball_radius = 10

# Set up the score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    elif keys[pygame.K_s] and left_paddle_y < height - paddle_height:
        left_paddle_y += paddle_speed

    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    elif keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check for collisions with walls
    if ball_y > height - ball_radius or ball_y < ball_radius:
        ball_speed_y *= -1

    # Check for collisions with paddles
    if ball_x < left_paddle_x + paddle_width and \
       ball_y > left_paddle_y and \
       ball_y < left_paddle_y + paddle_height:
        ball_speed_x *= -1

    if ball_x > right_paddle_x and \
       ball_y > right_paddle_y and \
       ball_y < right_paddle_y + paddle_height:
        ball_speed_x *= -1

    # Check for scoring
    if ball_x < 0:
        right_score += 1
        ball_x = width / 2
        ball_y = height / 2
        ball_speed_x *= -1

    if ball_x > width:
        left_score += 1
        ball_x = width / 2
        ball_y = height / 2
        ball_speed_x *= -1

    # Draw the screen
    screen.fill(black)

    # Draw the paddles
    left_paddle = pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, left_paddle)

    right_paddle = pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height)
    pygame.draw.rect(screen, white, right_paddle)

    # Draw the ball
    ball = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    # Draw the score
    left_score_text = font.render(str(left_score), True, white)
    right_score_text = font.render(str(right_score), True, white)
    screen.blit(left_score_text, (width / 4, 20))
    screen.blit(right_score_text, (width * 3 / 4, 20))

    # Update the screen
    pygame.display.update()
