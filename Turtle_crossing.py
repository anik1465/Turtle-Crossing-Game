from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

#creates the turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

#function to get the turtle to move up if up key is pressed.
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

#checks if turtle reached finish line
    def reached_finish_line(self):
        if(self.ycor() > FINISH_LINE_Y):
            return True
        else:
            return False

#used to reset position back to beginning
    def restart(self):
        return self.goto(STARTING_POSITION)

