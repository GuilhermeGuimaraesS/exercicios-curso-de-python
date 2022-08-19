from time import sleep

num = []

while True:
    v = int(input('Digite um número: '))
    num.append(v)
    resp =  str(input('Você quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-=' * 30)
print('Analisando os dados inseridos', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

totList = len(num)
print(f'Foram digitados {totList} números!')
sleep(3)

num.sort(reverse=True)
print(f'Os valores adicionados, em ordem decrescente são: {num}.')
sleep(3)

if 5 not in num:
    print('O número 5 não foi digitado!')
else:
    print(f'O número 5 foi digitado, e está na posição {num.index(5)}. ')
