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
        tk.Button(self, text="Start", command=lambda: master.switch_frame(SetupGame)).pack()
        tk.Button(self, text="Quit", command=quit).pack()

class SetupGame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        output_label = tk.Label(self,fg = "black", text = "Jogadores")
        output_label.pack()
        self.output = tk.Label(self, fg = "black", bg = "white", height = 10, width = 15)
        self.output.pack()
        name_label = tk.Label(self, text="Name")
        name_label.pack()
        nome_var = tk.StringVar(self)
        
        def add_player():
            nome_get = nome_var.get()
            insert_status = insere_jogador(nome_get)
            if insert_status:
                self.get_output()
                nome.delete(0, len(nome_get))

        nome = tk.Entry(self, textvariable = nome_var)
        nome.pack()
        add_player_button = tk.Button(self, text="Add Player", command=add_player)
        add_player_button.pack()
        start_button = tk.Button(self, text="Start", command=lambda: master.switch_frame(Game))
        start_button.pack()
        menu_button = tk.Button(self, text="Main Menu", command=lambda: master.switch_frame(StartMenu))
        menu_button.pack()

    def get_output(self):
        jogadores = get_jogadores()
        print(jogadores)
        self.output["text"] = self.output["text"] + jogadores[len(jogadores)-1] + '\n'

class Game(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Game").pack()
        tk.Button(self, text="Main Menu", command=lambda: master.switch_frame(StartMenu)).pack()
        tk.Label(self, text="Table").pack()
        for i in range(linhas):
            for j in range(colunas):
                self.e = Entry(root,widht = 15, fg = 'black')
                self.e.grid(row = i, column =j)
                self.e.insert(END, lst[i][j])
                
# lst = get              



app = App()
app.title("Yacht")
app.geometry("800x600")
app.mainloop()