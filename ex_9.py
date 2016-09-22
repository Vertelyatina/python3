import numpy as np
import turtle as tt

tt.shape("turtle")
def archymedes(n):
	a = 20*(n - 1)*2*np.sin(np.pi/n)
	tt.left(180/n + 90)
	for i in np.arange(1, n + 1):
		tt.forward(a)
		tt.left(360/n)
	tt.right(180/n + 90)
	tt.penup()
	tt.forward(20)
	tt.pendown()
	
for i in np.arange(3, 17):
	archymedes(i)
