from random import randint

def sorteio():
    global lst
    lst = []
    cont = 0
    while True:
        lst.append(randint(0, 99))
        cont += 1
        if cont == 5:
            break
    print(f'Os números sorteados foram: {lst}')

def somaPar():
    lst_pares = []
    cont = 0
    soma_par = 0
    for cont, num in enumerate(lst):
        if num % 2 == 0:
            lst_pares.append(num)
            soma_par += num

    print(f'Dentre esses, os pares são: {lst_pares}. Somando eles, temos {soma_par}')

sorteio()
somaPar()
