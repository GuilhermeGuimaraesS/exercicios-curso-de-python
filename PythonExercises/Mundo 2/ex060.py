num = int(input('Digite um número para calcular seu fatorial: '))

cont = num
fatorial = 1

while cont > 0:
    fatorial = fatorial * cont
    cont -= 1
print('O fatorial do número {} é {}'.format(num, fatorial))
