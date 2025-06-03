from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")
screen.title("Crossing")

game_is_on = True

while game_is_on :
    
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()


screen.exitonclick()