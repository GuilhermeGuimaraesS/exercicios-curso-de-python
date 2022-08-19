listagem = ('Lápis', 1.75,
            'Borracha',2,
            'Caderno',15.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇO":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>.2f}')
print('-' * 40)
