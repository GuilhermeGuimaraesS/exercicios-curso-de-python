# Progressão Aritmética v2.0

print('=-' * 10)
print('GERADOR DE PA')
print('=-' * 10)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
aN = a1 + (10 - 1) * r

cont = 1
termo = 0

print(a1, ' → ', end='')
while termo < aN:
    termo = a1 + (cont) * r
    cont += 1
    print('{} → '.format(termo), end='')
print('FIM')
