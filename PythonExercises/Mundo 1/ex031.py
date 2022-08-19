import emoji
tam = float(input('Qual a distância até o destino desejado? '))
if tam <= 200:
    total1 = tam * 0.50
    print('A viagem custará R${:.2f}!'.format(total1))
else:
    total2 = tam * 0.45
    print('A viagem custará R${:.2f}!'.format(total2))
print(emoji.emojize("Tenha uma boa viagem :blush:!", use_aliases=True))
