palavras = ('Casa', 'Garagem', 'Escritorio', 'Setup')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ')
    for vog in palavra:
        if vog.lower() in 'aeiou':
            print(f'{vog}', end=' ')
