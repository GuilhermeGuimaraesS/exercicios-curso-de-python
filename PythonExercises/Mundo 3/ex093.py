ficha = dict()
gols_partida = list()

ficha['Nome'] = str(input('Nome do Jogador: ')).capitalize()
tot_part = int(input(f'Quantas partidas {ficha["Nome"]} jogou? '))

tot_gols = 0
for c in range(0, tot_part):
    gols_partida.append(int(input(f'Gols feitos no Jogo {c+1}:  ')))
ficha['Gols'] = gols_partida[:]
ficha['Gols no campeonato'] = sum(gols_partida)

print('-=' * 25)
for k, v in ficha.items():
    if k != 'Gols':
        print(f'O campo {k} tem valor {v}. ')
print('-=' * 25)

print(f'O jogador {ficha["Nome"]} jogou {tot_part} partidas. ')

for c in range(0, len(gols_partida)):
    print(f'    => No jogo {c+1}, fez {gols_partida[c]} gols. ')
print(f'Foi um total de {ficha["Gols no campeonato"]} gols. ')
