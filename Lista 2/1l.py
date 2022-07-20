def Palindrome(n):
	u = n // 1 % 10
	d = n // 10 % 10
	c = n // 100 % 10
	m = n // 1000 % 10
	if type(n) != int or  1000 > n > 9999:
		print("Erro!")
		return None
	if (u+d) == (c + m): return True
	else: return False

print(Palindrome(6886))