#  criar uma função leiaint() que funcione semelhante a função input(), só que aceitando apenas valores núméricos 

def leiaInt(texto, valor):
    verif = False
    while verif == False:
        verif = valor.isdigit()
        if verif == True:
            break
        elif verif == False:
            print('ERRO! Digite um número inteiro válido.')
    return valor



# programa principal

num = leiaInt('Digite um número: ')
print(num)
