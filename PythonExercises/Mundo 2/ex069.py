total = maiores18 = totHomens = mulheres20 = 0
resposta = 'Ss'
print('=-' * 15)
print('     CADASTRO DE PESSOAS   ')
print('=-' * 15)
while resposta != 'Nn':
    idade = int(input('Idade: '))
    if idade > 18:
        maiores18 += 1  # Total de pessoas maiores de 18
    sexo = ''
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'M':
        totHomens += 1  # Total de homens cadastrados
    if sexo == 'F' and idade < 20:
        mulheres20 += 1  # Total de Mulheres com menos de 20 anos
    total += 1
    resposta = ''
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
    if resposta == 'N':
        break
print('-' * 25)
print('CADASTRO FINALIZADO COM SUCESSO!')
print(f'''TOTAL DE CADASTROS: {total}
MAIORES DE 18: {maiores18}
TOTAL DE HOMENS CADASTRADOS: {totHomens}
TOTAL DE MULHERES MENORES DE 20: {mulheres20}''')
print('-' * 25)
