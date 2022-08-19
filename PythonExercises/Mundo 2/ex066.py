num = soma = cont = 0  # Variáveis
while True:
    num = int(input('Digite um número [999 para Finalizar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números, e a SOMA entre eles é igual a {soma}')
