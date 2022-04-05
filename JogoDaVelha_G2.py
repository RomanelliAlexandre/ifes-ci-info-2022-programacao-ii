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
matrizBtn = []
jogador = ["X"]
l_placar = []
p = Placar()

def atualizaPlacar():
    cont_vitorias_x, cont_vitorias_o = p.obtem_placar()
    l_placar[0]["text"] = "X: {:d} \t O: {:d}".format(cont_vitorias_x, cont_vitorias_o)

def verificaDiagonais():
    if (matrizJogo[0][0] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[2][2]) or (
        matrizJogo[2][0] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[0][2]):
        return matrizJogo[1][1]
    return 0

def verificaLinha(linha):
    for coluna in range(3):
        if matrizJogo[linha][coluna] != matrizJogo[linha][0]:
            return 0
    return matrizJogo[linha][0]

def verificaColuna(coluna):
    for linha in range(3):
        if matrizJogo[linha][coluna] != matrizJogo[0][coluna]:
            return 0
    return matrizJogo[0][coluna]

def verificaJogo():
    resultadoDiagonais = verificaDiagonais()
    if resultadoDiagonais != 0:
        if resultadoDiagonais == 1:
            messagebox.showinfo(title="Resultado", message="X venceu!")
            p.reg_vitoria_x()
        else:
            messagebox.showinfo(title="Resultado", message="O venceu!")
            p.reg_vitoria_o()
        reiniciaJogo()
    else:
        for i in range(3):
            resultadoLinha = verificaLinha(i)
            resultadoColuna = verificaColuna(i)
            if resultadoLinha != 0 or resultadoColuna != 0:
                vitorioso = ""
                if resultadoLinha != 0:
                    vitorioso = "X" if resultadoLinha == 1 else "O"
                else:
                    vitorioso = "X" if resultadoColuna == 1 else "O"
                mensagem = vitorioso + " venceu!"
                messagebox.showinfo(title="Resultado", message=mensagem)
                if vitorioso == "X":
                    p.reg_vitoria_x()
                else:
                    p.reg_vitoria_o()
                reiniciaJogo()
            else:
                # contar quantidade de valores 0 (zero) na matrizJogo
                contZero = 0
                for i in range(3):
                    for j in range(3):
                        if matrizJogo[i][j] == 0:
                            contZero += 1
                # se esta quantidade for nenhum, então deu velha (exibir mensagem e reiniciar jogo)
                if contZero == 0:
                    messagebox.showinfo(title="Resultado", message="Deu velha!")
                    reiniciaJogo()

def reiniciaJogo():
    atualizaPlacar()
    for i in range(3):
        for j in range(3):
            matrizJogo[i][j] = 0
            matrizBtn[i][j]["text"] = ""
    jogador[0] = "X"

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

def posicao_de_vitoria_iminente(jog):
    linha, coluna = posVitoriaIminenteJogadorEmLinhas(jog)
    if linha == -1:
        linha, coluna = posVitoriaIminenteJogadorEmColunas(jog)
        if linha == -1:
            return posVitoriaIminenteJogadorEmDiagonais(jog)
#       else:
#           return linha, coluna
#   else:
#       return linha, coluna
    return linha, coluna

def executaJogadaAutomatica():
    if jogador[0] == "X":
        return
    linha, coluna = posicao_de_vitoria_iminente(2)
    if linha < 0:
        linha, coluna = posicao_de_vitoria_iminente(1)
        if linha < 0:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            while matrizJogo[linha][coluna] != 0:
                coluna = (coluna + 1) % 3
                if coluna == 0:
                    linha = (linha + 1) % 3
    executaJogada(linha, coluna)

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
btn2 = tkinter.Button()
btn3 = tkinter.Button()
btn4 = tkinter.Button()
btn5 = tkinter.Button()
btn6 = tkinter.Button()
btn7 = tkinter.Button()
btn8 = tkinter.Button()
btn9 = tkinter.Button()

matrizBtn = [[btn1, btn2, btn3],
             [btn4, btn5, btn6],
             [btn7, btn8, btn9]]

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

btn1["width"] = 5
btn2["width"] = 5
btn3["width"] = 5
btn4["width"] = 5
btn5["width"] = 5
btn6["width"] = 5
btn7["width"] = 5
btn8["width"] = 5
btn9["width"] = 5

btn1["height"] = 3
btn2["height"] = 3
btn3["height"] = 3
btn4["height"] = 3
btn5["height"] = 3
btn6["height"] = 3
btn7["height"] = 3
btn8["height"] = 3
btn9["height"] = 3

btn1["font"] = ("Calibri", "16")
btn2["font"] = ("Calibri", "16")
btn3["font"] = ("Calibri", "16")
btn4["font"] = ("Calibri", "16")
btn5["font"] = ("Calibri", "16")
btn6["font"] = ("Calibri", "16")
btn7["font"] = ("Calibri", "16")
btn8["font"] = ("Calibri", "16")
btn9["font"] = ("Calibri", "16")

btn1["command"] = executaJogada1
btn2["command"] = executaJogada2
btn3["command"] = executaJogada3
btn4["command"] = executaJogada4
btn5["command"] = executaJogada5
btn6["command"] = executaJogada6
btn7["command"] = executaJogada7
btn8["command"] = executaJogada8
btn9["command"] = executaJogada9

labelPlacar = tkinter.Label()
labelPlacar["font"] = ("Calibri", "16")
labelPlacar["height"] = 2
labelPlacar.grid(row=3, column=0, columnspan=3)

l_placar = [labelPlacar]
atualizaPlacar()

root.mainloop()
