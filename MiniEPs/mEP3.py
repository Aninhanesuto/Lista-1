######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome: Ana Clara Sesana Moreira
# Matrícula: 2022100199
######################################################

def corretor(mulher):
	txt = ("da" if (mulher) else "do") 
	txt2 = ("A" if (mulher)  else "O")
	return txt, txt2

def indice(mulher, idade):
	if 18 <= idade <= 29:
		return 490  if (mulher) else 480
	elif 30 <= idade <= 34:
		return 500 if (mulher) else 490
	elif 35 <= idade <= 39:
		return 520 if (mulher) else 505
	elif 40 <= idade <= 44:
		return 540 if (mulher) else 515
	elif 45 <= idade <= 49:
		return 560 if (mulher) else 530
	elif 50 <= idade <= 54:
		return 580 if (mulher) else 540
	elif 55 <= idade <= 59:
		return 600 if (mulher) else 555
	elif 60 <= idade <= 64:
		return 630 if (mulher) else 570
	elif 65 <= idade <= 69:
		return 660 if (mulher) else 590
	elif 70 <= idade <= 74:
		return 705 if (mulher) else 620
	elif 75 <= idade <= 79:
		return 750 if (mulher) else 660
	elif idade >= 80:
		return 810 if (mulher) else 720

def conv(min):
	hora = min//60
	min -= hora*60
	return  f"{hora:02d}h {min:02d}min"

def main():
	sexo = input()
	idade = int(input())
	mulher = True if (sexo == "f" or sexo == "F") else False
	tempna = int(input())
	temptran1 = int(input())
	tempci = int(input())
	temptran2 = int(input())
	tempcor = int(input())
	temptotal = (tempna + temptran1 + tempci + temptran2 + tempcor)
	tempne = indice(mulher, idade)
	txt, txt2 = corretor(mulher)
	print(f'Tempo {txt} atleta: {conv(temptotal)}')
	print(f'Tempo necessario: {conv(tempne)}')
	if (tempne - temptotal) >= 0:
		print('Conseguiu indice? SIM')
		print(f"{txt2} atleta terminou a prova {conv(tempne - temptotal)} abaixo do indice")
	else:
		print('Conseguiu indice? NAO')
		print(f"{txt2} atleta terminou a prova {conv(temptotal - tempne)} acima do indice")
main()

