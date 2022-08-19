# Recebe a expressão digitada pelo usuário
express = str(input('Digite uma expressão: '))

# Inicialiazação de variaveis
prtE = prtD = 0

# Total de caracteres digitados na expressão
totCaract = len(express)

# O laço analisa quantos parênteses foram digitados na expressão, e cada vez que encontra um abrindo ou fechando, o valor da variável que conta cada um aumenta uma unidade
for c in range(0,  len(express)):
    if express[c] == '(':
        prtE += 1
    elif express[c] == ')':
        prtD += 1

# O laço verifica se o número de parênteses abrindo é igual ao de parênteses fechando, se for igual valida a expressão, senão, invalida a expressão
if prtE == prtD:   
    print('Sua expressão está válida! ')
else:
    print('Sua expressão está inválida! ')

#print(f'{prtE}')
#print(f'{prtD}')
