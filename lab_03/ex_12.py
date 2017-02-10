import turtle as tt
import numpy as np

tt.shape("turtle")
tt.penup()
tt.goto(-200, 0)
tt.pendown()
tt.left(90)

def drawhalf(diam):
	for i in range(60):
		tt.forward(diam*np.pi/120)
		tt.right(3)
def drawsegm(d1, d2):
	drawhalf(d1)
	drawhalf(d2)

for i in range(4):
	drawsegm(120, 20)
