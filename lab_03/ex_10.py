import turtle as tt
import numpy as np
tt.shape("turtle")

def pair():
	drawcircle('right')
	drawcircle('left')
def drawcircle(angle):
	if (angle == 'right'):
		for i in range(120):
			tt.forward(2)
			tt.right(3)
	if (angle == 'left'):
		for i in range(120):
			tt.forward(2)
			tt.left(3)
for i in range(5):
	pair()
	tt.right(360/5)
