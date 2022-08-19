palavras = ('programar', 'python', 'desenvolvedor','programador','javascript','fullstack','pentest')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')
