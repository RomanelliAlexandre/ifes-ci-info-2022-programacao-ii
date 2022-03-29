import tkinter
from tkinter import messagebox

matrizJogo = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
jogador = ["X"]
matrizBtn = []

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

def verificaDiagonais():
    if matrizJogo[1][1] == 0:
        return 0
    if (matrizJogo[0][0] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[2][2]) or (
            matrizJogo[0][2] == matrizJogo[1][1] and matrizJogo[1][1] == matrizJogo[2][0]):
        return matrizJogo[1][1]
    else:
        return 0

def verificaJogo():
    resultadoEmDiagonais = verificaDiagonais()
    if resultadoEmDiagonais != 0:
        if resultadoEmDiagonais == 1:
            messagebox.showinfo(title="Resultado", message="X venceu")
        else:
            messagebox.showinfo(title="Resultado", message="O venceu")
        reiniciaJogo()

def reiniciaJogo():
    for i in range(3):
        for j in range(3):
            matrizJogo[i][j] = 0
            matrizBtn[i][j]["text"] = ""
    jogador[0] = "X"

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

root.mainloop()
