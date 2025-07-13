from turtle import Turtle

FONT = ("courier", 20, "bold")

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def game_over_text(self):
        self.write("Game Over! 😢", align="center", font=FONT)

    def game_won_text(self):
        self.write("You've Won! 😀", align="center", font=FONT)
