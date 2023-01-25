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
