# Verificador de Números Primos

c = 1
contdiv = 0  # Quantidade de Divisores
num = int(input('Digite um número: '))

# A cada número contado, o programa divide o número digitado pelo número contado

for c in range(c, num + 1):
    if num % c == 0:
        contdiv += 1

# Análise da Quantidade de Divisores

if contdiv == 2:
    print('O número {} É PRIMO! '.format(num))
elif contdiv > 2:
    print('O número {} NÃO É PRIMO! '.format(num))


# Segunda Resolução

totDiv = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        totDiv +=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')

print('\n\033[mO número {} tem {} divisores!'.format(num, totDiv))
if totDiv == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')
