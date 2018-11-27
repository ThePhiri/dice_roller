from graphics import *
win = GraphWin("Dice Roller", 600, 500)
############## dice game logic ###########

#import packages
import random

class MSdie(object):
#constructor here
    def __init__(self, num_sides, value):
        self.value = value
        self.num_sides = num_sides

#define classmethod 'roll' to roll the MSdie
    def roll(self):
        self.roll_value = random.randint(1, self.num_sides)
        roll = self.roll_value
        return roll
#define classmethod 'getValue' to return the current value of the MSdie
    def getValue(self):
        return self.roll()
#define classmethod 'setValue' to set the die to a particular value
    def setValue(self):
        
        value_set = self.value
        return value_set


############## Die view ###########

class DieView:
    def __init__(self):
       
        #squares
        aRectangle = Rectangle(Point(50,250), Point(250,450))
        bRectangle = Rectangle(Point(300,250), Point(500,450))
        #square colour
        aRectangle.setFill("white")
        bRectangle.setFill("white")
        #draw
        aRectangle.draw(win)
        bRectangle.draw(win)
        self.dice_dots()

        win.getMouse() 
    
        

    def dice_dots(self):
        #top left dot
        d_dot1 = Circle(Point(80,300), 10) # set center and radius
        d_dot1.setFill("black")
        d_dot1.draw(win)

        #middle left dot



DieView()
