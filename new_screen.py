from turtle import Screen



class New_Screen():
    def create_screen(self):
        screen = Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("black")
        screen.title("My Snake Game")
        screen.tracer(0)
        return screen

