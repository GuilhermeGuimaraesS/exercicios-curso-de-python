# Cadastrar pessoas com nome e idade
from autenticador import NumeroForaDoIntervalo
from autenticador import  intervalo
from time import sleep

# - Nome; Criar uma função que leia apenas nomes. A função irá validar se foi digitado apenas letras.
from autenticador import leiaNome

# - Idade; Criar uma função que leia apenas números inteiros. A função irá validar se foi digitado apenas números
from autenticador import leiaIdade
    
# Criar menu principal do sistema e fazer a coleta dos dados
from autenticador import titulo
from autenticador import menu
    
escolha = 0
while escolha != 3:
    sleep(1)
    opcs = ['Verificar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
    menu(opcs)
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
        
    # Bloco que lista as pessoas cadastradas
    if escolha == 1:
        sleep(1)
        titulo('PESSOAS CADASTRADAS')
        with open("C://Users/guilh/Documents/GitHub/exercicios-curso-de-python/PythonExercises/Mundo 3 - modulos/exercicios/ex115/Cadastro.txt", "r") as arquivo:
            ficha = arquivo.read()
        print(ficha)
        sleep(1)
        
    # Bloco que realiza um novo cadastro
    if escolha == 2:
        sleep(1)
        titulo('NOVO CADASTRO')
        nome = leiaNome('Nome: ')
        idade = leiaIdade('Idade: ')
        # Guarda as informações digitadas em um arquivo .txt; Caso não exista, será criado na hora
        with open("C://Users/guilh/Documents/GitHub/exercicios-curso-de-python/PythonExercises/Mundo 3 - modulos/exercicios/ex115/Cadastro.txt", "a") as arquivo: # Arquivo == variável que recebe o .txt
            arquivo.write(f'\n{nome.ljust(40)} {idade} anos')    
        print(f'Novo registro de {nome} adicionado. ')
        sleep(1)
    
    # Bloco que exibe uma mensagem de despedida após o usuário sair 
    if escolha == 3:
        sleep(1)
        titulo('SAINDO DO SISTEMA... ATÉ MAIS!')
        sleep(1)
