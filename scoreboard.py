from turtle import Turtle

# class Scoreboard inherited from Turtle class to track and display scores
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # Method to update the scoreboard
    def update_scoreboard(self):
        # Place left score on the correct left position
        self.goto(-100, 200)
        # Clear the scoreboard first to prevent overwriting
        self.clear()
        # Display scores on the screen
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        # Place right score on the correct right position
        self.goto(100, 200)
        # Display scores on the screen
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Method to increase left score
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Method to increase left score
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()