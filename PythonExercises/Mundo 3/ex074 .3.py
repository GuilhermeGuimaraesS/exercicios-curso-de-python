from random import randint

maior = menor = 0
print('Os valores sorteados foram: ', end='')
for cont in range(1, 6):
    sort = randint(0, 10)
    if cont == 1:
        maior = menor = sort
    else:
        if sort > maior:
            maior = sort
        elif sort < menor:
            menor = sort
    print(sort,'', end=' ')
print(f'\nO maior número sorteado foi {maior}.')
print(f'O menor número sorteado foi {menor}.')
