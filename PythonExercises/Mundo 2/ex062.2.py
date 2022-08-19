print('=-' * 10)
print('GERADOR DE PA')
print('=-' * 10)
a1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))

cont = 1
termo = 0
mais = 10

while mais != 0:
    total += mais
    print(a1, ' → ', end='')
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo += r
        cont += 1
    print('FIM')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressaõ finalizada com {} termos mostrados'.format(total))
