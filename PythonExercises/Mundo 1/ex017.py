from math import hypot
cO = float(input('Me diga o valor do Cateto Oposto: '))
cA = float(input('Agora, me diga do Cateto Adjacente: '))
print('Com o Cateto Oposto medindo {}cm e o Cateto Adjacente {}cm, a Hipotenusa mede {}cm.'.format(cO, cA, hypot(cO, cA)))
