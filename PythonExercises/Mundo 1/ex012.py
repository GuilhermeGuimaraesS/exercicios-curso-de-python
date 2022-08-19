pO = float(input('Qual o preço original do produto? R$'))
pD = float(pO - (pO * (5/100)))
print('Após aplicar o desconto de 5% sobre o preço original do produto, o novo valor será R${:.2f}.'.format(pD))
