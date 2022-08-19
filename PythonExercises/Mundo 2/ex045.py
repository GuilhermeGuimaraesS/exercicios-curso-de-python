from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
print('=' * 25)
print('PEDRA, PAPEL, TESOURA')
print('=' * 25)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
esc = int(input('Escolha: '))
if esc >=3:
    print('!!!JOGADA INVÁLIDA!!!')
else:
    print('PEDRA')
    sleep(1)
    print('PAPEL')
    sleep(1)
    print('TESOURA')
    pc = randint(0, 2)
    print('=' * 22)
    print('Computador escolheu {}'.format(itens[pc]))
    print('Jogador escolheu {}'.format(itens[esc]))
    print('=' * 22)
    if pc == 0:  #COMPUTADOR JOGOU PEDRA
        if esc == 0:
            print('EMPATE!')
        elif esc == 1:
            print('JOGADOR VENCEU!')
        elif esc == 2:
            print('COMPUTADOR VENCEU!')
    elif pc == 1:  #COMPUTADOR JOGOU PAPEL
        if esc == 0:
            print('COMPUTADOR VENCEU!')
        elif esc == 1:
            print('EMPATE!')
        elif esc == 2:
            print('JOGADOR VENCEU!')
    elif pc == 2:  #COMPUTADOR JOGOU TESOURA
        if esc ==  0:
            print('JOGADOR VENCEU!')
        elif esc == 1:
            print('COMPUTADOR VENCEU!')
        elif esc == 2:
            print('EMPATE!')
