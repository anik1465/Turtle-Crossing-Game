'''class used to Display level and game over!!!'''
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-300, 250)
        self.level = 0
        self.write(f"Level: {self.level}", True, align="left", font=FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-300, 250)
        self.write(f"Level: {self.level}", True, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()
    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over!!!", True, align="left", font=FONT)

