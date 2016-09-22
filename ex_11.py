import turtle as tt
import numpy as np
tt.shape("turtle")
tt.left(90)

def drawpair(diam):
	drawcircle('right', diam)
	drawcircle('left', diam)
def drawcircle(angle, diam):
	if (angle == 'right'):
		for i in range(120):
			tt.forward(3*diam/120)
			tt.right(3)
	if (angle == 'left'):
		for i in range(120):
			tt.forward(3*diam/120)
			tt.left(3)

for i in range(50, 250, 25):
	drawpair(i)
	
