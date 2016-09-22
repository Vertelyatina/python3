import turtle as tt
tt.shape('turtle')

def sqtt(a):
	for i in range(4):
		tt.forward(a)
		tt.left(90)

for i in range(10, 110, 10):
	tt.penup()
	tt.goto(-i, -i)
	tt.pendown()
	sqtt(2*i)	
