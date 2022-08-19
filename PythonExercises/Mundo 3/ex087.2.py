matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s_par = s_col3 = max = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('=-' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print( f'[{matriz[l][c]:^5}] ' , end='')
        if matriz[l][c] % 2 == 0:
            s_par += matriz[l][c]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é: {s_par}. ')

for l in range(0, 3):
    s_col3 += matriz[l][2]
print(f'A soma dos valores  da terceira coluna é: {s_col3}. ')

for c in range(0, 3):
    if c == 0:
        max = matriz[1][c]
    elif matriz[2][c] > max:
        max = matriz[1][c]
print(f'O maior valor na segunda coluna é: {max}. ')
