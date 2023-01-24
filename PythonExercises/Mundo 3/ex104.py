#  criar uma função leiaint() que funcione semelhante a função input(), só que aceitando apenas valores núméricos 

def leiaInt(msg):
    ok = False # Variável que indica se foi digitado um número ou não
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True 
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m ')
        if ok:
            break
    return valor

# programa principal

num = leiaInt('Digite um número: ')
print(f'Você digitou o número:  {num}. ')
    