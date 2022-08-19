# Inicialização de variaveis
num = list()
resp = 'Ss'

# Recebe um valor inteiro, adiciona em uma  lista e pergunta se o usuário deseja continuar
v = int(input('Digite um número: '))
num.append(v)
resp = str(input('Quer continuar [S/N]? '))

# Repete as mesmas tarefas do bloco anterior, mas antes de adicionar o valor recebido verifica se já existe esse valor na lista, se  sim, exibe um aviso, senão, adiciona
while resp in 'Ss':
    v = int(input('Digite um número: '))
    if v in num:
        print('Ops! Número já adicionado, tente novamente. ')
    else:
        num.append(v)
    resp = str(input('Quer continuar [S/N]? '))
    
# Organiza a lista em ordem crescente e exibe na tela
num.sort()
print('-=' * 30)
print(f'Você digitou os seguintes valores:  {num}')
