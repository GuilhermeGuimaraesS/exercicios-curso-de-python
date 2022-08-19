name = str(input('Qual o seu nome? ')).strip().title()
n1 = name.split()
vHouse = float(input('Qual o valor da casa que será adquirida? R$'))
s = float(input('Qual é o salário do comprador? R$'))
parcelas = int(input('Em quantos anos você deseja pagar o finaciamento? '))
parcelas1 = int(parcelas * 12)
mensalidade = float(vHouse / parcelas1)
if mensalidade <= (30 / 100) * s:
    print('O finaciamento foi aprovado. Tenha um bom dia, Sr(a) {}!'.format(n1[0]))
else:
    print('O financiamento foi negado, Sr(a) {}!'.format(n1[0]))
