from microbit import display, button_a, button_b, sleep, Image
import random

# Pong game on Micro:bit with random bounces
# Player 1 paddle on left (x=0), Player 2 paddle on right (x=4)
# Holding button moves paddle up, releasing moves down

# Paddle size
PADDLE_HEIGHT = 2

# Initial paddle positions on the LED matrix
paddle1_y = 1
paddle2_y = 1

ball_x = 2
ball_y = 2
vel_x = 1
vel_y = 1

# Scores Unused yet but you can add something that uses this
score1 = 0
score2 = 0

# Draw paddles and ball
def draw():
    display.clear()
    # Draw paddle1
    for i in range(PADDLE_HEIGHT):
        y = paddle1_y + i
        if 0 <= y <= 4:
            display.set_pixel(0, y, 9)
    # Draw paddle2
    for i in range(PADDLE_HEIGHT):
        y = paddle2_y + i
        if 0 <= y <= 4:
            display.set_pixel(4, y, 9)
    # Draw ball
    display.set_pixel(ball_x, ball_y, 5)

def paddle_bounce():
    global vel_x, vel_y
    vel_x = -vel_x
    vel_y = random.choice([-1, 0, 1])

while True:
    # Move paddles
    if button_a.is_pressed():
        paddle1_y = max(0, paddle1_y - 1)
    else:
        paddle1_y = min(5 - PADDLE_HEIGHT, paddle1_y + 1)

    if button_b.is_pressed():
        paddle2_y = max(0, paddle2_y - 1)
    else:
        paddle2_y = min(5 - PADDLE_HEIGHT, paddle2_y + 1)

    next_x = ball_x + vel_x
    next_y = ball_y + vel_y

    if next_y < 0 or next_y > 4:
        vel_y = -vel_y
        next_y = ball_y + vel_y

    if next_x < 0:
        if paddle1_y <= next_y <= paddle1_y + PADDLE_HEIGHT - 1:
            paddle_bounce()
            next_x = ball_x + vel_x
        else:
            score2 += 1
            ball_x, ball_y = 2, 2
            vel_x = 1
            vel_y = random.choice([-1, 1])
            display.show(Image.NO)
            sleep(200)
            continue

    if next_x > 4:
        if paddle2_y <= next_y <= paddle2_y + PADDLE_HEIGHT - 1:
            paddle_bounce()
            next_x = ball_x + vel_x
        else:
            score1 += 1
            ball_x, ball_y = 2, 2
            vel_x = -1
            vel_y = random.choice([-1, 1])
            display.show(Image.NO)
            sleep(200)
            continue

    ball_x, ball_y = next_x, next_y

    draw()

    sleep(500)
