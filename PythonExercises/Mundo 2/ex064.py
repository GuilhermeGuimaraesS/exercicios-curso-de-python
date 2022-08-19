# Váriaveis

cont = num = soma = 0

num = int(input('Digite um número [999 para o programa]:'))
while num != 999:
    num = int(input('Digite um número [999 para o programa]:'))
    soma += num
    cont += 1

print('Soma: ', soma)
print('Quantidade de números digitados: {}'.format(cont))
