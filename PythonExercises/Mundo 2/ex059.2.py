from time import sleep

esc = 0
while esc != 5:
    num1 =  int(input('Primeiro valor: '))
    num2 = int(input('Segundo valor: '))

    print('=-' * 15)
    esc = int(input('''    MENU DE FUNÇÔES
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ESCOLHA: '''))
    print('=-' * 15)

    if esc == 1:
        s = num1 + num2
        print('A soma entre {} e {} é igual a {}'.format(num1, num2, s))
    elif esc == 2:
        m = num1 * num2
        print('A multiplicação entre {} e {} é igual a {}'.format(num1, num2, m))
    elif esc == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é maior que {}'.format(num2, num1))
    elif esc == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif esc == 5:
        print('Encerrando o Programa...')
    else:
        print('Opção Inválida... Tente Novamente!')
    sleep(2)
print('ProgramaEncerrado. Volte Sempre!')
