name = str(input('Digite o nome do funcionário: '))
slro = float(input('Agora, me diga qual o salário desse funcionário: '))
if slro > 1250.00:
    aumento1 = slro + (slro * 10 / 100)
    print('Após o aumento, o salário de {} passará a ser {:.2f}.'.format(name, aumento1))
if slro <= 1250.00:
    aumento2 = slro + (slro * 15 / 100)
    print('Após o aumento, o saláio de {} passará a ser {:.2f}.'.format(name, aumento2))
