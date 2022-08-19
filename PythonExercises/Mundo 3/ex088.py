from random import randint
from time import sleep

jogos = []
lista_temp = []

print('-' * 30)
print('     JOGA NA MEGA SENA     ')
print('-' * 30)

totJogos = int(input('Quantos jogos você quer sortear? '))
print('-=' * 5, f' SORTEANDO {totJogos} JOGOS ', '=-' * 5)

c = 1 # variável contadora
while c <= totJogos:
    cont = 0 
    while True:
        num = randint(0, 60)
        if num not in lista_temp:
            lista_temp.append(num)
            cont += 1
        if cont == 6:
            break   
    lista_temp.sort()
    jogos.append(lista_temp[:])
    lista_temp.clear()
    c += 1

for i in range(0, totJogos):
    sleep(1)
    print(f'JOGO {i+1}: {jogos[i]} ')
sleep(1)
print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
    