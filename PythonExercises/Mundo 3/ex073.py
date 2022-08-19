# Times da Serie A do Brasileirão (Temporada 2020)
tabela = ('Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Botafogo',
          'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Flamengo',
          'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional',
          'Palmeiras', 'Santos', 'São Paulo', 'Sport', 'Vasco')
# Cabeçalho do Programa (Função dele)
print('=' * 30)
print(f'{"DADOS BRASILEIRÃO 2020":^30}')
print('=' * 30)
print('-' * 30)
# Lista de Times
print('TABELA DE CLASSIFICAÇÃO: ')
for times in tabela:
    print(times)
print('-' * 30)
# 5 Primeiros colocados
for pos in range(0, 5):
    print(f'{pos + 1}º Colocado: {tabela[pos]}')
print('-' * 30)
# 4 Últimos colocados
for pos in range(16, 20):
    print(f'{pos + 1}º Colocado: {tabela[pos]}')
print('-' * 30)
# Todos os Times organizados em ordem alfabética
print('TIMES EM ORDEM ALFABÉTICA: ')
for pos in range(0, 20):
    print(f'{sorted(tabela)[pos]}')
print('-' * 30)
# Posição do Coritiba
posCoritiba = tabela.index('Coritiba')
print(f'O Coritiba é o {posCoritiba + 1}º colocado.')
print('-' * 30)
