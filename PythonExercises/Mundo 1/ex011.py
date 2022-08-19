L = float(input('Qual a largura, em metros, da parede que será pintada? '))
H = float(input('E a altura, também em metros, dessa mesma parede? '))
A = float(L * H)
Tinta = float(A / 2)
print('A parede possui dimensão {:.2f}x{:.2f}, totalizando uma área de {:.1f}m². \n'
      'Você precisará de {:.1f}L de tinta para pinta-la.'.format(L, H, A, Tinta))
