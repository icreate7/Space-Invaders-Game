from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self,position=(0,-320)):
        super().__init__()   #changing paddle to self. because of using the Turtle class
        self.shape("classic")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.left(90)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())
