caderneta = list()

while True:
    aluno = str(input('Nome: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2:  '))
    n_final = (n1 + n2) / 2
    caderneta.append([aluno, [n1, n2], n_final])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')

print('-' * 25)
# i= variável contadora; d_aluno: dados do aluno
for i, d_aluno in enumerate(caderneta): 
    print(f'{i:<4}{d_aluno[0]:<10}{d_aluno[2]:>8.1f}')
print('-' * 25)

while True:
    resp = int(input('Mostrar notas de qual aluno?  (999 interrompe) '))
    if resp == 999:
        break
    else:
        print(f'As notas de {caderneta[resp][0]} são {caderneta[resp][1]}. ')
    print('-' * 25)
