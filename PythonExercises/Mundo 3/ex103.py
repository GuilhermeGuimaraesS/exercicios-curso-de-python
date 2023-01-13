# criar uma função chamada ficha, que vai receber nome e gols de um jogador no campeonato. Depois retorna a ficha desse jogador. A ficha será mostrada mesmo que um ou os dois parâmetros estejam vazios

def ficha(nome, tot_gols):
    if (nome == ''):
        nome = '<desconhecido>'
    if (tot_gols == ''):
        tot_gols = '0'
    print('-' * 20)
    print(f'O jogador {nome} fez {tot_gols} gol(s) no campeonato. ')


# program principal

jogador = str(input('Nome do Jogador: ')).capitalize()
num = str(input('Número de Gols: '))
ficha(jogador, num)
