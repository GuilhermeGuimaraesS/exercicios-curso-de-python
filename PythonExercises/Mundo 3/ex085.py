par = []
impar = [] 
valores = []

for c in range(0, 7):
    num = int(input(f'Digite o {c+1}º número: '))
    if num % 2 == 0:
        par.append(num)
        par.sort()
    elif num % 2 == 1:
        impar.append(num)
        impar.sort()

valores.insert(0, par)
valores.insert(1, impar)

print('-='*50)
print(f'''Os números pares digitados foram: {par}
Os números ímpares digitados foram: {impar}''')
