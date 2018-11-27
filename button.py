from graphics import *

class Button:
    def __init__(self):
        win = GraphWin("Dice Roller", 800, 800)
        aRectangle = Rectangle(Point(100,300), Point(300,400))
        aRectangle.setFill("white")
        bRectangle = Rectangle(Point(200,300), Point(300,400))
        bRectangle.setFill("white")
        bRectangle.setFill("white")
        aRectangle.draw(win)
        bRectangle.draw(win)
        win.getMouse() 

Button()
