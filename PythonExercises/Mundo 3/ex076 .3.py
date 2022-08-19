produtos = ('Mouse', 45.98,'Headset', 74.57,'Monitor Full HD', 275.85, 'Cadeira Gamer', 875.98, 'Mesa de Escritório', 459.95, 'MousePAD Gamer', 98.54, 'SSD Sata III 480GB', 350.58, 'Webcam', 349.73)
print('=' * 40)
print(f"{'LISTA DE PREÇOS':^40}")
print('=' * 40)
for c in range(0, len(produtos), 2):
#    print(f"{produtos[c].ljust(30, '.')} R$ {produtos[c+1]}")
    print(f'{produtos[c]:.<30} R$ {produtos[c+1]:>.2f}')

