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

p1 = Player()
screen.listen()
screen.onkey(key='Up', fun=p1.player_move)

carlist = []

for _ in range(20):
    carlist.append(CarManager())

# create initial cars
for car in carlist:
    # Initial positions for cars:
    initx = randint(-200, 270)
    inity = randint(-200, 270)
    car.goto(x=initx, y=inity)

scoreboard = Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if len(carlist) < 20:
        carlist.append(CarManager())

    for car in carlist:
        car.move_car()
        if car.xcor() < -310:
            carlist.remove(car)
            # car.reset()
            car.hideturtle()
        if car.distance(p1) < 15:
            p1.player_reset()

    if p1.ycor() > 270:
        scoreboard.increase_score()
        p1.player_reset()
        for car in carlist:
            car.increase_speed()
