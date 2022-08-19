from time import sleep

num = []
pares = []
impares = []

while True:
    v = int(input('Digite um número: '))
    num.append(v)
#    if v % 2 == 0:
#        pares.append(v)
#    else:
#        impares.append(v)
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

for c in range(0, len(num)):
    if num[c] % 2 == 0:
        pares.append(num[c])
    elif num[c] % 2 != 0:
        impares.append(num[c])

print('-=' * 30)
sleep(2)
print(f'Os valores digitados foram: {num} e dentre eles', end='')
sleep(1)
print('.',  end='')
sleep(1)
print('.',  end='')
sleep(1)
print('.')
sleep(1)
print(f'{pares} são pares. ')
print(f'{impares} são ímpares. ')
