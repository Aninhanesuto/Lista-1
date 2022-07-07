def imprime(a,b):
	if a == b:
		return 
	
	elif a < b:
		print(a)
		return imprime(a+1, b)

imprime(3,3)