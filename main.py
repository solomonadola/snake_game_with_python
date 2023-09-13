from turtle import Screen
import  time

from snake import Snake

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my snake")
screen.tracer(0)


game_is_on = True
snake = Snake()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()







screen.exitonclick()