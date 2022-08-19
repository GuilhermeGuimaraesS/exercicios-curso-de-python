from datetime import date

print('=-' * 15)
print('  VERIFICADOR DE MAIOR IDADE  ')
print('=-' * 15)

# Variáveis

maior = 0
menor = 0
atual = date.today().year

for c in range(1, 8):
    name = str(input('Digite o nome completo da {}ª pessoa: '.format(c))).strip().title()
    nameD = name.split() # Divide o nome declarado
    nasc = int(input('Digite o ano de nascimento de {}: '.format(nameD[0])))
    idade = atual - nasc
    if idade >= 21:
        maior = maior + 1
    elif idade < 21:
        menor = menor + 1

print('''Temos {} pessoas MAIORES DE IDADE
e também {} pessoas MENORES DE IDADE!'''.format(maior, menor))
