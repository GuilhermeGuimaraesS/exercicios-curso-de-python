def escreva(a, b):
    print('-' * b )
    print(a.center(b))
    print('-' * b)

msg = str(input('Digite o texto que você quer mostrar na tela: '))
tot_caracter = len(msg) + 2
escreva(msg, tot_caracter)
    