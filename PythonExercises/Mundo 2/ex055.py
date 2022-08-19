print('=-' * 15)
print('COMPARADOR DE MASSA')
print('=-' * 15)

maior = 0
menor = 0

for p in range(1, 6):
    massa = float(input('Digite a massa (peso) da {}ª pessoa:(kg) '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if massa > maior:
            maior = massa
        if massa < maior:
            menor = massa

print('O maior peso lido foi {:.1f}kg.'.format(maior))
print('O menor peso lido foi {:.1f}kg.'.format(menor))
