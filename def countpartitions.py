def count_partitions(n,m):
	if n == 0:
		return 1
	elif m == 0 or n< 0:
		return 0
	else:
		return count_partitions(n - m, m) + count_partitions(n, m -1)


