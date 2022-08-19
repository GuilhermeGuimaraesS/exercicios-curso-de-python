from time import sleep


def maior(* num):
    tam = len(num)
    if tam == 0:
        num = 0
    print('Os números digitados foram: ')
    sleep(0.5)
    maior_num = 0
    cont = 0
    if tam > 0:
        for cont in range(0, len(num)):
            if cont == 0:
                maior_num == num[cont]
            else:
                if num[cont] > maior_num:
                    maior_num = num[cont]
            print(num[cont], end=' ')
            sleep(0.5)
    else:
        print(f'{num}', end=' ')
    print(f'Foram digitados {tam} valores ao todo. ')
    print(f'O maior valor dentre esses é {maior_num}. ')
    print('-=' * 20)
    sleep(0.5)


maior(4, 9, 0, 3, 6, 5)
maior(4, 7, 0)
maior(2, 4, 5, 1, 3, 9)
maior()
