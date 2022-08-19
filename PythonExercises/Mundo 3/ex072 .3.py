contagem = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')

pos = ''
resp = 'Ss'
while resp in 'Ss': 
    while True:
        pos = int(input('Digite um número entre 0 e 20: '))
        if pos in range(0, 21):
            break
        print('Número inválido! Tente novamente. ', end='')
    print(f'Você digitou o número {contagem[pos]}!')
    while True:  
        resp = str(input('Você quer continuar? [S/N]: '))
        if resp in 'SsNn':
            break
        elif resp not in 'Ss':
            print('Opção inválida! Tente novamente. ', end='')


#    else:
#        while pos not in range(0, 21):
#            pos = int(input('Número inválido! Tente mais uma vez. Digite um número entre 0 e 20: '))
#        break
