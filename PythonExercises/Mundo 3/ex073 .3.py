from time import sleep

# Lista de Times do Brasileirão Série A 2021 de acordo com a sua posição. Dados do dia 29.07.2021
times = ('Palmeiras', 'Atlético-MG','Fortaleza','Bragantino','Athletico-PR','Flamengo','Ceará SC','Atletico-GO','Bahia','Corinthians','Fluminense','Santos','Juventude','Internacional','Cuiabá','Sport Recife','São Paulo','América-MG','Grêmio','Chapecoense')

print('-'*20)
print('DADOS BRASILEIRÃO SÉRIE A 2021 (DIA 29.07.2021)')
print('-'*20)
sleep(1)
print('=+'*25)

# 5 primeiros colocados 
print('Os cinco primeiros colocados são: ')   
for pos in range(0, 5):
    print(f'{pos+1}º colocado: {times[pos]}')


print('=+'*25)
sleep(3)

# 4 últimos colocados
print('Os quatro últimos colocados da tabela são: ')
for pos in range(16, 20):
    print(f'{pos+1}º colocado {times[pos]}')

print('=+'*25)
sleep(3)

# Times organizados em ordem alfabética
timesOrd = sorted(times)
print(f'Os times em ordem alfabética: ')
for pos in range (0, len(times)):
    print(f'{timesOrd[pos]}')

print('=+'*25)
sleep(3)

# Posição em que se encontra a Chapecoense
posChap = times.index('Chapecoense')
print(f'A Chapecoense está na {posChap+1}ª posição!')

print('=+'*25)
