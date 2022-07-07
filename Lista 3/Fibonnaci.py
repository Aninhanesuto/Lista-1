def fib(n):
	if n<=1:
		return n
	elif n>1:
		return fib(n-1)+fib(n-2)
n = int(input("Digite o número para calcular o Fibbonacci:"))
print(fib(n - 1))
