def reverstr(a):
	if a == "": return a
	else:
		print(a[len(a) - 1], end = "")
		return reverstr(a[0:len(a) - 1])

reverstr("hello")