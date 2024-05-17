import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car = CarManager()
score = Scoreboard()
tim = Player()
#creates screen size of 600 x 600
screen.setup(width=600, height=600)
screen.bgcolor("black") #sets background color to black
screen.tracer(0)
screen.listen() #listens to events
screen.onkey(fun=tim.go_up, key="Up")

#while loop to continue Turtle crossing
game_is_on = True
while game_is_on:
    time.sleep(0.1) #sleep method used to update score, generate cars
    car.create_car()
    car.moving() #moves the cars from right to left
    #detect collision with car
    for cars in car.all_cars:#go thru each car
        if(cars.distance(tim) < 30):#if distance less than 30 then collided
            game_is_on = False #ends the game
            score.end_game()

    #detect the play crossed raod
    if(tim.reached_finish_line()):#if finished line is reached
        tim.restart()
        car.level_up()
        score.level_up()

    screen.update()
screen.exitonclick()
