name = str(input('Qual é o nome do(a) aluno(a)? ')).strip().title()
n1 = float(input('Qual foi a primeira nota desse(a) aluno(a)? '))
n2 = float(input('E qual foi a segunda nota desse(a) aluno(a)? '))
name1 = name.split()
m = (n1 + n2) / 2
if m < 5.0:
    print('Como a média de {}, foi {:.1f}, ele(a) foi Reprovado(a)!'.format(name1[0], m))
if 5.0 <= m <= 6.9:
    print('Como a média de {}, foi {:.1f}, ele(a) terá que fazer Recuperação!'.format(name1[0], m))
elif m >= 7.0:
    print('Como a média de {}, foi {:.1f}, ele(a) foi Aprovado(a)!'.format(name1[0], m))
