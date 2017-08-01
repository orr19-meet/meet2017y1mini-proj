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
    stamp_list.append(stampID)


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

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
def up():
    global direction  
    direction=UP
    
    print("You pressed the up key!")



def down():
    global direction
    direction=2
    
    print("You pressed the down key!")


def left():
    global direction
    direction=1
    
    print("You pressed the left key!")


def right():
    global direction 
    direction=3 
    
    print("You pressed the right key!")

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)

turtle.listen()

TIME_STEP=100

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
    global food_stamps, food_pos
#If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("You have eaten the food!")
    
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()

    elif new_x_pos <= LEFT_EDGE:
        print("You hit the left edge! Game over!")
        quit()

    if new_y_pos >= UP_EDGE:
        print("You hit the up edge! Game over!")
        quit()

    
    elif new_y_pos <= DOWN_EDGE:
        print("You hit the down edge! Game over!")
        
        quit()


    turtle.ontimer(move_snake,TIME_STEP)
move_snake()


turtle.register_shape("trash.gif") 
food = turtle.clone()
food.hideturtle()
food.shape("trash.gif")
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []


for this_food_pos in food_pos :
    food.goto(this_food_pos)
    food.stamp()
    food_stamps.append(this_food_pos)




        

                  




        

                  




    

        

                  





    

        

                  

