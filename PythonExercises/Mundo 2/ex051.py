# Progressão Aritmética

print('=' * 25)
print('  10 TERMOS DE UMA PA  ')
print('=' * 25)

a1 = int(input('Primeiro Termo: '))
r = int(input('Razão da P.A: '))
a11 = a1 + (10 * r)
for c in range(a1, a11 + r, r):
    print(c, end=' ')
