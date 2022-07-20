def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fatorial(n - 1)
# print(fatorial(8))
n = int(input("Digite um numero: "))
print(fatorial(n))

"""

def FirstFactorial(num): 
  for i in range(num-1,0,-1):
    num *= i
  return num
  
print(FirstFactorial(input()))

def FirstFactorial(num): 

    # code goes here
    factorial=1
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

"""