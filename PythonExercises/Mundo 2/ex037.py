num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases numéricas para conversão: 
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
esc = int(input('Sua escolha: '))
if esc == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif esc == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('ESCOLHA INVÁLIDA. TENTE OUTRA VEZ!')
