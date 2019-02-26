from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

x = 0
y = 0

def pixelator():
  global x
  global y
  number = randint(0, 2)
  
  if y == 7 and x == 8:
    y = 0
    x = 0
    time.sleep(1)
    
    O = [0, 0, 0]
    question_mark = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
    ]
    sense.set_pixels(question_mark)
    
    pixelator()
  else:
    if x > 7:
      x = 0
      y = y + 1
      pixelator()
    else:
      if number < 2:
        sense.set_pixel(x, y, (0, 0, 255))
        x = x + 1
        pixelator()
      else:
        x = x + 1
        pixelator()
  
pixelator()