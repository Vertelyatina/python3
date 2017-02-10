print("Введите n:")
n = int(input())
a = ['even', 'odd']
i = 1
while i < n:
	print(i, a[i%2])
	i+=1

