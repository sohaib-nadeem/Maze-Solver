import turtle
# import time

Grid_1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s             +                            +",
"+  ++++++++++  +++++++++++++  +++++++  ++++  +",
"+           +                 +        +     +",
"+  +++++++  +++++++++++++  +++++++++++++++++++",
"+  +     +  +           +  +                 +",
"+  +  +  +  +  +  ++++  +  +  +++++++++++++  +",
"+  +  +  +  +  +  +     +  +  +  +        +  +",
"+  +  ++++  +  ++++++++++  +  +  ++++  +  +  +",
"+  +     +  +              +           +  +  +",
"+  ++++  +  ++++++++++++++++  +++++++++++++  +",
"+     +  +                    +              +",
"++++  +  ++++++++++++++++++++++  ++++++++++  +",
"+  +  +                    +     +     +  +  +",
"+  +  ++++  +++++++++++++  +  ++++  +  +  +  +",
"+  +  +     +     +     +  +  +     +     +  +",
"+  +  +  +++++++  ++++  +  +  +  ++++++++++  +",
"+                       +  +  +              +",
"++++  +  +  ++++++++++  +  +  +  +++++++++++++",
"+++++++++++++++++++++++e++++++++++++++++++++++",
]

Grid_2 = [
"+++++++++++++++",
"+s+   +   +  e+",
"+ + + + + + +++",
"+ + + + + +   +",
"+ + + + + +++ +",
"+ + + + + +   +",
"+ + + + + + +++",
"+ + + + + +   +",
"+ + + + + +++ +",
"+   +   +     +",
"+++++++++++++++"
]

Grid_3 = [
"+++++++++++++++++++++",
"+s    +     +       +",
"+ +++ + +++ + +++++ +",
"+ +   +   +   + +   +",
"+ +++++++ +++ + + +++",
"+   +   +   +   + + +",
"+++ + +++ + +++++ + +",
"+     +   +   +     +",
"+ +++++ + +++++ +++++",
"+       +   +      e+",
"+++++++++++++++++++++"
]


Grid_4 = [
"+++++++++++++++++++++",
"+s+   +           + +",
"+ + + + +++++++++ + +",
"+   +   +       + + +",
"+++++++ + +++++ + + +",
"+       +     +     +",
"+ +++++ +++++ +++++++",
"+     + +   +       +",
"+++++ + + +++++ +++ +",
"+     +   +e    +   +",
"+++++++++++++++++++++"
]


start_x = 2
start_y = 1
end_x = 23
end_y = 19

width = 1380
height = 600

def turtle_vec(x, y):
    return ((-width/2) + (30 * x), (height/2) - (30 * y))

# makes a filled square taking its current position as the top left vertex
def make_square(width, height):
    t.begin_fill()
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.end_fill()

# draw the maze
def setupMaze(grid):
    t.ht()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]

            if char == "+":
                t.goto(turtle_vec(x, y))
                make_square(30,30)                
            elif char == "s":
                start_x = x
                start_y = y
                t.fillcolor("red")
                t.goto(turtle_vec(x, y))
                make_square(30,30)
                t.fillcolor("white")
            elif char == "e":
                end_x = x
                end_y = y
                t.fillcolor("green")
                t.goto(turtle_vec(x, y))
                make_square(30,30)
                t.fillcolor("white")

    t.goto(turtle_vec(start_x + 0.5, start_y + 0.5))
    t.setheading(270)
    t.st()

def is_wall_in_front(x, y):
    direction = t.heading()
    if(direction == 0):
        return (Grid_1[y][x + 1] == "+")
    elif(direction == 90):
        return (Grid_1[y - 1][x] == "+")
    elif(direction == 180):
        return (Grid_1[y][x - 1] == "+")
    elif(direction == 270):
        return (Grid_1[y + 1][x] == "+")

def is_wall_on_right(x, y):
    direction = t.heading()
    if(direction == 0):
        return (Grid_1[y + 1][x] == "+")
    elif(direction == 90):
        return (Grid_1[y][x + 1] == "+")
    elif(direction == 180):
        return (Grid_1[y - 1][x] == "+")
    elif(direction == 270):
        return (Grid_1[y][x - 1] == "+")

def next_x(x):
    direction = t.heading()
    if(direction == 0):
        return x + 1
    if(direction == 180):
        return x - 1
    if(direction == 90 or direction == 270):
        return x

def next_y(y):
    direction = t.heading()
    if(direction == 90):
        return y - 1
    if(direction == 270):
        return y + 1
    if(direction == 0 or direction == 180):
        return y

############# main program starts here  ######################

# set up screen
s = turtle.Screen()
s.title("Maze Solver")
s.bgcolor("black")
s.setup(1400, 620) ###############

# set up turtle
t = turtle.Turtle()
t.shape("turtle")
t.shapesize(1,1)
t.fillcolor("white")
t.penup()

# set up maze
t.speed(100)
t.fillcolor("white")
setupMaze(Grid_1)
t.speed(1)
t.fillcolor("blue")

# set initial position
current_x = start_x
current_y = start_y

# solve maze
while(current_x != end_x or current_y != end_y):
    if(is_wall_on_right(current_x, current_y)):
        if(is_wall_in_front(current_x, current_y)):
            t.left(90)
        else:
            t.forward(30)
            current_x = next_x(current_x)
            current_y = next_y(current_y)
    else:
        t.right(90)
        t.forward(30)
        current_x = next_x(current_x)
        current_y = next_y(current_y)

s.exitonclick()
# time.sleep(2)