days = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Hmmm. E quantos quilômetros você percorreu durante esses dias? '))
value = float((60 * days) + (km * 0.15) )
print('Considerando os {} dias alugados e os {} Km rodados, têm-se um total de R${:.2f}. \n'
      'Visto que, a diária do carro custa R$60.00 e cada quilômetro rodado custa R$0.15.'.format(days, km, value))
