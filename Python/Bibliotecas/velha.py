import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Jogo da Velha")

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

buttons = [[None for _ in range(3)] for _ in range(3)]

def reset_game():
    global player
    player = "X"
    for x in range(3):
        for y in range(3):
            board[x][y] = " "
            buttons[x][y].config(text=" ")

def make_move(x, y, player):
    if board[x][y] != " ":
        print("Espaço já ocupado!")
        return False
    else:
        board[x][y] = player
        buttons[x][y].config(text=player)
        return True

def has_winner():
    # linhas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    # colunas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    # diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    # sem vencedor
    return None

def is_tie():
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def on_button_click(x, y):
    global player
    if not make_move(x, y, player):
        return
    winner = has_winner()
    if winner:
        messagebox.showinfo(title="Vitória", message="Jogador {} venceu!".format(winner))
        reset_game()
        return
    if is_tie():
        messagebox.showinfo(title="Empate", message="O jogo terminou empatado!")
        reset_game()
        return
    player = "X" if player == "O" else "O"

for x in range(3):
    for y in range(3):
        button = tk.Button(root, text=" ", font=("Arial", 32), width=3, height=1, command=lambda x=x, y=y: on_button_click(x, y))
        button.grid(row=x, column=y)
        buttons[x][y] = button

player = "X"

root.mainloop()