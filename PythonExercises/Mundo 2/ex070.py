from time import sleep

cont = preçoBarato = totalProduto = totalValor = mais1000 = 0
barato = resposta = ''
print('=-' * 15)
print('        BEST MARKET      ')
print('=-' * 15)
while True:
    name = str(input('Produto: ')).strip().title()
    preço = float(input('Preço: R$'))
    cont += 1
    if cont == 1 or preço < preçoBarato:
        preçoBarato = preço
        barato = name
    if preço >= 1000:
        mais1000 += 1  # Total de produtos que custam mais de R$1000.00
    totalProduto += 1  # Quantidade de produtos
    totalValor += preço  # Soma dos valores dos produtos
    while resposta not in 'S, N':
        resposta = str(input('Você quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('GERANDO NOTA FISCAL...')
sleep(3)
print('-' * 25)
print('   NOTA FISCAL  ')
print('-' * 25)
print(f'''COMPRA FINALIZADA COM SUCESSO
QUANTIDADE DE PRODUTOS: {totalProduto}
TOTAL DE PRODUTOS QUE CUSTAM MAIS DE R$1000: {mais1000}
PRODUTO MAIS BARATO: {barato} R${preçoBarato:.2f}
TOTAL GASTO: R${totalValor:.2f}''')
print('-' * 25)

