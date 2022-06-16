def soma(x1,x2,x3,x4,x5):
	count = 0
	count2 = 0
	SomaPar = 0
	SomaImpar = 0
	if x1%2 ==0: 
		count +=1
		SomaPar += x1
	else: 
		count2 += 1
		SomaImpar += x1
	if x2%2 ==0: 
		count +=1
		SomaPar += x2
	else: 
		count2 += 1
		SomaImpar += x2
	if x3%2 ==0: 
		count +=1
		SomaPar += x3
	else: 
		count2 += 1
		SomaImpar += x3
	if x4%2 ==0: 
		count +=1
		SomaPar += x4
	else: 
		count2 += 1
		SomaImpar += x4
	if x5%2 ==0: 
		count +=1
		SomaPar += x5
	else: 
		count2 += 1
		SomaImpar += x5
	soma = SomaPar
	soma2 = SomaImpar
	if count >0:
		media1 = soma/count

	if count2 >0:
		media2 = soma2/count2
	print(f"A soma dos números pares são {soma},  e dos números impares são {soma2} e a media dos números pares é {media1} e a media dos números ímpares é {media2}")

soma(9,4,1,3,5)
