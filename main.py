from graphics import *

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
        win = GraphWin("Dice Roller", 600, 500)
        #squares
        aRectangle = Rectangle(Point(50,250), Point(250,450))
        bRectangle = Rectangle(Point(300,250), Point(500,450))
        #square colour
        aRectangle.setFill("white")
        bRectangle.setFill("white")
        #draw
        aRectangle.draw(win)
        bRectangle.draw(win)
        
        win.getMouse() 

DieView()
