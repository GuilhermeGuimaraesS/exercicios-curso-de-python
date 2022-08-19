from time import sleep

ficha = dict()
ficha['Nome'] = str(input('Nome: ')).capitalize()
ficha['Média'] = float(input(f'Média de {ficha["Nome"]}: '))

if ficha['Média'] >= 7:
    ficha['Situação'] = 'Aprovado'
elif ficha['Média'] < 7 and ficha['Média'] >= 5:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'

sleep(0.5)
print('-=' * 30)
for k, v in ficha.items():
    sleep(0.5)
    print(f'    - {k} é igual a {v}! ')   
print('-=' * 30)
