def fatorial(n):
    f = 1
    for cont in range(1, n+1):
        f *= cont
    return f


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}. ')