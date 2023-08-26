import turtle


#Screen setup
wn = turtle.Screen()
wn.setup(width = 800, height = 600)
wn.title('Drawing app')
wn.bgcolor('white')

# Tools bar
toolsbar = turtle.Turtle(visible=False)
toolsbar.color("gray")
toolsbar.speed(0)
toolsbar.penup()
toolsbar.setposition(-400, 200)
toolsbar.pendown()
toolsbar.begin_fill()
for i in range(2):
    toolsbar.forward(800)
    toolsbar.left(90)
    toolsbar.forward(100)
    toolsbar.left(90)
toolsbar.end_fill()

# Drawing pen
pen = turtle.Turtle('circle')
pen.color("black")
pen.shapesize(1)
pen.speed(-1)

class Color(turtle.Turtle):
    def __init__(self, clr: str, pos: list[int]) -> None:
        turtle.Turtle.__init__(self, 'square')
        turtle.Turtle.onclick(self, lambda x, y: pen.color(clr), 1)
        self.penup()
        self.speed(-1)
        self.color(clr)
        self.goto(pos[0], pos[1])
        self.shapesize(1)

# Color pallete
c1, c2 = Color('green', [-230 , 270]), Color('red', [-200 , 270])
c3, c4 = Color('blue', [-170 , 270]), Color('orange', [-140 , 270])
c5, c6 = Color('yellow', [-110 , 270]), Color('white', [-80 , 270])
c7, c8 = Color('darkgray', [-50 , 270]), Color('black', [-20 , 270])

# Functions for drawing
def dragging(x: float, y: float) -> None:
    global xcor , ycor
    pen.ondrag(None)
    pen.setheading(pen.towards(x , y))
    pen.goto(x , y)
    xcor, ycor = x, y
    pen.ondrag(dragging)

def draw(x: float, y: float) -> None:
    global xcor, ycor
    if x >= -400 and x <= 400 and y >= -300 and y <= 200:
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        xcor, ycor = x, y

start_filling = False
def check_fill() -> None:
    global start_filling
    if start_filling: pen.end_fill()
    else: pen.begin_fill()
    start_filling = not start_filling

# Keyboard and mouse bindings
wn.listen()
wn.onkeypress(lambda: pen.pensize(1) , "1")
wn.onkeypress(lambda: pen.pensize(5) , "2")
wn.onkeypress(lambda: pen.pensize(10) , "3")
wn.onkeypress(lambda: pen.pensize(15) , "4")
wn.onkeypress(lambda: pen.pensize(20) , "5")
wn.onkeypress(lambda: pen.clear() , "c")
wn.onkeypress(check_fill , "f")
wn.onscreenclick(draw)
pen.ondrag(dragging)


if __name__ == '__main__':
    wn.mainloop()