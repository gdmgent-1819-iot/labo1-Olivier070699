import time
from sense_hat import SenseHat
from random import randint

sense = SenseHat()

def showLetters():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  
  sense.show_letter('N', text_colour=[r, g, b])
  time.sleep(1)
  sense.show_letter('M', text_colour=[r, g, b])
  time.sleep(1)
  sense.show_letter('D', text_colour=[r, g, b])
  time.sleep(1)
  showLetters()
showLetters()