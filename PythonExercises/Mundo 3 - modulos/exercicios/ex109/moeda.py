def aumentar(n = 0, p = 0):
    """
    ->  Aumenta o valor recebido do usuário de acordo com o percentual desejado.
    :param n: valor que será mudado.
    :param p: percentual de aumento.
    :return: valor com o aumento.
    Função criada por Guilherme Guimarães dos Santos
    """
    alter = n * (p / 100)
    res = n + alter
    return res


def diminuir(n = 0, p = 0):
    """
    ->  Diminue o valor recebido do usuário de acordo com o percentual desejado.
    :param n: valor que será mudado.
    :param p: percentual de redução.
    :return: valor com a redução
    Função criada por Guilherme Guimarães dos Santos
    """
    alter = n * (p / 100)
    res = n - alter
    return res


def dobro(n = 0):
    """
    -> Calcula o dobro do valor fornecido
    :param n: valor que será calculado.
    :return: dobro do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n * 2
    return res


def metade(n = 0):
    """
    -> Calcula a metade do valor fornecido
    :param n: valor que será calculado.
    :return: metade do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n / 2
    return res


def moeda(n = 0):
    """
    -> Converte o valor fornecido para um valor monetário
    :param n: valor que será convertido.
    :return: valor alterado e com R$.
    Função criada por Guilherme Guimarães dos Santos
    """
    n = f'{n:,.2f}' # Deixa o valor com apenas duas casas decimais
    res = n.replace('.', ',') # Troca ponto por vírgula
    return f'R${res}'

