print('=' * 25)
print('Calculador de IMC')
print('=' * 25)
print('Vão ser solicitados o seu peso(massa) e a sua altura, para que possamos calcular o seu IMC!')
peso = float(input('Informe o seu peso: (Kg) '))
h = float(input('Informe a sua altura: (m) '))
IMC = int(peso / (h ** 2))
if IMC < 18.5:
    print('Como seu IMC está {:.1f}, você está Abaixo do Peso. Se alimente melhor!'.format(IMC))
elif 18.5 <= IMC < 25:
    print('Parabéns!!! Como seu IMC está {:.1f}, você está com o Peso Ideal.'.format(IMC))
elif 25 <= IMC < 30:
    print('Cuidado! Como seu IMC está {:.1f}, você está Sobrepeso.'.format(IMC))
elif 30 <= IMC < 40:
    print('Como o seu IMC está {:.1f}, você precisa ir ao médico, infelizmente está em um grau de Obesidade!'.format(IMC))
elif IMC >= 40:
    print('Seu IMC está {:.1f}! Procure ajuda urgentemente, você está em um grau de Obesidade Mórbida!!!'.format(IMC))
