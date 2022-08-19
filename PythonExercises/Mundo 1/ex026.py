frase = str(input('Digite uma frase: ')).upper().strip()
qntdA = frase.count('A')
qntdB = frase.find('A')+1
qntdC = frase.rfind('A')+1
print('A letra A aparece {} vezes na frase.'.format(qntdA))
print('A letra A aparece pela primeira vez na posição {}.'.format(qntdB))
print('A última letra A apareceu na posição {}.'.format(qntdC))
