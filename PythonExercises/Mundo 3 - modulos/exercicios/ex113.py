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


def leiaFloat(msg):
    valido = False
    valor = 0
    while not valido:
        num = str(input(msg)).replace(',','.').strip()
        if num.isalpha() or num == '':
            print('\033[0;31mERRO! Digite um número real válido. \033[m')
        else:
            valido = True
            valor = float(num)
    return valor

