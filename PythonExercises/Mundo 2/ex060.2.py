from time import sleep

num = int(input('Digite um número para ver seu fatorial: '))
cont = num
fatorial = 1
print('Calculando {}! ...'.format(num))
sleep(3)
print('{}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print('{}'.format(fatorial))
