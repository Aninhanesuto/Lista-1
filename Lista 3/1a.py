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
def palindrome(n,m):
	if n > m:
		return n
	elif  n // 100 == n % 100:
			print(n)
			return palindrome(n+1, m)
	else:
			return palindrome(n+1, m)

print(palindrome(1000, 9999))