lista_temp = list()
caderneta = list()
notas_temp = list()
notas_f = list()
n_final = 0
ficha = []

while True:
    aluno = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n_final = (n1 + n2)/2
#    n_final_ar = round(n_final, 1)

    lista_temp.append(aluno)
    lista_temp.append(n1)
    lista_temp.append(n2)
    notas_temp.append(n1)
    notas_temp.append(n2)
    lista_temp.append(n_final)
    caderneta.append(lista_temp[:])
    notas_f.append(notas_temp[:])
    lista_temp.clear()
    notas_temp.clear()

#    ficha.append(aluno, [n1, n2], n_final)

    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
#print('Nº  NOME           MÉDIA')
print('-' * 25)
for cont in range(0, len(caderneta)):
    print(f'{cont:<4} {caderneta[cont][0]:<10} {caderneta[cont][3]:>8.1f}')
print('-' * 25)

while True:
    resp = int(input('Mostrar notas de qual aluno?  (999 interrompe) '))
    if resp == 999:
        break
    else:
        print(f'As notas de {caderneta[resp][0]} são {notas_f[resp]}')
    print('-' * 25)
