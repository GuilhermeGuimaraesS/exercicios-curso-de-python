def aumentar(n, p):
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


def diminuir(n, p):
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


def dobro(n):
    """
    -> Calcula o dobro do valor fornecido
    :param n: valor que será calculado.
    :return: dobro do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n * 2
    return res


def metade(n):
    """
    -> Calcula a metade do valor fornecido
    :param n: valor que será calculado.
    :return: metade do valor fornecido.
    Função criada por Guilherme Guimarães dos Santos
    """
    res = n / 2
    return res
