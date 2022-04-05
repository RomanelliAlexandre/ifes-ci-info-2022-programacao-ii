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
        colunaComZero = -1
        for c in range(3):
            if matrizJogo[l][c] == jogador:
                contJogador += 1
            if matrizJogo[l][c] == 0:
                colunaComZero = c
        if contJogador == 2 and colunaComZero != -1:
            return l, colunaComZero
    return -1, -1

def posVitoriaIminenteJogadorEmColunas(jogador):
    for c in range(3):
        contJogador = 0
        linhaComZero = -1
        for l in range(3):
            if matrizJogo[l][c] == jogador:
                contJogador += 1
            if matrizJogo[l][c] == 0:
                linhaComZero = l
        if contJogador == 2 and linhaComZero != -1:
            return linhaComZero, c
    return -1, -1

def posVitoriaIminenteJogadorNaDiagonal(jogador, diagonal):
    contJogador = 0
    posZero = -1
    for i in range(3):
        if (diagonal == 0 and matrizJogo[i][i] == jogador):
            contJogador += 1
        if (diagonal == 1 and matrizJogo[2 - i][i] == jogador):
            contJogador += 1
        if (diagonal == 0 and matrizJogo[i][i] == 0):
            posZero = i
        if (diagonal == 1 and matrizJogo[2 - i][i] == 0):
            posZero = i
    if contJogador == 2:
        return posZero
    else:
        return -1

def posVitoriaIminenteJogadorEmDiagonais(jogador):
    pos = posVitoriaIminenteJogadorNaDiagonal(jogador, 0)
    if pos != -1:
        return pos, pos
    else:
        pos = posVitoriaIminenteJogadorNaDiagonal(jogador, 1)
        if pos != -1:
            return 2 - pos, pos
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

def constroiBotao(linha, coluna):
    btn = tkinter.Button()
    btn.grid(row=linha, column=coluna)
    btn["width"] = 5
    btn["height"] = 3
    btn["font"] = ("Calibri", "16")
    return btn

btn1 = constroiBotao(0, 0)
btn2 = constroiBotao(0, 1)
btn3 = constroiBotao(0, 2)
btn4 = constroiBotao(1, 0)
btn5 = constroiBotao(1, 1)
btn6 = constroiBotao(1, 2)
btn7 = constroiBotao(2, 0)
btn8 = constroiBotao(2, 1)
btn9 = constroiBotao(2, 2)

matrizBtn = [[btn1, btn2, btn3],
             [btn4, btn5, btn6],
             [btn7, btn8, btn9]]

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
