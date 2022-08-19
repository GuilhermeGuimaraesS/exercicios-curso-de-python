# Variaveis

somaidade = 0
mulheresMenos20 = 0
idadeM = 0
nomeOld = ''

for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    name = str(input('Nome: ')).strip().title()
    nameD = name.split()
    idade = int(input('Idade de {}: '.format(nameD[0])))
    gen = str(input('Sexo [M/F]: ')).strip().title()
    somaidade += idade # Soma entre as idades do grupo
    if gen == 'M':
        if idade > idadeM:
            idadeM = idade
            nomeOld = nameD[0] # Homem mais velho
    elif gen == 'F':
        if idade < 20:
            mulheresMenos20 += 1 # Total de mulheres que tem menos de 20 anos
m = somaidade / 4

print('''Média de idade do grupo: {:.1f} anos
Homem mais velho: {} com {} anos
Quantidade de mulheres menores de 20: {}'''.format(m, nomeOld, idadeM, mulheresMenos20))
