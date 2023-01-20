# Criar um mini sistema que utilize o interactive help do Python. O comando vai ser digitado e o manual daquele comando vai ser exibido para o usuário. Quando ele digitar 'FIM', o programa se encerrará. (Usar cores)


def enunciado(msg):
    msg = msg.strip()
    tot_caract = (len(msg) + 8)
    print('=' * tot_caract)
    print(msg.center(tot_caract))
    print('=' * tot_caract)

def PyHelp(comando):
    from time import sleep

    help(comando)
    sleep(0.5)


def enunciadoDois(msg, n):
    from time import sleep

    sleep(1)
    msg = msg.strip()
    n = n.strip()
    n = (f" '{n}' ")
    tot_caract = (len(msg) + len(n) + 8)
    print('=' * tot_caract)
    print((msg + n).center(tot_caract))
    print('=' * tot_caract)
    sleep(1)


# programa principal

enunciado('SISTEMA DE AJUDA PyHelp')
nome = str(input('Nome da Função ou Biblioteca: '))
enunciadoDois('Acessando o manual do comando', nome)
help(nome)
