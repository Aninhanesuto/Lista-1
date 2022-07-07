def corredor(h, m, s, km):
	min = (h * 60) + m + s/60
	calculo = min/km
	min2 = round(calculo, 0)
	s2 = round(calculo % 60, 2)
	return min2, s2

def main():
	print("Tempo do corredor (horas, minutos e segundos):")
	h = float(input())
	m =  float(input())
	s =  float(input())
	km = float(input("Distância percorrida (em km): "))
	min2, s2 = corredor(h, m, s, km)
	print(f"Ritmo: {min2}:{s2} min/km")

main()