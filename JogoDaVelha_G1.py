import tkinter
from tkinter import messagebox
import random

class Placar:
    """A classe Placar contém dois atributos, sendo um para registrar a quantidade de vitórias do jogador X
       e outro para registrar a quantidade de vitórias do jogador O."""
    def __init__(self):
        self.vitorias_x = 0
        self.vitorias_o = 0

    def reg_vitoria_x(self):
        """Acrescenta uma vitória ao registro de vitórias do jogador X."""
        self.vitorias_x += 1

    def reg_vitoria_o(self):
        """Acrescenta uma vitória ao registro de vitórias do jogador O."""
        self.vitorias_o += 1

    def obtem_placar(self):
        """Retorna os números de vitórias do jogador X e do jogador O, respectivamente."""
        return self.vitorias_x, self.vitorias_o

matrizJogo = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
jogador = ["X"]
matrizBtn = []
p = Placar()
l_placar = []

def atualizaPlacar():
    cont_vitorias_x, cont_vitorias_o = p.obtem_placar()
    str_label = "X: {:d} \t O: {:d}".format(cont_vitorias_x, cont_vitorias_o)
    l_placar[0]["text"] = str_label

def posVitoriaIminenteJogadorEmLinhas(jogador):
    for l in range(3):
        contJogador = 0
        posZero = -1
        for c in range(3):
            if matrizJogo[l][c] == jogador:
                contJogador += 1
            if matrizJogo[l][c] == 0:
                posZero = c
        if contJogador == 2 and posZero != -1:
            return l, posZero
    return -1, -1

def posVitoriaIminenteJogadorEmColunas(jogador):
    return -1, -1

def posVitoriaIminenteJogadorEmDiagonais(jogador):
    return -1, -1

def posVitoriaIminenteJogador(jogador):
    linha, coluna = posVitoriaIminenteJogadorEmLinhas(jogador)
    if linha == -1:
        linha, coluna = posVitoriaIminenteJogadorEmColunas(jogador)
        if linha == -1:
            return posVitoriaIminenteJogadorEmDiagonais(jogador)
        else:
            return linha, coluna
    else:
        return linha, coluna

def executaJogada(linha, coluna):
    if matrizJogo[linha][coluna] == 0:
        matrizBtn[linha][coluna]["text"] = jogador[0]
        if jogador[0] == "X":
            matrizJogo[linha][coluna] = 1
            jogador[0] = "O"
        elif jogador[0] == "O":
            matrizJogo[linha][coluna] = 2
            jogador[0] = "X"
        verificaJogo()
    executaJogadaAutomatica()

def executaJogadaAutomatica():
    if jogador[0] == "X":
        return
    linha, coluna = posVitoriaIminenteJogador(2) # 2 é jogador O
    if linha == -1:
        linha, coluna = posVitoriaIminenteJogador(1) # 1 é o jogador X
        if linha == -1:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            while matrizJogo[linha][coluna] != 0:
                if coluna < 2:
                    coluna += 1 # coluna = coluna + 1
                else:
                    coluna = 0
                    linha = (linha + 1) % 3
    executaJogada(linha, coluna)

def verificaDiagonais():
    if matrizJogo[1][1] == 0:
        return 0
    if (matrizJogo[0][0] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[2][2]) or (
            matrizJogo[0][2] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[2][0]):
        return matrizJogo[1][1]
    else:
        return 0

def verificaLinhas():
    for linha in range(3):
        j = matrizJogo[linha][0]
        contIguais = 0
        for coluna in range(3):
            if matrizJogo[linha][coluna] == j:
                contIguais += 1
        if contIguais == 3 and j != 0:
            return j
    return 0

def verificaColunas():
    for coluna in range(3):
        j = matrizJogo[0][coluna]
        contIguais = 0
        for linha in range(3):
            if matrizJogo[linha][coluna] == j:
                contIguais += 1
        if contIguais == 3 and j != 0:
            return j
    return 0

def verificaJogo():
    resultadoEmDiagonais = verificaDiagonais()
    if resultadoEmDiagonais != 0:
        if resultadoEmDiagonais == 1:
            messagebox.showinfo(title="Resultado", message="X venceu")
            p.reg_vitoria_x()
        else:
            messagebox.showinfo(title="Resultado", message="O venceu")
            p.reg_vitoria_o()
        reiniciaJogo()
    else:
        resultadoEmLinhas = verificaLinhas()
        if resultadoEmLinhas != 0:
            if resultadoEmLinhas == 1:
                messagebox.showinfo(title="Resultado", message="X venceu")
                p.reg_vitoria_x()
            else:
                messagebox.showinfo(title="Resultado", message="O venceu")
                p.reg_vitoria_o()
            reiniciaJogo()
        else:
            resultadoEmColunas = verificaColunas()
            if resultadoEmColunas != 0:
                if resultadoEmColunas == 1:
                    messagebox.showinfo(title="Resultado", message="X venceu")
                    p.reg_vitoria_x()
                else:
                    messagebox.showinfo(title="Resultado", message="O venceu")
                    p.reg_vitoria_o()
                reiniciaJogo()
            else:
                contZero = 0
                for l in range(3):
                    for c in range(3):
                        if matrizJogo[l][c] == 0:
                            contZero += 1
                if contZero == 0:
                    messagebox.showinfo(title="Resultado", message="Deu velha!")
                    reiniciaJogo()

def reiniciaJogo():
    for i in range(3):
        for j in range(3):
            matrizJogo[i][j] = 0
            matrizBtn[i][j]["text"] = ""
    jogador[0] = "X"
    atualizaPlacar()

def executaJogada1():
    executaJogada(0, 0)

def executaJogada2():
    executaJogada(0, 1)

def executaJogada3():
    executaJogada(0, 2)

def executaJogada4():
    executaJogada(1, 0)

def executaJogada5():
    executaJogada(1, 1)

def executaJogada6():
    executaJogada(1, 2)

def executaJogada7():
    executaJogada(2, 0)

def executaJogada8():
    executaJogada(2, 1)

def executaJogada9():
    executaJogada(2, 2)

root = tkinter.Frame()
root.master.title("Jogo da velha")

btn1 = tkinter.Button()
btn1["font"] = ("Calibri", "16")
btn1["width"] = 5
btn1["height"] = 3

btn2 = tkinter.Button()
btn2["font"] = ("Calibri", "16")
btn2["width"] = 5
btn2["height"] = 3

btn3 = tkinter.Button()
btn3["font"] = ("Calibri", "16")
btn3["width"] = 5
btn3["height"] = 3

btn4 = tkinter.Button()
btn4["font"] = ("Calibri", "16")
btn4["width"] = 5
btn4["height"] = 3

btn5 = tkinter.Button()
btn5["font"] = ("Calibri", "16")
btn5["width"] = 5
btn5["height"] = 3

btn6 = tkinter.Button()
btn6["font"] = ("Calibri", "16")
btn6["width"] = 5
btn6["height"] = 3

btn7 = tkinter.Button()
btn7["font"] = ("Calibri", "16")
btn7["width"] = 5
btn7["height"] = 3

btn8 = tkinter.Button()
btn8["font"] = ("Calibri", "16")
btn8["width"] = 5
btn8["height"] = 3

btn9 = tkinter.Button()
btn9["font"] = ("Calibri", "16")
btn9["width"] = 5
btn9["height"] = 3

btn1["command"] = executaJogada1
btn2["command"] = executaJogada2
btn3["command"] = executaJogada3
btn4["command"] = executaJogada4
btn5["command"] = executaJogada5
btn6["command"] = executaJogada6
btn7["command"] = executaJogada7
btn8["command"] = executaJogada8
btn9["command"] = executaJogada9

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

matrizBtn = [[btn1, btn2, btn3],
             [btn4, btn5, btn6],
             [btn7, btn8, btn9]]

labelPlacar = tkinter.Label(text="X: 0 \t O: 0")
labelPlacar["font"] = ("Calibri", "16")
labelPlacar["height"] = 2
labelPlacar.grid(row=3, column=0, columnspan=3)

l_placar = [labelPlacar]
atualizaPlacar()

root.mainloop()
