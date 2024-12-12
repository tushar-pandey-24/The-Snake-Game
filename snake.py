from turtle import Turtle

POSITION = [(0,0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.snake_head = self.snake_list[0]

    def create_snake(self):
        for snakes in POSITION:
            self.add_tail(snakes)

    def move(self):
        for snake in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[snake - 1].xcor()
            new_y = self.snake_list[snake - 1].ycor()
            self.snake_list[snake].goto(x=new_x, y=new_y)
        self.snake_head.forward(20)

    def add_tail(self, snake):
        leo = Turtle("square")
        leo.color("white")
        leo.penup()
        leo.goto(snake)
        self.snake_list.append(leo)

    def extend_tail(self):
        self.add_tail(self.snake_list[-1].position())

    def reset(self):
        for segments in self.snake_list:
            segments.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.snake_head = self.snake_list[0]

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)



