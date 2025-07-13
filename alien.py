import random
import time
from turtle import Turtle

# Grid config
rows = 5
cols = 6
alien_width = 50  # because stretch_len=5 (20px * 5)
alien_height = 20 # because stretch_wid=1 (20px)
x_spacing = 10
y_spacing = 10
start_x = -175
start_y = 240

class Alien(Turtle):
    def __init__(self, position=(0,490)):
        super().__init__()
        self.shape("triangle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.right(90)
        self.penup()
        self.goto(position)

class AlienGroup:
    def __init__(self):
        self.aliens_list = []
        self.alien_bullets = []
        self.bullet_cooldown = 3
        self.move_side_distance = 20
        self.move_down_distance = 40
        self.last_bullet_time = time.time()  # store the last time a bullet was fired
        self.create_aliens()
        self.move_aliens()

    def create_aliens(self):
        for row in range(rows):
            for col in range(cols):
                x = start_x + col * (alien_width + x_spacing)
                y = start_y - row * (alien_height + y_spacing)
                alien = Alien(position=(x, y))
                alien.showturtle()
                self.aliens_list.append(alien)

    def move_aliens(self):
        edge_hit = False
        for alien in self.aliens_list:
            alien.setx(alien.xcor() + self.move_side_distance)
            # Check if any alien hits edge of screen
            if alien.xcor() > 240 or alien.xcor() < -240:
                edge_hit = True
        if edge_hit:
            for alien in self.aliens_list:
                alien.sety(alien.ycor() - self.move_down_distance) # moves down
            self.move_side_distance *= -1

    def create_alien_bullet(self):
        current_time = time.time()
        if current_time - self.last_bullet_time >= self.bullet_cooldown:
            if not self.aliens_list:
                return
            shooter = random.choice(self.aliens_list)
            alien_bullet = Turtle()
            alien_bullet.shape("circle")
            alien_bullet.shapesize(stretch_len=0.5, stretch_wid=0.5)
            alien_bullet.color("red")
            alien_bullet.penup()
            alien_bullet.setheading(-90)
            alien_bullet.goto(shooter.xcor(), shooter.ycor() - 10)
            self.alien_bullets.append(alien_bullet)

            self.last_bullet_time = current_time  # updates the timer for the alien bullet

    def move_alien_bullets(self):
        for bullet in self.alien_bullets[:]:
            bullet.forward(1)
            if bullet.ycor() < -350:
                bullet.hideturtle()
                self.alien_bullets.remove(bullet)





