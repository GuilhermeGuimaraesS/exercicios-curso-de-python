print('=-' * 15)
print('BANCO DOS GAFANHOTOS')
print('=-' * 15)

valor = int(input('Quanto você deseja sacar? '))
tot50 = tot20 = tot10 = tot1 = 0
ced50 = ced20 = ced10 = ced1 = 0

valorD = valor
while True:
    if valorD >= 50:
        tot50 = valorD - 50
        valorD = tot50
        ced50 += 1
    elif valorD >= 20:
        tot20 = valorD - 20
        valorD = tot20
        ced20 += 1
    elif valorD >= 10:
        tot10 = valorD - 10
        valorD = tot10
        ced10 += 1
    elif valorD >= 1:
        tot1 = valorD - 1
        valorD = tot1
        ced1 += 1
    elif valorD == 0:
        break
print('-' * 20)
print(f'''CÉDULAS DE R$50: {ced50}
CÉDULAS DE R$20: {ced20}
CÉDULAS DE R$10: {ced10}
CÉDULAS DE R$1: {ced1}
TOTAL SACADO: R${valor}''')
print('-' * 20)
