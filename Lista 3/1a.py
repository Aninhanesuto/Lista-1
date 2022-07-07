# importh string
# s = s.lower
# s = s.translate(None, string.punctuation)
# s = s.replace(" ", "" )

#def palindrome(s):
#	if s == s[::-1]:
#		return True
#	else:
#		return False

#print(palindrome("racecar"))
#print(palindrome("computer"))
s = int(input("Digite um número de 4 algarismos: "))
d = s//100
e = s//1000 % 10
def palindrome(s):
	if d == s:
		return True
	else:
		return False
print(e)
