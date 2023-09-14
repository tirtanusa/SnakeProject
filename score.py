from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(y = 250,x= 0)
        self.pendown()
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align= "center",font=('Arial', 20, 'normal'))

    def add(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over.\nScore : {self.score}", align= "center",font=('Arial', 20, 'normal'))
        
        