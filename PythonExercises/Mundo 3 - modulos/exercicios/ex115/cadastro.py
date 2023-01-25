# Cadastrar pessoas com nome e idade

    # - Nome; Criar uma função que leia apenas nomes. A função irá validar se foi digitado apenas strings

def vazio(entrada):
    while True:
        if entrada == '':
            print('ERRO! Digite um nome válido... ')
        else:
            break
    return entrada
    
def leiaNome(msg):
    valido = False
    name = ''
    while not valido:
        entrada = str(input(msg)).strip().upper()
        nome_sobrenome = vazio(entrada)
        nome_sobrenome = entrada.split() # Fatia a entrada, dividindo nome e sobrenome

        pontos_validos = 0
        for cont in range(0, len(nome_sobrenome)): # Verifica se todas as partes da entrada são letras
            if nome_sobrenome[cont].isalpha():
                pontos_validos += 1
        if pontos_validos == len(nome_sobrenome):
            valido = True
            name = entrada
        else:
            print('ERRO! Digite um nome válido... ')
    return name


cliente = leiaNome('Nome:  ')
print(cliente)


    # - Idade; Criar uma função que leia apenas números inteiros. A função irá validar se foi digitado apenas números


# Listar as pessoas cadastradas

