tempo = int(input("Digite o tempo total gasto na corrida (em min): "))
dist = int(input("Digite a distância percorrida (em km): ")) 
media = tempo//dist
valor = tempo%dist * 6
print("Ritmo medio do corredor: ",media,":",valor,"min/km")


