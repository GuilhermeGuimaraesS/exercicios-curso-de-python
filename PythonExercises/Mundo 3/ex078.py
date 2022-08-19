# Inicialização de variaveis 
num = list() 
maior = menor = 0
posMax = num.index(maior)
posMin = num.index(menor)
 
# Laço que recebe os números e guarda dentro da lista e identifica o maior e o menor valor digitado pelo usuário
for cont in range(0, 5):
    num.append(int(input('Digite um número: ')))
    if cont == 1:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        elif num[cont] < menor:
            menor = num[cont]
# Mostra a lista contendo os números digitados 
print(f'Os números digitados foram: {num}, dentre eles')

print(f'O maior valor digitado foi: {maior}, que aparece na(s) posição(s): ')

# Mostra uma ou mais posições em que o maior valor se encontra
for c in range(posMax, len(num)):
    if num[c] == maior:
        print(f'{c}', end='... ')

print(f'\nO menor valor digitado foi: {menor}, que aparece na(s) posição(s): ')

# Mostra uma ou mais posições em que o menor valor se encontra
for c in range(posMin, len(num)):
    if num[c] == menor:
        print(f'{c}', end='... ')
