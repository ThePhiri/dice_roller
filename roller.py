from random import randrange
from graphics import *

from button import Button
from dieview import DieView
from msdie import MSdie

def main():

	# create the application window
	win = GraphWin("Dice Roller",)
	win.setCoords(0,0,12,12)
	win.setBackground("green")

	

	roll_btn = Button(win, Point(3,2), 3, 3, "Roll")
	quit_btn = Button(win, Point(7,2), 3, 3, "Quit")

	d1 = DieView(win, Point(3,6), 3)
	d2 = DieView(win, Point(7,6), 3)

	#

	while True:
		if roll_btn.clicked(win.getMouse()):
			d1.setValue(MSdie(6).roll())
			d2.setValue(MSdie(6).roll())
		elif quit_btn.clicked(win.getMouse()):
			return False

	

	# close the window
	win.close()

main()