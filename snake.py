from turtle import Turtle
from new_screen import New_Screen
import time
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
new_screen = New_Screen()
screen = new_screen.create_screen()
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segment_snake = []
        self.create_snake()
        self.head = self.segment_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_square(position)

    def last_segment(self):
        self.create_square(self.segment_snake[len(self.segment_snake) - 1].position())

    def create_square(self, coordinate):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(coordinate)
        self.segment_snake.append(square)

    def reset_snake(self):
        for segments in self.segment_snake:
            segments.goto(1000, 1000)

        self.segment_snake.clear()
        self.create_snake()
        self.head = self.segment_snake[0]

    def control_snake(self):
        def move_north():
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def move_south():
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def move_east():
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        def move_west():
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT)

        screen.listen()
        screen.onkey(fun=move_north, key="w")
        screen.onkey(fun=move_west, key="a")
        screen.onkey(fun=move_south, key="s")
        screen.onkey(fun=move_east, key="d")

    def move(self):
        screen.update()
        time.sleep(0.1)
        for segment_num in range(len(self.segment_snake) - 1, 0, -1):
            new_x = self.segment_snake[segment_num - 1].xcor()
            new_y = self.segment_snake[segment_num - 1].ycor()
            self.segment_snake[segment_num].goto(new_x, new_y)
            self.control_snake()

        self.head.forward(MOVE_DISTANCE)