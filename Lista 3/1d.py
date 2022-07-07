def potenciacao(a,b):
	if b ==0:
		return 1
	elif b == 1:
		return a
	else:
		return a * potenciacao(a, b-1)
print(potenciacao(2, 10))