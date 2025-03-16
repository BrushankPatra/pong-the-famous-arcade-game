from turtle import Turtle

# Ball class inherited from Turtle class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # Function to move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1