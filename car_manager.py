from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# COLORS = ["red", "orange", "yellow", "green", "blue"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.resizemode('user')
        self.color(choice(COLORS))
        self.goto(320, randint(-200, 270))
        self.setheading(180)
        self.shape('square')
        self.shapesize(1, 2)

    def move_car(self):
        self.goto(x=self.xcor() - 10, y=self.ycor())


