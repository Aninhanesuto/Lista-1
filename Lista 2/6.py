def Propriedade(n):
	n1 = n // 100
	n2 = n % 100
	if n < 1000: return False
	elif (n1 + n2) ** 2 == n: return True
	else: return False

def main():
	x = int(input("Digite um valor de 4 digitos: "))
	x = Propriedade(x)
	print(f"Esse número tem esse propriedade: {x}")

main()