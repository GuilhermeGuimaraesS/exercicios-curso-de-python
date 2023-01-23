def moeda(n = 0):
    """
    -> Converte o valor fornecido para um valor monetário
    :param n: valor que será convertido.
    :return: valor alterado e com R$.
    Função criada por Guilherme Guimarães dos Santos
    """
    n = f'{n:.2f}' # Deixa o valor com apenas duas casas decimais
    res = str(n).replace('.', ',') # Troca ponto por vírgula
    return f'R${res}'


def aumentar(n = 0, p = 0, formt=False):
    """
    ->  Aumenta o valor recebido do usuário de acordo com o percentual desejado.
    :param n: valor que será mudado.
    :param p: percentual de aumento.
    :param formt: (True formata, False não formata (padrão))variável para formatar ou não o valor retornado pela função.
    :return: valor com o aumento.
    Função criada por Guilherme Guimarães dos Santos
    """
    alter = n * (p / 100)
    res = n + alter
    if formt:
        return moeda(res)
    else:
        return res


def diminuir(n = 0, p = 0, formt=False):
    """
    ->  Diminue o valor recebido do usuário de acordo com o percentual desejado.
    :param n: valor que será mudado.
    :param p: percentual de redução.
    :param formt: (True formata, False não formata (padrão))variável para formatar ou não o valor 
    :return: valor com a redução
    Função criada por Guilherme Guimarães dos Santos
    """
    alter = n * (p / 100)
    res = n - alter
    if formt:
        return moeda(res)
    else:
        return res


def dobro(n = 0, formt=False):
    """
    -> Calcula o dobro do valor fornecido
    :param n: valor que será calculado.
    :param formt: (True formata, False não formata (padrão))variável para formatar ou não o valor 
    :return: dobro do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n * 2
    if formt:
        return moeda(res)
    else:
        return res


def metade(n = 0, formt=False):
    """
    -> Calcula a metade do valor fornecido
    :param n: valor que será calculado.
    :param formt: (True formata, False não formata (padrão))variável para formatar ou não o valor 
    :return: metade do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n / 2
    if formt:
        return moeda(res)
    else:
        return res


def título(msg):
    global tot_espaço
    tot_espaço = len(msg) + 16
    print('-' * tot_espaço)
    print( f'{msg.center(tot_espaço)}')
    print('-' * tot_espaço)


def resumo(n, perc_a = 0,  perc_r = 0):
    """
    -> Função que analisa um valor fornecido e retorna ele próprio, seu dobro, sua metade, aumento(taxa fornecida) e redução (taxa fornecida). A função guarda todos os dados em um dicionário
    :param n: valor que será analisado
    :param perc_a: percentual de aumento
    :param perc_r: percentual de redução
    Função criada por Guilherme Guimarães dos Santos
    """
    resultados = dict()
    resultados['Preço Analisado:'] = moeda(n)
    resultados['Dobro do preço:'] = dobro(n, True)
    resultados['Metade do preço:'] = metade(n, True)
    resultados[f'{perc_a}% de aumento:'] = aumentar(n, perc_a, True)
    resultados[f'{perc_r}% de redução:'] = diminuir(n, perc_r, True)
    
    título('RESUMO DO VALOR')
    for k in resultados:
        print(f'{k.ljust(20)} {resultados[k]}')
    print('-' * tot_espaço)

