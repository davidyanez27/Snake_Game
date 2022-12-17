from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hig_score = self.read_data("data.txt")
        self.penup()
        self.hideturtle()
        self.setposition(0, 270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Scoreboard {self.score}    High Score: {self.hig_score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()


    def read_data(self, name):
        with open(file=name, mode="r") as file:
            return int(file.read())

    def write_Data(self, name):
        with open(file=name, mode="w") as file:
            file.write(str(self.hig_score))

    def reset_score(self):
        if self.score > self.hig_score:
            self.hig_score = self.score
            self.write_Data("data.txt")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write(arg="Game Over", align=ALIGNMENT, font=FONT)

