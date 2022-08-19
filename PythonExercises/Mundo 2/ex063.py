# Sequência de Fibonacci

print('=-' * 20)
print('      SEQUÊNCIA DE FIBONACCI      ')
print('=-' * 20)

num = int(input('Quantos termos da sequência você mostrar? '))
cont = 1

print('{} primeiros termos da Sequência de Fibonacci: '.format(num))
T1 = 0
print(T1, end=' ')
T2 = 1
print(T2, end=' ')

while cont <= num:
    T3 = T1 + T2
    print(T3, end=' ')
    T1 = T2
    T2 = T3
    cont += 1
print('FIM')
