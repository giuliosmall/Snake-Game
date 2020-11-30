'''This is our main working file'''

from turtle import Screen  #Turtle we can delate Turtle since we use it inside all the classes
import time 
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake() #calling class
# the class creates the snake body, moves it and allows for control with keys
food = Food()
scoreboard = Scoreboard() #allow to maintain the score and create the scoreboard

screen.listen()       
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
      
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)      
    snake.move()  

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()                          
                                      
                                      
                                                                    
screen.exitonclick() #run it it does not disappear straight away 
