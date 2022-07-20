def FirstFactorial(num): 
	num = int(num)
	factorial=1
    # code goes here
	if num<0:
		print("No factorial exists to this number")
	elif num==0:
		print("Factorial is 1")
	else:
		for i in range(1,num+1):
			factorial = factorial*i
	return factorial

# keep this function call here  
print(FirstFactorial(input()))