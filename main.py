import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True

sleep = 0.1

player = Player()
screen.listen()
screen.onkey(key='Up', fun=player.player_move)

carlist = []


def carsCreate():
    carlist.append(CarManager())


for _ in range(20):
    carsCreate()

# create initial cars
for car in carlist:
    # Initial positions for cars:
    print(car.color())
    initx = randint(-200, 270)
    inity = randint(-200, 270)
    car.goto(x=initx, y=inity)

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(sleep)
    screen.update()

    random_number = randint(0, 6)
    if random_number == 1:
        carlist.append(CarManager())

    for car in carlist:
        car.move_car()
        if car.xcor() < -310:
            carlist.remove(car)
            # car.reset()
            car.hideturtle()
        if car.distance(player) < 20:
            # player.player_reset()
            scoreboard.game_over()
            sleep = 0.1
            game_is_on = False

    if player.ycor() > 270:
        scoreboard.increase_score()
        player.player_reset()
        for car in carlist:
            sleep *= 0.9

screen.exitonclick()
