from turtle import Turtle,Screen
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.snakes = []
        self.create_snake() # "Automatically" create snake when object declared
        self.head = self.snakes[0]
    
    def create_snake(self):
        xcoor = 0
        for item in range(3):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(x=xcoor,y=0)
            xcoor-=20
            self.snakes.append(new_snake)

    def add_snake(self):
        last_segment = len(self.snakes)-1
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.snakes[last_segment].position())
        self.snakes.append(new_snake)

    def reset(self):
        for snake in self.snakes:
            snake.hideturtle()
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]

            

    def move(self):
        for snake in range(len(self.snakes)-1, 0,-1):
            #x and y value of the front segment.
            #So, the segment move to the last position of the segment in front of it.
            new_xcor = self.snakes[snake -1].xcor() 
            new_ycor = self.snakes[snake -1].ycor()
            self.snakes[snake].goto(new_xcor,new_ycor)
        self.snakes[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].seth(UP) 

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].seth(DOWN) 
    
    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].seth(LEFT) 

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].seth(RIGHT) 
    
        

