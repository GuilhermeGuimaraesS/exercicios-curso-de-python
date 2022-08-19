R = float(input('Quanto você tem em reais? R$'))
D = float(R / 4.06)
E = float(R / 4.53)
print('Com R${:.2f} você pode comprar US${:.2f} e {:.2f} €.'.format(R, D, E))
