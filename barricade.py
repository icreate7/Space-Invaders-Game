from turtle import Turtle

class Barricade(Turtle):
    def __init__(self, position=(100,-100)):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1.5, stretch_len=4)
        self.color("yellow")
        self.penup()
        self.goto(position)
        self.health = 3
        self.active = True

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.active = False
            self.hideturtle()
        else:
            self.update_color()

    def update_color(self):
        if self.health == 2:
            self.color("orange")
        if self.health == 1:
            self.color("red")
