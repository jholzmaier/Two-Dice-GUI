"""
Program: two_diceGUI.py
Author: Jaclyn 7/18/2023

GUI-Based version of the two dice game which compares random numbers and provides the game's outcome

NOTE: The file breezypythonGUI.py MUST be in the same directory as this file for the app to run correctly!

"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font 
# Other Imports go here

# Class Header (Application name will change project to project)
class TwoDiceGUI(EasyFrame):
	# Definition of our class constructor method 
	def __init__(self):
		#Call to the Easy Frame Constructor Method
		EasyFrame.__init__(self, title = "Two Dice Game", width = 340, height = 280, resizable = False, background = "seagreen")
		# Add the various components to the window 
		self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan =2, sticky = "NSEW", background = "seagreen", font = Font(family = "Impact", size = 24))
		self.addLabel(text = "Player's Roll is:", row = 1, column = 0, sticky ="NE", background = "seagreen")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly", sticky = "NW")
		self.addLabel(text = "Computer's Roll is:", row = 1, column = 0, sticky = "NE", background = "seagreen")
		self.computerRoll = self.addIntegerField(value = 0, row = 2, column = 1, width = 4, state = "readonly", sticky = "NW")
		self.button = self.addButton(text = "Roll Dice!", row = 3, column = 0, columnspan = 2, command = self.roll)
		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, background = "seagreen", foreground = "yellow", font = Font(family = "Georgia", size = 20), sticky = "NSEW")
	# Definition of Roll() Function
	def roll(self):
		# Variables for this Function
		playerDie = random.randint(1, 6)
		compDie = random.randint(1, 6)
		if playerDie > compDie:
			result = "Congratulations, You Win!"
			self.resultArea["foreground"] = "yellow"
		elif playerDie < compDie:
			result = "Sorry, You Lost..."
			self.resultArea["foreground"] = "red"
		else: 
			result = "We have a tie."
			
			self.resultArea["foreground"] = "white"

		# Output Phase
		self.playerRoll.setNumber(playerDie)
		self.computerRoll.setNumber(compDie)
		self.resultArea["text"] = result

		# Processing Phase 

# Global definition of the main() method
def main():
	# Instantiate an object from the class into the mainloop()
	TwoDiceGUI().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()