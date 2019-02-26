from sense_hat import SenseHat
import time

sense = SenseHat()

r = [255, 0, 0]
O = [0, 0, 0]
def rectangle():
	r1 = [
		r,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
	]
	r2 = [
		r,r,r,r,O,O,O,O,
		r,O,O,r,O,O,O,O,
		r,O,O,r,O,O,O,O,
		r,r,r,r,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
	]
	r3 = [
		r,r,r,r,r,r,O,O,
		r,O,O,O,O,r,O,O,
		r,O,O,O,O,r,O,O,
		r,O,O,O,O,r,O,O,
		r,O,O,O,O,r,O,O,
		r,r,r,r,r,r,O,O,
		O,O,O,O,O,O,O,O,
		O,O,O,O,O,O,O,O,
	]
	r4 = [
		r,r,r,r,r,r,r,r,
		r,O,O,O,O,O,O,r,
		r,O,O,O,O,O,O,r,
		r,O,O,O,O,O,O,r,
		r,O,O,O,O,O,O,r,
		r,O,O,O,O,O,O,r,
		r,O,O,O,O,O,O,r,
		r,r,r,r,r,r,r,r,
	]
	
	sense.set_pixels(r1)
	time.sleep(0.5)
	sense.set_pixels(r2)
	time.sleep(0.5)
	sense.set_pixels(r3)
	time.sleep(0.5)
	sense.set_pixels(r4)
	time.sleep(0.5)
	sense.set_pixels(r3)
	time.sleep(0.5)
	sense.set_pixels(r2)
	time.sleep(0.5)
	rectangle()
rectangle()
