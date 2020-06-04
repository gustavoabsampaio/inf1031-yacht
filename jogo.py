#imports locais
from jogada import *
from dado import *
from jogador import *
from tabela import *

#imports de terceiros
import tkinter as tk

def numero_jogadores():
    n = int(input('Escolha o número de jogadores (1-6):'))
    return n

def cria_jogadores():
    n = numero_jogadores()
    i = 1
    while n>0:
        jogador = input("Insira o nome do jogador " + str(i) + ":")
        insere_jogador(jogador)
        i+=1
        n-=1
    return 

def cria_tabela():
    lista = get_jogadores()
    for i in lista:
        cria_coluna(lista[i])
    return




class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartMenu)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text="Start", command=lambda: master.switch_frame(Game)).pack()
        tk.Button(self, text="Quit", command=quit).pack()

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Game").pack()
        tk.Button(self, text="Main Menu", command=lambda: master.switch_frame(StartMenu)).pack()

app = App()
app.title("Yacht")
app.geometry("800x600")
app.mainloop()