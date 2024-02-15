# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game to be played in the terminal. The game allows two players to take turns marking spaces in a 3x3 grid, attempting to make a row, column, or diagonal of their symbol (either 'X' or 'O').

## How to Play

1. Clone the repository to your local machine.
2. Navigate to the directory containing the game files.
3. Activate the virtual environment.
4. Run the game by executing the `tic_tac_toe.py` file in your terminal.
5. During each player's turn, input a number between 1 and 9 corresponding to the position on the game board as shown below:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

## Gameplay Instructions

- The game is played on a 3x3 grid.
- Players take turns placing their symbol ('X' or 'O') in an empty space on the grid.
- The first player to align three of their symbols either horizontally, vertically, or diagonally wins the game.
- If all spaces on the grid are filled and no player has achieved three in a row, the game ends in a draw.

## Getting Started

To get started with the game, follow the installation instructions above and execute the `tic_tac_toe.py` file. The game will prompt you to input your moves in the terminal.

## Functionality

### `display_board(board)`

This function displays the current state of the game board in the terminal.

### `player_input(Player_Symbol, played_moves)`

This function prompts the current player to input their move and ensures that the input is valid. It returns the chosen move.

### `check_winner(board, player)`

This function checks if the current player has won the game by achieving three in a row horizontally, vertically, or diagonally.

### `play_tic_tac_toe()`

This is the main function that controls the flow of the game. It initializes the game variables, handles player turns, and checks for a winner or a draw.

## Dependencies

This project uses the `art` library to display ASCII art in the terminal. You can install it using pip:

```
pip install art
```

Alternatively, a virtual environment is included. You can activate it by running the following command:

```
.venv\Scripts\activate
```