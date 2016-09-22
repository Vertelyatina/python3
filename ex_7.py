import numpy as np
import turtle as tt

tt.shape("turtle")
for i in np.arange(50, 3600, 0.2):
	tt.forward(3)
	tt.left(360/i)
