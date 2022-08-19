num1 = int(input('Digite um valor: '))
num2 = int(input('Digite mais um valor: '))
num3 = int(input('Digite outro valor: '))
num4 = int(input('Digite o último valor: '))

lista = (num1, num2, num3, num4)
# Números Pares
print('-' * 30)
print('Os números pares são: ', end='')
for cont in range(0, 4):
    if lista[cont] % 2 == 0:
        pares = lista[cont]
        print(pares, '', end='')
# Quantidadede vezes em que o número 9 aparece
qnt9 = lista.count(9)
print(f'\nO número 9 apareceu {qnt9} vezes.')
# Posição em que o número 3 aparece
if 3 in lista:
    pos3 = lista.index(3)
    print(f'O número 3 apareceu na {pos3 + 1}ª posição.')
else:
    print('O número 3 não apareceu')
print('-' * 30)
