from sense_hat import SenseHat
import time
sense = SenseHat()

x = 0
y = 0

def pixelator():
  global x
  global y
  
  if y == 7 and x == 8:
    y = 0
    x = 0
    pixelator()
  else:
    if x > 7:
      x = 0
      y = y + 1
      pixelator()
    else:
      sense.set_pixel(x, y, (0, 0, 255))
      time.sleep(0.3)
      sense.set_pixel(x, y, (0, 0, 0))
      x = x + 1
      pixelator()
  
  
pixelator()