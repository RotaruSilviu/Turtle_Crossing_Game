import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_forward, key="w")
screen.onkeypress(fun=player.move_backward, key="s")

counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    for each_car in car.cars:
        if player.distance(each_car) < 20:
            score.game_over()
            game_is_on = False
    if player.next_level():
        car.level_up()
        score.level_up()
    car.move_cars()


screen.exitonclick()
