name = str(input('Digite seu nome completo: ')).strip().title()
dividido = name.split()
print('Prazer em conhecer você!')
print('Seu primeiro nome é {}'.format(dividido[0]))
print('Seu último nome é {}'.format(dividido[len(dividido)-1]))
