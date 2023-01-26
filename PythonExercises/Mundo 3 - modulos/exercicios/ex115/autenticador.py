def vazio(entr, msg):
    """
    -> Função para verificar se a variável está vazia
    :param entr: variável que será verficada
    :param msg: mensagem que será exibida na tela
    :return: variável não vazia
    Função criada por Guilherme Guimarães dos Santos
    """
    while True:
        if entr == '':
            print('\033[0;31mERRO! Digite um nome válido... \033[m')
            entr = str(input(msg)).strip().upper()
        else:
            n = entr
            break
    return n

    
def leiaNome(msg):
    """
    -> Faz a leitura apenas de nomes.
    :param msg: mensagem que será exibida na tela
    :return: nome completo do(a) cadastrado(a)
    Função criada por Guilherme Guimarães dos Santos
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().upper()
        nome_sobrenome = vazio(entrada, msg) 
        nome_sobrenome_f = nome_sobrenome.split() # Fatia a entrada, dividindo nome e sobrenome

        pontos_validos = 0
        for cont in range(0, len(nome_sobrenome_f)): # Verifica se todas as partes da entrada são letras
            if nome_sobrenome_f[cont].isalpha():
                pontos_validos += 1
        if pontos_validos == len(nome_sobrenome_f):
            valido = True
            name_full = nome_sobrenome
        else:
            print('\033[0;31mERRO! Digite um nome válido... \033[m')
    return name_full


def leiaIdade(msg):
    """
    -> Função para ler a idade do(a) cadastrado(a). Lê apenas valores inteiros
    :param msg: mensagem que será exibida na tela
    :return: idade do cadastrado(a)
    Função criada por Guilherme Guimarães dos Santos
    """
    valido = False
    while not valido:
        try:
            age = int(input(msg))
        except:
            print('\033[0;31mERRO! Digite uma idade válida... \033[m')
        else:
            valido = True
    return age


def titulo(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)


class NumeroForaDoIntervalo(Exception): # Gera classe de erro de intervalo
    pass

def intervalo(n, i, f):
    """
    -> Função para verificar se a variável analisada está no intervalo desejado
    :param n: variável que será analisada.
    :param i: início do intervalo.
    :param f: fim do intervalo.
    :return: variável já analisada
    Função criada por Guilherme Guimarães dos Santos
    """
    if n not in range(i, f):
        raise NumeroForaDoIntervalo
    else:
        return n 
    
    
def menu(lista):
    titulo('MENU PRINCIPAL') 
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')  
        c += 1
    print('-' * 50)

