sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu Sexo M/F]: ')).strip().upper()[0]
    if sexo != 'M' or sexo != 'F':
        print('Escolha Inválida! Tente Novamente')
if sexo == 'M':
    print('Sexo Masculino registrado com sucesso!')
elif sexo == 'F':
    print('Sexo Feminino registrado com sucesso!')
