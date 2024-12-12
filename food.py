from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.refresh()

    def refresh(self):
        rand_x = random.randint(-265, 265)
        rand_y = random.randint(-265, 265)
        self.goto(rand_x, rand_y)