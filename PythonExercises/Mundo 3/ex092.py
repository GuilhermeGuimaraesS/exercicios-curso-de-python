from datetime import date

dados = {}

dados['Nome'] = str(input('Nome: ')).capitalize()
ano_nasc = int(input('Ano de Nascimento: '))
dados['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
ano_atual = date.today().year
idade = (ano_atual - ano_nasc)
dados['Idade'] = idade

if dados['CTPS'] == 0:
    print('-=' * 25)
    for k, v in dados.items():
        print(f'    - {k} = {v} ')
        
elif dados['CTPS'] > 0:
    dados['Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    idade_aposent = (dados['Contratação'] + 35) - ano_nasc
    dados['Aposentadoria'] = idade_aposent
    print('-=' * 25)
    for k, v in dados.items():
        print(f'    - {k} = {v} ')
