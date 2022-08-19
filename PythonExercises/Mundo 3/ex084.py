# bloco com inicialização das varíaveis
dados = []
temp =  []
totP = 0
maiP = menP = 0
max = []
min = []


while True:
    temp.append(str(input('Nome: ')).capitalize())
    temp.append(float(input('Peso(Kg): ')))
    dados.append(temp[:]) # adiciona os itens da lista temp na lista dados
    totP += 1
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

max.append(dados[0][0])
min.append(dados[0][0])

# i = índice; variável contadora
# p = peso de cada pessoa correspondente ao índice; ex: i == 1, p[0] == peso da pessoa na posição 1 

for i, p in enumerate(dados):
    if i == 0:
        maiP = menP = p[1]
    elif i > 0: 
# bloco que seleciona as pessoas mais pesadas
        if p[1] > maiP:
            maiP = p[1]
            max.clear()
            max.append(p[0])
        elif p[1] == maiP:
            max.append(p[0])
# bloco que seleciona as pessoas mais leves             
        elif p[1] < menP:
            menP = p[1]
            min.clear()
            min.append(p[0])
        elif p[1] == menP:
            min.append(p[0])
            
print('=-'*50)
print(f'No total, foram cadastradas {totP} pessoas. ')

print(f'O maior peso foi de {maiP}kg. Peso de: ', end='')
for c in range(0, len(max)):
    print(f'[{max[c]}] ', end='')
print()
print(f'O menor peso foi de {menP}kg. Peso de: ', end='')
for c in range(0, len(min)):
    print(f'[{min[c]}] ', end='')
print()
