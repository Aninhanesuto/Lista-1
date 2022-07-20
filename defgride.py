def gride_paths(n,m):
	if n  == 1 or m == 1:
		return 1
	else:
		return gride_paths(n, m - 1) + gride_paths(n - 1, m)

print(gride_paths(10,10))

