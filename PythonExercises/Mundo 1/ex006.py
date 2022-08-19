n = int(input('Digite um número qualquer: '))
d = n*2
t = n*3
rq = float(pow(n, (1/2)))
print(' Após fazer alguns cálculos, verificou-se que o dobro do número {}, é {}. \n O seu triplo é {}.'
      ' \n E a sua raiz quadrada {:.2f}.'.format(n, d, t, rq))
