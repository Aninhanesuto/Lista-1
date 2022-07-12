def ascedente(n):
	d = (n//100) % 10
	c = (n//10) % 10
	u = n%10
	if type(n) != int or n<100 or n>999:
		print("Erro!")
		return False
	elif u>c>d:
		return True
	else:
		return False

print(ascedente(134))