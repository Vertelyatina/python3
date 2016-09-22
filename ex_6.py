import turtle as tt
print("Введите n:")
n = int(input())

tt.shape("turtle")
for i in range(1, n + 1, 1):
	tt.forward(150)
	tt.stamp()
	tt.penup()
	tt.goto(0, 0)
	tt.left(360/n)
	tt.pendown()
	
