from math import sin, cos, tan, radians
ângulo = float(input('Digite um ângulo que você desejar: '))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(' O SENO do ângulo {} é {:.2f}. \n O COSSENO do ângulo {} é {:.2f}. \n A TANGENTE do ângulo {} é {:.2f}.'
      .format(ângulo, seno, ângulo, cosseno, ângulo, tangente))
