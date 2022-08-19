def Área(a, b):
    area_terreno = a * b
    print(f'A área desse terreno é {area_terreno} m². ')
def Lin(a):
    print('=' * a)

Lin(50)
print(f'{" CÁLCULO DE ÁREA ":^50}')
Lin(50)
larg = float(input('Largura do terreno (m): '))
compr = float(input('Comprimento do terreno (m): '))

Área(larg, compr)
