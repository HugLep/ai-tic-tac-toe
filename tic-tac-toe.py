import tkinter as tk
from tkinter import *


# Plateau de jeu 3x3
board = [[0 for j in range(3)] for i in range(3)]



# Fonction appelée lorsqu'une case est cliquée
def toggle_value(row, col):
    global nbPlace

    if board[row][col] == 0 and nbPlace < 1:
        board[row][col] = 1
        canvas.itemconfig(cells[row][col], fill='Blue')
        nbPlace = nbPlace + 1

        # Passage automatique au prochain tour
        nextRound()

# Fonction qui verifie si le match doit etre terminé par une victoire de l'ordinateur (1), du joueur (-1) ou un match nul (0)
def testWin(board):
    for p in [1, 2]:
        for x in [0, 1, 2]:
            if board[x][0] == p and board[x][1] == p and board[x][2] == p:
                if p == 2 :
                    return 1
                elif p == 1 :
                    return -1
            elif board[0][x] == p and board[1][x] == p and board[2][x] == p:
                if p == 2 :
                    return 1
                elif p == 1 :
                    return -1
        if board[0][0] == p and board[1][1] == p and board[2][2] == p:
            if p == 2 :
                return 1
            elif p == 1 :
                return -1
        elif board[0][2] == p and board[1][1] == p and board[2][0] == p:
            if p == 2 :
                return 1
            elif p == 1 :
                return -1

    # Match Nul
    rest = 0
    for j in [0, 1, 2]:
        for i in [0, 1, 2]:
            if board[j][i] == 0:
                rest = rest + 1
        
    if rest == 0:
        return 0


# Algorithme Minimax
def minimax(board, depth, isMaximizing):
    result = testWin(board)
    if result == 1 or result == 0 or result == -1 :
        return result
    
    if isMaximizing == True:
        bestScore = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    score = minimax(board, depth + 1, False)
                    board[i][j] = 0
                    bestScore = max(score, bestScore)
        return bestScore
    
    elif isMaximizing == False:
        bestScore = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    score = minimax(board, depth + 1, True)
                    board[i][j] = 0

                    bestScore = min(score, bestScore)
        return bestScore


# Fonction qui va trouver le meilleur mouvement a faire pour l'ordinateur, à l'aide le l'algorithme Minimax
def meilleur_mouvement(plateau):
    global meilleur_move_i, meilleur_move_j

    meilleur_score = float('-inf')

    meilleur_move_i = None
    meilleur_move_j = None

    for i in range(3):
        for j in range(3):
            
            if plateau[i][j] == 0:
                plateau[i][j] = 2
                score = minimax(plateau, 0, False)
                plateau[i][j] = 0
                if score > meilleur_score:
                    meilleur_score = score
                    meilleur_move_i = i
                    meilleur_move_j = j


# Fonction pour passer au prochain tour apres le tour du joueur
def nextRound():
    global nbPlace
    if testWin(board) != 1 and testWin(board) != 0 and testWin(board) != -1:
        meilleur_mouvement(board)
        board[meilleur_move_i][meilleur_move_j] = 2
        canvas.itemconfig(cells[meilleur_move_i][meilleur_move_j], fill='red')

    if testWin(board) != 1 and testWin(board) != 0 and testWin(board) != -1:
        nbPlace = 0
    
    else:
        winnerWindows(testWin(board))



# Fonction pour recommencer la partie
def restart():
    global board, nbPlace, root1
    for i in range(3):
        for j in range(3):
            board[i][j] = 0
            canvas.itemconfig(cells[i][j], fill='White')
    
    nbPlace = 0
    root1.destroy()

# Fonction pour stopper le jeu
def quit():
    global root, root1
    
    root1.destroy()
    root.destroy()


# Fonction pour créer la fenetre du plateau de jeu
def create_grid(rows, cols):
    global canvas, cells, board, root, nbPlace
    

    root = tk.Tk()
    root.title("Tic Tac Toe - HugLep")

    canvas = tk.Canvas(root, width=cols*150, height=rows*150)
    canvas.pack()

    cells = [[None for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):
        for i in range(rows):
            x1 = j * 150
            y1 = i * 150
            x2 = x1 + 150
            y2 = y1 + 150
            cells[i][j] = canvas.create_rectangle(x1, y1, x2, y2, outline='black', fill='white')
            canvas.tag_bind(cells[i][j], '<Button-1>', lambda e, row=i, col=j: toggle_value(row, col))

    nbPlace = 0

    root.mainloop()

# Fonction pour créer la fenetre anonncant le vainceur ou un match nul
def winnerWindows(winner):
    global root1
    root1 = tk.Tk()

    if winner == 1:
        monAffichage = Label(root1, text = "L'ordinateur a gagné")
        monAffichage.pack()
    if winner == -1:
        monAffichage = Label(root1, text = "Le joueur a gagné")
        monAffichage.pack()
    if winner == 0:
        monAffichage = Label(root1, text = "Match Nul")
        monAffichage.pack()
    
    restartButton = Button(root1, text = "Recommencer", command=restart)
    restartButton.pack()

    quitButton = Button(root1, text = "Quitter", command=quit)
    quitButton.pack()

    root1.mainloop()




# Appel de la fonction pour créer le plateau 3x3
create_grid(3, 3)