col1 = []
col2 = []
col3 = []

for c1 in range(0, 3):
    num1 = int(input(f'Digite um valor para [0, {c1}]: '))
    if c1 == 0:
        col1.insert(0, num1)
    elif c1 == 1:
        col2.insert(0, num1)
    elif c1 == 2:
        col3.insert(0, num1)
for c2 in range(0, 3):
    num2 = int(input(f'Digite um valor para [1, {c2}]: '))
    if c2 == 0:
        col1.insert(1, num2)
    elif c2 == 1:
        col2.insert(1, num2)
    elif c2 == 2:
        col3.insert(1, num2)
for c3 in range(0, 3):
    num3 = int(input(f'Digite um valor para [2, {c3}]: '))
    if c3 == 0:
        col1.insert(2, num3)
    elif c3 == 1:
        col2.insert(2, num3)
    elif c3 == 2:
        col3.insert(2, num3)

print('-='*30)  
for pos in range(0, 3):
    print(f'[  {col1[pos]}  ][  {col2[pos]}  ][  {col3[pos]}  ]')
