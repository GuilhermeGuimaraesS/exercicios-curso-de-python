# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extensão.
contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze', 'Desesseis', 'Dezessete', 'Dezoito',
            'Dezenove','Vinte',)

while True:  # Parte extra do Desafio
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Entrada Inválida... Tente novamente.', end=' ')
    print(f'O número {num} na forma extensa é {contagem[num]}.')
    while True:  # Parte extra do Desafio
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':  # Parte extra do Desafio
            break
    if resp == 'N':  # Parte extra do Desafio
        break
print('Programa Encerrado. Volte sempre!')  # Parte extra do Desafio
