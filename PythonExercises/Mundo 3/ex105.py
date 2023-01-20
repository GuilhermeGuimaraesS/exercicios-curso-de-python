# Programa que recebe várias notas e retorna um dicionário com total de notas, maior e menor nota, média da turma e a situação (opcional). Adicionar docstrings da função

def notas(*num, situ=False):
    # media >= 7, situ = 'BOA', 6 <= media < 7, situ = 'RAZOÁVEL', media < 6, situ = 'RUIM'
    """
    -> Função para analisar as notas e situações de vários alunos.
    :param num: recebe uma ou mais notas dos alunos.
    :param situ: parâmetro opcional; indica se é para adicionar ou não a situação.
    :return: dicionário com várias informações da turma.
    Função criada por Guilherme Guimarães dos Santos
    """
    cont = tot_notas = soma = 0
    maior_nota = menor_nota = 0
    caderneta = dict()

    for cont in range(0, len(num)):
        soma += num[cont]
        tot_notas += 1

        if cont == 0:
            maior_nota = menor_nota = num[cont]
        else:
            if num[cont] > maior_nota:
                maior_nota = num[cont]
            elif num[cont] < menor_nota:
                menor_nota = num[cont]
    
    caderneta['Total'] = tot_notas 
    caderneta['Média'] = (soma / tot_notas)
    caderneta['Maior'] = maior_nota
    caderneta['Menor'] = menor_nota

    if situ:
        if caderneta['Média'] >= 7:
            caderneta['Situação'] = 'BOA!'
        elif caderneta['Média'] < 6:
            caderneta['Situação'] = 'RUIM!'
        else:
            caderneta['Situação'] = 'RAZOÁVEL!'

        return caderneta
    else:
        return caderneta

# programa principal
resp = notas(5.4, 7.8, 6, 6.8, situ=True)
help(notas)
