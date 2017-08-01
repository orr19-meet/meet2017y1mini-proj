import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
#

turtle.penup()
SQUARE_SIZE = 20
START_LENGTH = 6
#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")
#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()


for i in range(START_LENGTH) :
    
    x_pos=snake.pos()[0]  #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]
#Add SQUARE_SIZE to x_pos. Where does x_pos point to now?
# You're RIGHT!
    x_pos=x_pos+SQUARE_SIZE
    my_pos=(x_pos,y_pos)  #Store position variables in a tuple
    snake.goto(x_pos,y_pos)  #Move snake to new
#(x,y)
#Append the new position tuple to pos_list
    pos_list.append(my_pos)
#Save the stamp ID! You'll need to erase it later. Then

#append
# it to stamp_list.
    stampID = snake.stamp()
    stamp_list.append(snake.stamp())


UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100 
#milliseconds
SPACEBAR = "space" 

UP = 0
LEFT=1
DOWN=2
RIGHT=3

direction = UP

def up():
    global direction  
    direction=UP
    move_snake()
    print("You pressed the up key!")



def down():
    global direction
    direction=2
    move_snake()
    print("You pressed the down key!")


def left():
    global direction
    direction=1 
    move_snake()
    print("You pressed the left key!")


def right():
    global direction 
    direction=3 
    move_snake()
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")

    elif direction==UP:
        snake.goto(x_pos, y_pos+SQUARE_SIZE)
        print("You moved up!")

    else:
        snake.goto(x_pos, y_pos-SQUARE_SIZE)
        print("You moved down!")
              
    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    #pop zeroth element in pos_list to get rid of last the last
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


        

                  

