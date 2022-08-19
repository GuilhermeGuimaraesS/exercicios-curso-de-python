from datetime import date

name = str(input('Qual o nome completo do(a) atleta? ')).strip().title()
nasc = float(input('Digite o Ano de Nascimento do(a) atleta, para vizualizar a categoria em que ele(a)'
                   ' está inserido(a): '))
name1 = name.split()
Tyear = date.today().year
nasc1 = int((Tyear - nasc))
if nasc1 <= 9:
    print('Como {} tem {} anos, ele(a) está na categoria Mirim!'.format(name1[0], nasc1))
elif nasc1 <= 14:
    print('Como {} tem {} anos, ele(a) está na categoria Infantil!'.format(name1[0], nasc1))
elif nasc1 <= 19:
    print('Como {} tem {} anos, ele(a) está na categoria Junior!'.format(name1[0], nasc1))
elif nasc1 <= 20:
    print('Como {} tem {} anos, ele(a) está na categoria Sênior!'.format(name1[0], nasc1))
elif nasc1 > 20:
    print('Como {} tem {} anos, ele(a) está na categoria Master!'.format(name1[0], nasc1))
