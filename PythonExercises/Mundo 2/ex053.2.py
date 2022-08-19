frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso da frase {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Essa frase É UM PALÍDROMO')
else:
    print('Essa frase NÃO É UM PALÍDROMO')
