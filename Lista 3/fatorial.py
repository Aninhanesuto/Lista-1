def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fatorial(n - 1)
# print(fatorial(8))
n = int(input("Digite um numero: "))
print(fatorial(n))