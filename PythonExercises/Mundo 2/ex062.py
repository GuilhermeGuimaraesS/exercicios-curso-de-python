# Progressão Aritmética v3.0

a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
aN = a1 + (10 - 1) * r

cont = 1
termo = 0
total = 1

print('{} → '.format(a1), end='')
while termo < aN:
    termo = a1 + (cont) * r
    cont += 1
    print('{} → '.format(termo), end='')
    total += 1
print('PAUSA')

qnt = int(input('\nQuantos termos a mais você quer mostrar? (Se não quiser mais nenhum, aperte 0)'))

while qnt != 0:
    aN = a1 + ((10 + qnt) - 1) * r

    cont = 1
    termo = 0

    while termo < aN:
        termo = a1 + (cont) * r
        cont += 1
        print('{} → '.format(termo), end='')
        total += 1
    print('PAUSA')
    qnt = int(input('\nQuantos termos a mais você quer mostrar? (Se não quiser mais nenhum, aperte 0)'))
print('Progressão finalizada com {} termos mostrados'.format(total))
