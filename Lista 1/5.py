contaPar = 0
contarImpar = 0
somaPar=0
somaImpar = 0
x = int(input("Digite um número: "))
if x%2 == 0:
    contaPar += 1 # contaPar = contaPar +1
    somaPar+=x
else:
    contarImpar += 1
    somaImpar+=x
x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1
    somaPar+=x 
else:
    contarImpar +=1
    somaImpar+=x
x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1
    somaPar+=x
else:
    contarImpar +=1
    somaImpar
x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1
    somaPar+=x
else:
    contarImpar +=1
    somaImpar+=x
print(f"Foram digitados {contaPar} números pares")
print(f"Foram digitados {contarImpar} números pares")
print(f"Soma dos números pares: {somaPar}")  
print(f"Soma dos números pares: {somaImpar}")  
if contaPar > 0:
	print(f"Média dos números pares: {somaPar/contaPar:.2f}") # :.2f -> para imprimir com duas casas decimais
if contarImpar > 0:
	print(f"Média dos números pares: {somaImpar/contarImpar:.2f}") # :.2f -> para imprimir com duas casas decimais
