print('=' * 25)
print('Analisador de triângulos')
print('=' * 25)
print('Digite três segmentos, e será mostrado se é possível formar um triângulo, e se sim, qual tipo.')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r3:
    print('Esses segmentos podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Esses segmentos não podem formar um triângulo.')
