vel = float(input('Qual a foi a velocidade do carro em Km/h, ao passar por este trecho? '))
multa = 7 * (vel-80)
if vel > 80:
    print('Você ultrapassou o limite deste trecho, que é 80 Km/h. Você irá pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Velocidade dentro do permitido!')
