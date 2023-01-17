# criar uma função chamada voto que vai receber o ano de nascimento
# a função vai retornar um valor literal informando se a pessoa tem voto NEGADO (< 16 anos), OPCIONAL (>= 16 anos e < 18 anos; ou > 70 anos) ou OBRIGATÓRIO (>= 18 e <= 70)

def voto(num):
    '''
    -> Recebe o ano de nascimento do cidadão, pega o ano atual, calcula a idade do cidadão e armazena na váriavel 'idade'. 
    :param num: ano de nascimento do cidadão
    :return: Obrigatoriedade de voto
    Função criada por Guilherme Guimarães dos Santos
    '''
    from datetime import date

    ano_atual = date.today() # Pegar o ano atual
    global idade
    idade = (ano_atual - num)
    if idade < 16:
        return 'NEGADO'
    elif (idade >= 16 and idade < 18) or (idade > 70):
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


# Programa principal

ano_nasc= int(input('Digite o ano de nascimento: '))
tipo_voto = voto(ano_nasc)
print(f'Idade do cidadão: {idade} anos. Voto {tipo_voto}!')
