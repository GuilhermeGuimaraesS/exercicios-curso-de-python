# Números pares entre 1 e 50

print("=-" * 15)
print(" Números pares entre 1 e 50 ")
print("=-" * 15)

# Primeira Resolução

for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
print('FIM')

# Segunda Resolução

for num in range(2, 51, 2):
    print(num, end=' ')
print('FIM')
