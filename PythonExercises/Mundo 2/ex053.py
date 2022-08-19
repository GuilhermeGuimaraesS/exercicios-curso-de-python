print('=' * 20)
print('ANALISADOR DE FRASES')
print('=' * 20)

frase = input('Digite uma frase: ').strip().upper()
print('OBS: PALÍDROMO = FRASE QUE QUANDO ESCRITA DE TRAŚ PARA FRENTE É IGUAL QUANDO SE ESCREVE NORMALMENTE')
frase1 = frase.replace(' ', '') # Remove os espaços dentro da frase
frase2 = frase1[::-1] # Coloca a frase de trás para frente

print('O inverso da frase {} é {}'.format(frase1, frase2))
if frase1 == frase2:
    print('Essa frase É UM PALÍDROMO!')
else:
    print('Essa frase NÃO É UM PALÍDROMO!')
