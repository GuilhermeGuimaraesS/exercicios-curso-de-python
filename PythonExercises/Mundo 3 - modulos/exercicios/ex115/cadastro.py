# Cadastrar pessoas com nome e idade

    # - Nome; Criar uma função que leia apenas nomes. A função irá validar se foi digitado apenas strings

def vazio(entr, msg):
    while True:
        if entr == '':
            print('\033[0;31mERRO! Digite um nome válido... \033[m')
            entr = str(input(msg)).strip().upper()
        else:
            n = entr
            break
    return n

    
def leiaNome(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().upper()
        nome_sobrenome = vazio(entrada, 'Nome ') 
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
    age = 0
    try:
        age = int(input(msg))
    except:
        print('Digite um número')



cliente = leiaNome('Nome:  ')
print(cliente)


    # - Idade; Criar uma função que leia apenas números inteiros. A função irá validar se foi digitado apenas números


# Listar as pessoas cadastradas

