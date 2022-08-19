nome = input('Qual o nome do funcionário? ')
sA = float(input('OK. E qual é o salário de {}? R$'.format(nome)))
sN = sA + (sA * 15/100)
print('Após o aumento de 15%, o salário de {}, que antes era R${:.2f}, passará a ser R${:.2f}'.format(nome, sA, sN))
