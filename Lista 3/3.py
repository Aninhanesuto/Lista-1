#def perfeitos(n, i =1, s = 0):
	





def ehPerfeito(n, i = 1, s = 0):
	if n == i:
		return True if s==n else False
	elif n % i == 0:
		return ehPerfeito(n, i+1, s + i)
	elif n % i != 0:
		return ehPerfeito(n, i+1, s)
	
print(ehPerfeito(496))


#def main():
	#n = int(input("Digite um número natural: "))
	#ehPerfeito(n)