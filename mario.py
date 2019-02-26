from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255, 0, 0]
O = [0, 0, 0]

def up():
  global r
  global O
    
  up = [
  O, O, O, r, O, O, O, O,
  O, O, r, r, r, O, O, O,
  O, r, r, r, r, r, O, O,
  r, r, r, r, r, r, r, O,
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O
  ]
  sense.set_pixels(up)
  
def down():
  global r
  global O
  
  down = [
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O,
  O, O, r, r, r, O, O, O,
  r, r, r, r, r, r, r, O,
  O, r, r, r, r, r, O, O,
  O, O, r, r, r, O, O, O,
  O, O, O, r, O, O, O, O
  ]
  
  sense.clear()
  sense.set_pixels(down)
down()

def upOrDown():
  event = sense.stick.wait_for_event()
  if(event.action == "pressed" and event.direction == "up"):
    sense.set_pixels(up)
    time.sleep(1)
    sense.set_pixels(down)
  if(event.action == "pressed" and event.direction == "down"):
    sense.clear()
    return 0
  upOrDown()
  
upOrDown()
