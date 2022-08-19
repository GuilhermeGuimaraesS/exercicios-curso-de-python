soma = cont = maior = menor = 0  # Variáveis Inteiras
resposta = 'S'  # Variável String
while resposta in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Você quer continuar [S/N]? ')).strip()[0].upper()
média = soma / cont
print('Média: {:.2f}'.format(média))
print('''Maior: {}
Menor: {}'''.format(maior, menor))
