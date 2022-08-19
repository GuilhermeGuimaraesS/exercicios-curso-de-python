from datetime import date

print('=' * 25)
print('Alistamento Militar')
print('=' * 25)
gen = str(input('Você é Homem ou Mulher? ')).strip().title()
if gen == 'Homem':
    nasc = int(input('Qual o ano que você nasceu? '))
    atual = date.today().year
    idade = atual - nasc
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
    if idade == 18:
        print('Analisando o ano que você nasceu, concluí-se que você deve se alistar IMEDIATAMENTE.')
    elif idade < 18:
        a2 = (18 - idade)
        ano = atual + a2
        if a2 == 1:
            print(
                'Analisando o ano que você nasceu, concluí-se que ainda falta {} ano para você realizar o alistamento.'
                    .format(a2))
            print('Seu alistamento foi em {}'.format(ano))
        else:
            print(
                'Analisando o ano que você nasceu, concluí-se que ainda falta {} anos para você realizar o alistamento.'
                    .format(a2))
            print('Seu alistamento será em {}.'.format(ano))
    elif idade > 18:
        a3 = (idade - 18)
        ano = atual - a3
        if a3 == 1:
            print('Analisando o seu ano de nascimento, concluí se que você ultrapassou {} ano do prazo para se alistar.'
                  .format(a3))
            print('Seu alistamento foi em {}'.format(ano))
        else:
            print('Analisando o ano que você nasceu, concluí-se que você ultrapassou {} anos do prazo para se alistar.'
                  .format(a3))
            print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Como você é mulher, não precisa realizar o Serviço Militar Obrigatório!!!')
