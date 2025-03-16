from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Famous Arcade Game")
screen.tracer(0)

screen.listen()

# Create paddles
left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))

# Create ball
ball = Ball()

# Control the left paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Control the right paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Loop to control the game on or off
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect the collision of the ball and the wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        # Needs to bounce
        ball.bounce_y()

    # Detect the collision of the ball and the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect if the ball misses the paddles
    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_pos()

    # Detect when right paddle misses
    if ball.xcor() < -380:
        ball.reset_pos()

# Exit program on click in the screen
screen.exitonclick()
