# Tabuada 2.0

num = int(input("Digite um número para vizualizar a sua tabuada: "))

print("=-" * 10)
print("    TABUADA   ")
print("=-" * 10)

print("-" * 15)
for cont in range(1, 11):
    print(" {:2} x {:2} = {:2} ".format(cont, num, (cont * num)))
print("-" * 15)
