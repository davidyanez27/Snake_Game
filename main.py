from food import Food
from snake import Snake, screen
from scoreboard import Scoreboard

game_is_on = True
snake = Snake()
dot = Food()
score = Scoreboard()

while game_is_on:
    snake.move()

    #Detect collision with food.
    if snake.head.distance(dot) < 15:
        dot.refresh()
        score.increase()
        # last = len(snake.segment_snake)-1
        # last_position = snake.segment_snake[len(snake.segment_snake)-1].position()
        # snake.create_square(last_position)
        snake.last_segment()

    #Detec collision with wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.reset_score()
        snake.reset_snake()

    for segment_number in range(len(snake.segment_snake)-1, 0, -1):
        if snake.head.position() == snake.segment_snake[segment_number].position():
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()



