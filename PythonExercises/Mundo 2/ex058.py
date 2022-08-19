# Advinhação v2.0

from random import randint
print('=-' * 15)
print('JOGO DA ADVINHAÇÃO')
print('=-' * 15)

sort = randint(0, 10)
print('Vou pensar um número entre 0 e 10... Tente advinha - lo!')

tentativas = 0
esc = 0

while esc != sort:
    esc = int(input('Digite a sua sugestão: '))
    if esc != sort:
        print('Erroooooou... Tente novamente!')
    tentativas += 1

print('!!! PARABÉNS !!!')
print('Você precisou de {} palpites para acertar!'.format(tentativas))
print('Número sorteado: {}'.format(sort))
