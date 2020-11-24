'''This is our main working file'''

from turtle import Screen, Turtle
import time 

#After you have created the snake.py class you need to import it in main.py
from snake import Snake 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake() #calling class
# the class creates the snake body, moves it and allows for control with keys

screen.listen()       
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')
      
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)                                  
                                      
                                      
                                      
                                
screen.exitonclick() #run it it does not disappear straight away 
