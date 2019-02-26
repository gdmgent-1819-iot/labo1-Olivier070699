from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

def pixelator():
  r = randint(0, 255)
  g = randint(0, 255)
  b = randint(0, 255)
  
  sense.show_message("Hello! We are New Media Development :)", text_colour=[r, g, b])
  time.sleep(1)
  pixelator()
  
pixelator()
