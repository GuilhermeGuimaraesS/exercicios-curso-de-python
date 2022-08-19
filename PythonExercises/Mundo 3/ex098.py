from time import sleep

def contagem(a, b, c):
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c} ')
    sleep(2.5)
    if a > b:
        if c < 0:
            c *= (-1)
        elif c == 0:
            c = 1
        while a >= b:
            print(f'{a} ', end='')
            sleep(0.5)
            a -= c 
    elif a < b:
        if c < 0:
            c *= (-1)
        elif c == 0:
            c = 1
        while a <= b:
            print(f'{a} ', end='')
            sleep(0.5)
            a += c
    print('FIM!')
    sleep(1)
    
contagem(1, 10, 1)
contagem(10, 0, 2)

print('-=' * 30)
print('Agora é sua vez! Digite os valores para uma contagem personaizada. ')
inicio = int(input('Primeiro valor da contagem: '))
final = int(input('Último valor da contagem: '))
step = int(input('Passo da contagem: '))
contagem(inicio, final, step)
