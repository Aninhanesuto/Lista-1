def Primo(n, i = 1,qt = 1):
	if n == i:
		return True if qt == 2 else False
	elif n % i == 0:
		return Primo(n, i+1, qt+1)
	elif n % i != 0:
		return Primo(n, i+1, qt)
	
print(Primo(744))