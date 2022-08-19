number = int(input('Digite um número: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number //1000 %10
print('Observando o número {} \n Unidade: {} \n Centena: {} \n Dezena: {} \n Milhar: {}'
      .format(number, u, d, c, m))
