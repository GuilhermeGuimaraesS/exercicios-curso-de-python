# Cadastrar pessoas com nome e idade
from time import sleep
from autenticador import menu, opçao, titulo, operaçao


while True:
    sleep(1)
    opcs = ['Verificar pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema']
    menu(opcs)
    escolha = opçao()
    if escolha in range(1, 3):
        operaçao(escolha)
    # Bloco que exibe uma mensagem de despedida após o usuário sair 
    if escolha == 3:
        sleep(1)
        titulo('SAINDO DO SISTEMA... ATÉ MAIS!')
        sleep(1)
        break
