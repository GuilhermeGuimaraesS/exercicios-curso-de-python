from random import randint

# Variáveis
maior = menor = 0
# Sorteio de números
print('Os valores sorteados foram: ', end='')
for cont in range(1, 6):
    sort = randint(0, 10)
    # Verificação de maiores e menores dentre os números sorteados
    if cont == 1:
        maior = menor = sort
    else:
        if sort > maior:
            maior = sort
        elif sort < menor:
            menor = sort
    print(sort,'', end='')
print(f'\nO maior número sorteado foi: {maior}')  # Mostra o maior número sorteado
print(f'O menor número sorteado foi: {menor}')  # MOstra o menor número sorteado
