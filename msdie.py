#class definition for an n-sided die
import random

class MSdie:

  #Current die value
  current_val = 0

  def __init__(self,numOfSides):
    self.numOfSides = numOfSides

  #define classmethod 'roll' to roll the MSdie
  # 
  def roll(self):

    if self.current_val != 0:
      return self.current_val
    else:
      self.current_val = random.randint(1, self.numOfSides)
      return self.current_val

  def getValue(self):

    return self.current_val

  def setValue(self, value):
    self.current_val = value