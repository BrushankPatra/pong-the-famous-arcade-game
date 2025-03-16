from turtle import Turtle

# Ball class inherited from Turtle class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.shape("circle")
        self.penup()

    # Function to move the ball
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)