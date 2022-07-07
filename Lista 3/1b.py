def imprime(n):
	if n==1:
		return print(1)
	else:
		
		return imprime(n - 1), print(n)
imprime(8)