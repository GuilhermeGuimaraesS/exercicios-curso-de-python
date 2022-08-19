print("=-" * 15)
print("    INTERVALO DE 1 - 500")
print("=-" * 15)

# Execução do programa
print("-" * 28)
print("INFORMAÇÕES DESSE INTERVALO: ")
print("-" * 28)

# Variáveis

sImp3 = 0
totImp = 0
dvs3 = 0

for cont in range(1, 501):
   if cont % 2 == 1:
        totImp += 1
        if cont % 3 == 0:
           dvs3 += 1
           sImp3 += cont

print("TOTAL DE NÚMEROS ÍMPARES: {} ".format(totImp))
print("TOTAL DE NÚMEROS ÍMPARES E DIVISIVEIS POR 3: {} ".format(dvs3))
print("SOMA DOS NÚMEROS ÍMPARES E DIVISIVEIS POR 3: {} ".format(sImp3))

# Segunda Solução

dvs3 = 0
SomaImp3 = 0
for cont in range(1, 501, 2):
    if cont % 3 ==0:
        SomaImp3 += cont
        dvs3 += 1
print('A soma de todos os {} valores solicitados é igual a {}'.format(dvs3, SomaImp3))
