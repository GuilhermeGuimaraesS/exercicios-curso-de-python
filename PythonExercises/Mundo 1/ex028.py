import random
sort = random.randint(0, 5)
num = int(input('Digite um número entre 0 e 5: '))
if num == sort:
    print('Você acertou!')
else:
    print('Você errou!')
