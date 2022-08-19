cadastro = {}
base_dados = []
mulheres = []
acima_media = []
i = 0
s_idade = 0

while True:
    cadastro['Nome'] = str(input('Nome: ')).capitalize()
    while True:
        cadastro['Sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if cadastro['Sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    if cadastro['Sexo'] in 'F':
        mulheres.append(cadastro['Nome'])
    cadastro['Idade'] = int(input('Idade: '))
    s_idade += float(cadastro['Idade'])
    base_dados.append(cadastro.copy())
    cadastro.clear()
    i += 1
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N. ')
    if resp == 'N':
        break

tot_pessoas = i
media_idade = (s_idade / tot_pessoas)

for pessoa in base_dados:
    for k, v in pessoa.items():
        if k == 'Idade' and v > media_idade:
            acima_media.append(pessoa.copy())

print('-=' * 30)
print(f'Foram cadastradas um total de {tot_pessoas} pessoas. ')
print(f'A média de idade do grupo é {media_idade:.1f} anos. ')
print(f'As mulheres cadastradas foram: ', end='')
for c in range(0, len(mulheres)):
    print(mulheres[c], end=' ')
print()
print('-' * 50)
print('As pessoas que estão acima da Média de Idade são: ')
print('-' * 50)
for pessoa in acima_media:
    for k, v in pessoa.items():
        print(f'{k} = {v}; ', end='')
    print()
    print()
print('-=' * 30)
