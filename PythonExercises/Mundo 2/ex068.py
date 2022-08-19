from random import randint

escolhaPC = escolhaPlayer = ''
Vitória = True
totalV = 0

print('=-' * 15)
print('   VAMOS JOGAR PAR OU ÍMPAR   ')
print('=-' * 15)
while Vitória == True:
    computador = randint(0, 10)
    num = int(input('Diga um valor: '))
    while escolhaPlayer not in 'PI':
        escolhaPlayer = str(input('Par ou Ímpar? [P/I] ')).strip()[0].upper()
    if escolhaPlayer == 'P':
        escolhaPC == 'I'
    elif escolhaPlayer == 'I':
        escolhaPC == 'P'
    soma = computador + num  # Soma dos Números
    if soma % 2 == 0:  # Resultado == Par
        if escolhaPlayer == 'P':
            print(f'VOCÊ jogou {num} e o COMPUTADOR {computador}. Total de {soma} DEU PAR!')
            print('Você Venceu')
            print('Vamos Jogar novamente...')
            totalV += 1
        elif escolhaPlayer == 'I':
            Vitória = False
            print(f'VOCÊ jogou {num} e o COMPUTADOR {computador}. Total de {soma} DEU ÍMPAR!')
            print('Computador Venceu')
    elif soma % 2 == 1:  # Resultado == Ímpar
        if escolhaPlayer == 'I':
            print(f'VOCÊ jogou {num} e o COMPUTADOR {computador}. Total de {soma} DEU ÍMPAR!')
            print('Você Venceu')
            print('Vamos Jogar novamente...')
            totalV += 1
        elif escolhaPlayer == 'P':
            Vitória = False
            print(f'VOCÊ jogou {num} e o COMPUTADOR {computador}. Total de {soma} DEU ÍMPAR!')
            print('Computador Venceu')
print(f'GAME OVER! Você venceu {totalV} vezes.')
