from time import sleep

col1 = []
col2 = []
col3 = []
soma = 0
soma_c3 = 0
maior_l2 = 0

for c1 in range(0, 3):
    num1 = int(input(f'Digite um valor para [0, {c1}]: '))
    if num1 % 2 == 0:
        soma += num1
    if c1 == 0:
        col1.insert(0, num1)
    elif c1 == 1:
        col2.insert(0, num1)
    elif c1 == 2:
        col3.insert(0, num1)
        soma_c3 += num1

for c2 in range(0, 3):
    num2 = int(input(f'Digite um valor para [1, {c2}]: '))
    if num2 % 2 == 0:
        soma += num2
    if c2 == 0:
        col1.insert(1, num2)
    elif c2 == 1:
        col2.insert(1, num2)
    elif c2 == 2:
        col3.insert(1, num2)
        soma_c3 += num2

for c3 in range(0, 3):
    num3 = int(input(f'Digite um valor para [2, {c3}]: '))
    if num3 % 2 == 0:
        soma += num3
    if c3 == 0:
        col1.insert(2, num3)
    elif c3 == 1:
        col2.insert(2, num3)
    elif c3 == 2:
        col3.insert(2, num3)
        soma_c3 += num3

for cont in range(0, 3):
    if col1[1] > maior_l2:
        maior_l2 = col1[1]
    elif col2[1] > maior_l2:
        maior_l2 = col2[1]
    elif col3[1] > maior_l2:
        maior_l2 = col3[1]

print('-='*20)  
for pos in range(0, 3):
    print(f'[  {col1[pos]}  ][  {col2[pos]}  ][  {col3[pos]}  ]')
print('-='*20)

print('Analisando os valores da matriz', end='')
for cont in range(0, 3):
    sleep(1)
    print('.', end='')
sleep(1)

print(f'\nA soma dos valores pares entre os digitados é igual a: {soma}. ')
print(f'A soma dos valores da terceira coluna é igual a: {soma_c3}. ')
print(f'O maior valor entre os valores que estão na 2ª linha é: {maior_l2}. ')
