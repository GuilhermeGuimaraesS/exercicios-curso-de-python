# criar uma função chamada ficha, que vai receber nome e gols de um jogador no campeonato. Depois retorna a ficha desse jogador. A ficha será mostrada mesmo que um ou os dois parâmetros estejam vazios

def ficha(nome = '<desconhecido>', tot_gols = 0):
    print('-' * 20)
    print(f'O jogador {nome} fez {tot_gols} gol(s) no campeonato. ')


# programa principal

jogador = str(input('Nome do Jogador: ')).capitalize()
num = str(input('Número de Gols: '))

# Verifica se foi digitado um número ou não. Se sim, transforma em inteiro se não, a variável num recebe o valor 0.
if num.isnumeric():
    num = int(num)
else:
    num = 0

# Se a variável jogador estiver vazia, chama a função com o valor padrão para jogador
if jogador.strip() == '':
    ficha(tot_gols=num)
else:
    ficha(jogador, num)
