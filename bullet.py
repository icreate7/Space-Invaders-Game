from turtle import Turtle

class Bullet:
    def __init__(self):
        self.bullets = []
        self.bullet_speed = 3

    def create_bullet(self, paddle):
        new_bullet = Turtle()
        new_bullet.shape("square")
        new_bullet.shapesize(stretch_len=0.2, stretch_wid=0.1)
        new_bullet.color("white")
        new_bullet.penup()
        new_bullet.goto(paddle.xcor(), paddle.ycor() + 10)
        new_bullet.setheading(90)
        self.bullets.append(new_bullet)

    def move_bullet(self):
        for bullet in self.bullets[:]:  # [:] to safely remove inside loop
            bullet.forward(self.bullet_speed)
            if bullet.ycor() > 340:
                bullet.hideturtle()
                self.bullets.remove(bullet)
