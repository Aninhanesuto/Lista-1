def divisores(n, i = 1,qt = 1):
	if n == i:
		return qt
	elif n % i == 0:
		return divisores(n, i+1, qt+1)
	elif n % i != 0:
		return divisores(n, i+1, qt)
	
print(divisores(80))