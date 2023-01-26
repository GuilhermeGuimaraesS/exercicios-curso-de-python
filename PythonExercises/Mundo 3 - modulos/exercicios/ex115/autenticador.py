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


# - Nome; Criar uma função que leia apenas nomes. A função irá validar se foi digitado apenas letras.
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


# - Idade; Criar uma função que leia apenas números inteiros. A função irá validar se foi digitado apenas números
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
    

# Criar menu principal do sistema e fazer a coleta dos dados
def menu(lista):
    """
    -> Função que recebe uma lista com títulos e retorna um menu personalizado com as opções e os números que correspondem àquela opção.
    :lista: lista com as funcionalidades
    """
    titulo('MENU PRINCIPAL') 
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')  
        c += 1
    print('-' * 50)
    

def opçao():
    """
    -> Função que faz a leitura e validação da escolha. Verifica se foi digitado um valor inteiro entre 1 e 3
    :return: opção digitada pelo usuário
    """
    while True:
        try:
            escolha = int(input('\033[0;33mOpção desejada: \033[m'))
            intervalo(escolha, 1, 4)
        except NumeroForaDoIntervalo:
            print('\033[0;31mOpção inválida! Digite um número entre 1 e 3...\033[m')
        except:
            print('\033[0;31mOpção inválida! Digite um número entre 1 e 3...\033[m')  
        else:
            break
    return escolha

        
def operaçao(num):
    from time import sleep
    # Bloco que lista as pessoas cadastradas
    if num == 1:
        sleep(1)
        titulo('PESSOAS CADASTRADAS')
        with open("C://Users/guilh/Documents/GitHub/exercicios-curso-de-python/PythonExercises/Mundo 3 - modulos/exercicios/ex115/Cadastro.txt", "r") as arquivo:
            ficha = arquivo.read()
        print(ficha)
        sleep(1)
        
    # Bloco que realiza um novo cadastro
    if num == 2:
        sleep(1)
        titulo('NOVO CADASTRO')
        nome = leiaNome('Nome: ')
        idade = leiaIdade('Idade: ')
        # Guarda as informações digitadas em um arquivo .txt; Caso não exista, será criado na hora
        with open("C://Users/guilh/Documents/GitHub/exercicios-curso-de-python/PythonExercises/Mundo 3 - modulos/exercicios/ex115/Cadastro.txt", "a") as arquivo: # Arquivo == variável que recebe o .txt
            arquivo.write(f'\n{nome.ljust(40)} {idade} anos')    
        print(f'Novo registro de {nome} adicionado. ')
        sleep(1)
    


