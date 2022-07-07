def Fibo(n):
	if n < 0:
		print("Erro")
		return None
	elif n == 1 or n == 2:
		return 1
	elif n > 2:
		return Fibo(n-1)+Fibo(n-2)
print(Fibo(6))