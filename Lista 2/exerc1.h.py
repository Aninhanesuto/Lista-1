def converte(s):
	m = (s // 60) 
	r2 = m%60
	r = (s % 60)
	h = (s//3600)
	print(f"{h}:{m}:{r}")
s = int(input("Digite o valor em segundos: "))
converte(s)