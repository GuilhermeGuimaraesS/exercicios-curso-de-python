from random import randint
from time import sleep
from operator import itemgetter

tbl_dado = dict()
ranking = list()

for cont in range(1 , 5):
    tbl_dado[f'jogador{cont}'] = randint(1, 6)
print('VALORES SORTEADOS:')
for k, v in tbl_dado.items():
    sleep(1)
    print(f'    O {k} tirou {v} no dado. ')
sleep(1)

ranking = sorted(tbl_dado.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print(' == RANKING DOS JOGADORES == ')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}. ')
    sleep(1)


#for k in sorted(tbl_dado, key = tbl_dado.get, reverse=True):
#    sleep(1)
#    print(  f' O {k} tirou {tbl_dado[k]} no dado. ')
#sleep(1)
