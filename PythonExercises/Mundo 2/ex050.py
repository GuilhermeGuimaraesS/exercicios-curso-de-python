# Soma de números pares

nPar = 0
sPar = 0
cont = 0
for cont in range(1, 7):
    num = int(input(f'Digite o {cont}º número: '))
    cont += 1
    if num % 2 == 0:
        nPar += 1
        sPar += num
print(f'Você digitou {nPar} números PARES, a soma deles é {sPar}.')
