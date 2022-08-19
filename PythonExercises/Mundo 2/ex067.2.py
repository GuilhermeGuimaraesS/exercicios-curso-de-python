from time import sleep

cont = num = 0
print('=' * 20)
print('  TABUADA v3.0  ')
print('=' * 20)
while True:
    num = int(input('Digite um número para vizualizar a sua tabuada  [Número negativo encerra o programa]: '))
    print('-' * 20)
    if num < 0:
        break
    for cont in range(0, 10):
        cont += 1
        print(f'{num:2} x {cont:2} = {(num * cont):2}')
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRANDO...')
sleep(1)
print('OBRIGADO E VOLTE SEMPRE!')
