from tkinter import *
from random import randint

num = randint(0, 100)
if num % 2 == 0:
    print(f"O número {num} é Par. ")
elif num % 2 == 1:
    print(f'O número {num} é Ímpar. ')


janela = Tk() # Cria a janela
janela.title("Par ou Ímpar")

texto_orientacao = Label(janela, text="Clique no botão para sortear um número")
texto_orientacao.grid(column=0, row=0)

janela.mainloop() # Mantém a janela criada, aberta