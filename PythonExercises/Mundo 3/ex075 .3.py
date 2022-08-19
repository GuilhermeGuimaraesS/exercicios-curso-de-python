# O programa recebe quatro valores inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite um ultimo número: '))
num = (n1, n2, n3, n4)

print(f'Os números digitados foram: {num}. ')
# Verifica se o nove aparece e se ele aparece, mostra quantas vezes
vezesNove = num.count(9) 
print(f'O número nove aparece {vezesNove} vezes.')

# Verifica se o número três aparece e se ele aparece mostra quantas vezes e mostra em que posição ele aparece primeiro 
vezesTres = num.count(3)
if vezesTres == 0:
    print('O número três não aparece. ')
else:
    posTres = num.index(3)
    print(f'O número três aparece {vezesTres} vezes, e pela primeira vez na posição {posTres}.')

# Inicia duas variaveis, uma contabiliza a quantidade de números pares e a outra quantas vezes o número zero aparece
qntPares = 0 
vezesNul = 0
# Verifica quais são os números pares se houver pares mostra quais se não exibe a mensagem negando existência e mostra quantas vezes o número zero foi digitado
print('O(s) número(s) pares digitado(s): ')
for c in range(0, len(num)):
    if num[c] %2 == 0 and num[c] != 0:
        qntPares += 1
        print(f'{num[c]}', end=' ')
    elif num[c] == 0:
        vezesNul += 1
if qntPares == 0:
    print('Não foram digitados números pares.')
print(f'\nO número 0 aparece {vezesNul} vezes.')
