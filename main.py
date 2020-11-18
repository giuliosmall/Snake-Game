'''This is out main working file'''

# Start from creating the snake

from turtle import Screen, Turtle
import time 

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

starting_positions=[(0,0),(-20,0),(-40,0)]

segments = []

for position in starting_positions:
	new_segment = Turtle("square")
	new_segment.color("white")
	new_segment.penup()
	new_segment.goto(position)
	segments.append(new_segment)

#screen.update()
#2. move the snake automatically

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1) 
    
    for seg_num in range(len(segments)-1,0,-1):
    #start where we start the range, stop and step - we want to go from 2 1, step -1
        new_x= segments[seg_num -1].xcor()
        new_y=segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)#we want the third segment to go to the second position
#we have to move also the first segment away 
    segments[0].forward(20)
    segments[0].left(90)
    #the pieces will do only a circle 
    
    #we need to think about segments that move in a graph
      
                                  
                                      
                                      
                                      
                                      






screen.exitonclick() #run it it does not disappear straight away 
