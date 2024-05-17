from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = [] #create an empty list of cars

    def create_car(self):
        random_chance = random.randint(1, 6) #used to randomize creation of car
        if (random_chance == 1):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS)) #choses a color from the color list
            random_y = random.randint(-250,250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) #appends the car created to the car list
            self.speed = STARTING_MOVE_DISTANCE #sets speed of car

    #function to get turtles moving right to left
    def moving(self):
        #go thru each car and move them
        for car in self.all_cars:
            car.backward(self.speed)

#if player levels up increase their speed by 10
    def level_up(self):
        for car in self.all_cars:
            self.speed += MOVE_INCREMENT
            car.backward(self.speed)


