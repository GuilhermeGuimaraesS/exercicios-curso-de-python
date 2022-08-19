print('{:=^40}'.format(' Lojas GTech '))

valor = float(input('Qual o valor das compras? R$'))
pType = int(input('''O pagamento será realizado: 
[ 1 ] À vista
[ 2 ] Parcelado no Cartão
Opcão: '''))
if pType == 1:
    condc = str(input('Certo. Via dinheiro, cartão ou cheque? ')).strip().title()
    if condc == 'Dinheiro' or 'Cheque':
        print('Você terá um desconto de 10% sobre o valor original, totalizando R${:.2f}'
              .format(valor - (valor * (10 / 100))))
    if condc == 'Cartão':
        print('Você terá um desconto de 5% sobre o valor original, totalizando R${:.2f}'
              .format(valor - (valor * (5/100))))
elif pType == 2:
    condc1 = int(input('Em quantas vezes você irá parcelar? ')).strip()
    if condc1 == 1:
        print('Você irá pagar o valor original.')
    if condc1 == 2:
        print('Você irá pagar o valor original em 2x de R${:.2f} SEM JUROS'.format(valor / 2))
    elif condc1 >= 3:
        acrs = valor + (valor * 20 / 100)
        print('O valor inicial da compra sofrerá um acréscimo de 20%, totalizando R${:.2f}'.format(acrs))
        print('E serão {} parcelas de R${:.2f} cada.'.format(condc1, (acrs / condc1)))
else:
    print('Opção inválida. Tente novamente!')
