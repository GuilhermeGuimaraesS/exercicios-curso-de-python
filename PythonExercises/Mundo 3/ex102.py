# criar uma função fatorial, ela vai receber o número e um parâmetro lógico que, se for verdadeiro vai mostrar o cálculo do fatorial e se for falso, só mostra o resultado

def fatorial(num, show=False):
    '''
        -> Calcula o fatorial de um número
        :param num: O número que vai ser calculado
        :param show: (opcional) Mostrar ou não o processo de cálculo do fatorial. True mostra e False não mostra (padrão)
        :return: O valor fatorial de um número
        Função criada por Guilherme Guimarães dos Santos
    '''
    print('-' * 30)
    cont = num
    fat = 1
    if show == False:
        while cont >= 1:
            fat *= cont
            cont -= 1
        return fat
    else:
        while cont >= 1:
            if cont > 1:
                print(f'{cont} x ', end='')
            else:
                print(f'{cont} = ', end='')
            fat *= cont
            cont -= 1
        return fat

# Programa principal
numb = int(input('Digite um número: '))
print(fatorial(numb))
