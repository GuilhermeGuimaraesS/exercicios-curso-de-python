# Cadastrar pessoas com nome e idade
from autenticador import NumeroForaDoIntervalo
from autenticador import  intervalo

# - Nome; Criar uma função que leia apenas nomes. A função irá validar se foi digitado apenas letras.
from autenticador import leiaNome

# - Idade; Criar uma função que leia apenas números inteiros. A função irá validar se foi digitado apenas números
from autenticador import leiaIdade
    
# Criar menu principal do sistema e fazer a coleta dos dados

def titulo(msg):
    print('-' * 50)
    print(msg.center(50))
    print('-' * 50)
    


escolha = 0
while escolha != 3:
    titulo('MENU PRINCIPAL')
    print('\033[0;33m1 -\033[m \033[0;34mVerificar pessoas cadastradas \033[m')
    print('\033[0;33m2 -\033[m \033[0;34mCadastrar nova pessoa \033[m')
    print('\033[0;33m3 -\033[m \033[0;34mSair do Sistema \033[m')
    print('-' * 50)
    while True:
        try:
            escolha = int(input('\033[0;33mOpção desejada: \033[m'))
            intervalo(escolha, 1, 4)
        except NumeroForaDoIntervalo:
            print('Opção inválida! Digite um número entre 1 e 3...')
        except:
            print('Opção inválida! Digite um número entre 1 e 3...')  
        else:
            break

    if escolha == 2:
        nome = leiaNome('Nome: ')
        idade = leiaIdade('Idade: ')
        print(f'Novo registro de {nome} adicionado. ')
    

# Listar as pessoas cadastradas
