num = []

for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or  v > num[-1]:
        num.append(v)
        print('Valor adicionado ao fim da lista! ')
#    if c == 0:
#        num.append(v)
#    elif v > num[-1]:
#        num.append(v)
    else:
        pos = 0
        while pos < len(num):
            if v <= num[pos]:
                num.insert(pos, v)
                print(f'Valor adicionado a posição {pos} da lista! ')
                break
            pos += 1
print(f'Os números adicionados foram: {num}')

if c == 0 or  v > num[-1]:
    num.append(v)
