import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic Tac Toe")
current_player = "X"
game_board = [["", "", ""],
              ["", "", ""],
              ["", "", ""]]

def button_click(row, col):
    global current_player
    if game_board[row][col] == "":
        buttons[row][col].config(text=current_player)
        game_board[row][col] = current_player
        if check_win():
            message_dis()
        elif check_draw():
            message_dis('draw')
        else:
            if current_player == "X":
                current_player = "O"
                ai_move()

def check_win():
    for row in range(3):
        if game_board[row][0] == game_board[row][1] == game_board[row][2] != "":
            return True

    for col in range(3):
        if game_board[0][col] == game_board[1][col] == game_board[2][col] != "":
            return True

    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "":
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "":
        return True
    return False

def check_draw():
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == "":
                return False
    return True

def message_dis(txt=None):
    if txt != 'draw':
        messagebox.showinfo('Game Over', f'Player {current_player} wins!')
    else:
        messagebox.showinfo('Game Over', 'It is a Draw')
    msg_box = messagebox.askokcancel('Tic Tac Toe', 'Do you wish to continue?')
    if not msg_box:
        window.destroy()
    else:
        reset_screen()

def reset_screen():
    global current_player, game_board

    current_player = "X"
    game_board = [["", "", ""],
                  ["", "", ""],
                  ["", "", ""]]

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")

def ai_move():
    depth = sum(cell == "" for row in game_board for cell in row)
    global current_player
    best_score = -10000
    best_move = None
    for row in range(3):
        for col in range(3):
            if game_board[row][col] == "":
                game_board[row][col] = "O"
                score = minimax(game_board, depth, False)
                game_board[row][col] = ""
                if score > best_score:
                    best_score = score
                    best_move = [row, col]
    buttons[best_move[0]][best_move[1]].config(text = "O")
    game_board[best_move[0]][best_move[1]] = "O"
    if check_win():
        message_dis()
    elif check_draw():
        message_dis('draw')
    else:
        current_player = "X"

def minimax(board, depth, AI):
    if check_win():
        if AI:
            return -10*depth
        else:
            return 10*depth
    elif check_draw():
        return 0
    else:
        if AI:
            best_score = -10000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = "O"
                        score =minimax(board, depth-1, False)
                        board[row][col] = ""
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = 10000
            for row in range(3):
                for col in range(3):
                    if board[row][col] == "":
                        board[row][col] = "X"
                        score = minimax(board, depth-1, True)
                        board[row][col] = ""
                        if score < best_score: best_score = score
            return best_score



buttons = []
for row in range(3):
    button_row = []
    for col in range(3):
        button = tk.Button(window, text="", width=6, height=5, command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)
window.mainloop()