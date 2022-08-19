print('=' * 25)
print('Analisador de Triângulos')
print('=' * 25)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if abs(r2 - r3) < r1 < r2 + r3 and abs(r1 - r3) < r2 < r1 + r3 and abs(r1 - r2) < r3 < r1 + r2:
    print('Esses segmentos podem formar um triângulo.')
else:
    print('Esses segmentos não podem formar um triângulo.')
