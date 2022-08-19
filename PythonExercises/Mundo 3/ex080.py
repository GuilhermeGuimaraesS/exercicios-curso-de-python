num = list()

for c in range(0, 5):
    v = int(input('Digite um valor: '))
    if c == 0 or v > num[-1]:
        num.append(v)
        print('Valor adicionado ao fim da lista! ')
    else:
        pos = 0
        while pos < len(num):
            if v <= num[pos]:
                num.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista!')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {num}. ')
