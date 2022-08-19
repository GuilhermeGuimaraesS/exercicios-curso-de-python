ficha = dict()
gols_partida = list()
aproveitamento_jogadores = list()

while True:
    ficha.clear()
    ficha['Nome'] = str(input('Nome do Jogador: ')).capitalize()
    tot_gols = 0
    tot_part = int(input(f'Quantas partidas {ficha["Nome"]} jogou? '))
    
    for c in range(0, tot_part):
        gols_partida.append(int(input(f'Gols feitos no Jogo {c+1}:  ')))
        ficha['Gols'] = gols_partida[:]
    ficha['Gols no campeonato'] = sum(gols_partida)
    gols_partida.clear()
    aproveitamento_jogadores.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Escreve apenas S ou N. ')
    if resp in 'Nn':
        break
print('-=' * 45)

print(f'{"Cod":<5}', end='')
for i in ficha.keys():
    print(f'{i:<25}', end='')
print()
print('-' * 90)
for k, v in enumerate(aproveitamento_jogadores):
    print(f'{k:<5}', end='') # Mostra o índice do jogador. Ex: 0, 1, ... , etc
    for dado in v.values():
        print(f'{str(dado):<25}', end='')
    print()
print('-' * 90)

while True:
    busca = int(input('Quer ver o aproveitamento de qual jogador? (999 encerra) '))
    if busca == 999:
        break
    if busca >= len(aproveitamento_jogadores):
        print(f'ERRO! Não existe jogador com esse código {busca}! ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {aproveitamento_jogadores[busca]["Nome"]} --')
        for i, g in enumerate(aproveitamento_jogadores[busca]["Gols"]):
            print(f'    No jogo {i+1} fez {g} gols. ')
    print('-' * 90)
print(f'{" === VOLTE SEMPRE === ":^90}')
