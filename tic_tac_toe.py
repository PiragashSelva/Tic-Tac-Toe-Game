import tkinter as tk
from tkinter import messagebox
from art import *


def check_winner(board, player):
    # Function to check if the player has won the game
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    if (
        board[0][0] == board[1][1] == board[2][2] == player
        or board[0][2] == board[1][1] == board[2][0] == player
    ):
        return True
    return False


def reset_game():
    # Function to reset the game
    global board, played_moves, current_player
    board = [[" " for column in range(3)] for row in range(3)]
    played_moves = []
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")
    current_player = 0


def button_click(row, col):
    # Function to handle button clicks
    global current_player, played_moves

    if board[row][col] == " ":
        # Update the board
        board[row][col] = Players[current_player]
        buttons[row][col].config(text=Players[current_player])

        # Check for a winner
        if check_winner(board, Players[current_player]):
            messagebox.showinfo(
                "Game Over", "Player " + Players[current_player] + " has won!"
            )
            reset_game()
            return

        # Check for a draw
        played_moves.append((row, col))
        if len(played_moves) == 9 and not check_winner(board, Players[current_player]):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
            return

        # Swapping players for next round
        current_player = 1 - current_player


# Initialize variables
Players = ["X", "O"]
current_player = 0
board = [[" " for column in range(3)] for row in range(3)]
played_moves = []

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create canvas for drawing the game board
canvas = tk.Canvas(root, width=300, height=300)
canvas.grid(row=0, column=0)

# Draw horizontal lines
for i in range(1, 3):
    canvas.create_line(0, i * 100, 300, i * 100, fill="black", width=3)

# Draw vertical lines
for i in range(1, 3):
    canvas.create_line(i * 100, 0, i * 100, 300, fill="black", width=3)

# Create buttons for the game board
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        x1 = j * 100 + 10
        y1 = i * 100 + 10
        x2 = (j + 1) * 100 - 10
        y2 = (i + 1) * 100 - 10
        button = tk.Button(
            root,
            text=" ",
            font=("Helvetica", 24),
            width=3,
            height=1,
            command=lambda row=i, col=j: button_click(row, col),
            borderwidth=0,  # Set border width to 0
            highlightthickness=0,  # Remove highlight thickness
            bg=canvas.cget("bg"),  # Set background color to match canvas
            activebackground=canvas.cget(
                "bg"
            ),  # Set active background color to match canvas
        )
        row_buttons.append(button)
        button.place(x=x1, y=y1, width=x2 - x1, height=y2 - y1)
    buttons.append(row_buttons)

root.mainloop()