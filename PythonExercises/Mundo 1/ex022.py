name = str(input('Me diga seu nome completo: ')).strip()
up = name.upper()
down = name.lower()
outSpaces = len(name)-name.count(' ')
dividido = name.split()
cName = len(dividido[0])
print('Realizando uma análise, concluí-se que...')
print(' Seu nome com todas as letras maiúsculas é {}. \n Seu nome com todas as letras minúsculas é {}.'
      ' \n Seu nome possui {} letras. \n Seu primeiro nome é {} e tem {} letras.'
      .format(up, down, outSpaces, dividido[0], cName))
