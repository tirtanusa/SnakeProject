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
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} Highscore : {self.high_score}", align= "center",font=('Arial', 20, 'normal'))

    def add(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0,0)
    #     self.write(f"Game Over.\nScore : {self.score}", align= "center",font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()
        self.save_high_score()

    def save_high_score(self):
        with open("highscore.txt",mode = "w") as file:
            file.write(f"{self.high_score}")
        
        