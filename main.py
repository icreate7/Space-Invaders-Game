from turtle import Screen
from bullet import Bullet
from barricade import Barricade
from paddle import Paddle
from alien import Alien, AlienGroup
from text import Text
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.title("Space Invaders")
screen.tracer(0)

paddle = Paddle(position=(0,-320))

barricade_1 = Barricade(position=(-175,-220))
barricade_2 = Barricade(position=(0,-220))
barricade_3 = Barricade(position=(175,-220))

bullet = Bullet()
text = Text()
alien = Alien()
alien_group = AlienGroup()

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkey(lambda: bullet.create_bullet(paddle), "space")  # space bar fires bullet

# Setup for alien movement timer
last_move_time = time.time()
move_interval = 3

game_is_on = True
while game_is_on:
    barricades = [barricade_1, barricade_2, barricade_3]
    aliens_to_remove = []
    screen.update()
    time.sleep(0.01)
    bullet.move_bullet()
    alien_group.move_alien_bullets()
    alien_group.create_alien_bullet()

    # detect collision with the aliens
    for alien in alien_group.aliens_list:
        for player_bullet in bullet.bullets[:]:
            if player_bullet.distance(alien) < 20:
                alien.hideturtle()
                aliens_to_remove.append(alien)
                player_bullet.hideturtle()
                bullet.bullets.remove(player_bullet)

    for alien_bullet in alien_group.alien_bullets[:]:
        if alien_bullet.distance(paddle) < 10:
            text.game_over_text()
            game_is_on = False

        for barricade in barricades:
            if not barricade.active:
                continue  # Skip inactive ones

            if alien_bullet.distance(barricade) < 30:
                barricade.take_damage()
                alien_bullet.hideturtle()
                alien_group.alien_bullets.remove(alien_bullet)
                break  # no need to check other barricades

    # player bullets and barricade collision
    for player_bullet in bullet.bullets[:]:
        for barricade in barricades:
            if not barricade.active:
                continue  # Skip inactive ones

            if player_bullet.distance(barricade) < 30:
                barricade.take_damage()
                player_bullet.hideturtle()
                bullet.bullets.remove(player_bullet)

    # permanently remove the alien from the list
    for alien in aliens_to_remove:
        alien_group.aliens_list.remove(alien)

    # Move aliens down once per second
    current_time = time.time()
    if current_time - last_move_time > move_interval:
        alien_group.move_aliens()
        last_move_time = current_time

    for alien in alien_group.aliens_list:
        for barricade in barricades:
            if alien.distance(barricade) < 40:
                barricade.hideturtle()

        if alien.distance(paddle) < 20 or alien.ycor() < -300:
            text.game_over_text()
            game_is_on = False
            break

    # game winning scenario
    if len(alien_group.aliens_list) == 0:
        text.game_won_text()
        game_is_on = False


screen.update()
screen.exitonclick()