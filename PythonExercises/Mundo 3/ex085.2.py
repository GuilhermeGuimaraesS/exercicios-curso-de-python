valores = [[], []]

for c in range(1, 8):
    num = int(input(f'Digite o {c}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
        valores[0].sort()
    elif num % 2 == 1:
        valores[1].append(num)
        valores[1].sort()

print( f"""Os números digitados foram {valores}. 
Os pares: {valores[0]}.
Os ímpares: {valores[1]}. """ )
