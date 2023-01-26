def leiaInt(msg=''):
    """
    -> Função que faz a leitura apenas de valores inteiros. Caso não seja um valor inteiro, retorna uma mensagem de erro e tentar fazer a leitura novamente
    :param msg: Recebe uma mensagem para ser exibida para o usuário
    :return: valor inteiro
    """
    while True:
        try:
            num = int(input(msg))
        except (KeyboardInterrupt):
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário. \033[m')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido \033[m')
            continue # volta para o inicio do loop
        else:
            break
    return num


def leiaFloat(msg=''):
    """
    -> Função que faz a leitura apenas de valores reais. Caso não seja um valor real, retorna uma mensagem de erro e tentar fazer a leitura novamente
    :param msg: Recebe uma mensagem para ser exibida para o usuário
    :return: valor real
    """
    while True:
        try:
            num = float(input(msg))
        except (ValueError, KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número \033[m')
            num = 0
            break
        except:
            print('\033[0;31mERRO! Digite um valor real válido \033[m')
        else:
            break
    return num
