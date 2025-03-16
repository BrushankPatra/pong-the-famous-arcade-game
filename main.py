from turtle import Turtle, Screen
from paddle import Paddle

# Create paddles
left_paddle = Paddle((-360, 0))
right_paddle = Paddle((360, 0))

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Famous Arcade Game")

screen.listen()

# Control the left paddle
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Control the right paddle
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# Exit program on click in the screen
screen.exitonclick()
