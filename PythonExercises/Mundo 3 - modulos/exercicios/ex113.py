def leiaInt(msg):
    valido = False
    valor = 0
    while not valido:
        num = str(input(msg)).strip()
        if num.isnumeric():
            valido = True
            valor = int(num)
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
    return valor

num = leiaInt('Digite um número inteiro: ')
