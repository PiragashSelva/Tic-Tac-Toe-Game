# Tic-Tac-Toe Game

This is a simple implementation of the classic Tic-Tac-Toe game, now featuring a graphical user interface (GUI) using TKinter. The game allows two players to take turns marking spaces in a 3x3 grid, attempting to make a row, column, or diagonal of their symbol (either 'X' or 'O').

## How to Play

1. Clone the repository to your local machine.
2. Navigate to the directory containing the game files.
3. Activate the virtual environment if needed.
4. Run the game by executing the `tic_tac_toe.py` file.
5. Click on the buttons in the graphical window to make your moves.

## Gameplay Instructions

- The game is played on a 3x3 grid displayed in the window.
- Players take turns clicking on empty spaces on the grid to place their symbol ('X' or 'O').
- The first player to align three of their symbols either horizontally, vertically, or diagonally wins the game.
- If all spaces on the grid are filled and no player has achieved three in a row, the game ends in a draw.

## Getting Started

To get started with the game, follow the installation instructions above and execute the `tic_tac_toe.py` file. The game will open in a new window where you can play by clicking on the buttons.

## Functionality

### `check_winner(board, player)`

This function checks if the current player has won the game by achieving three in a row horizontally, vertically, or diagonally.

### `reset_game()`

This function resets the game board and variables to start a new game.

### `button_click(row, col)`

This function handles button clicks on the game board, updates the board state, checks for a winner or a draw, and switches players.

### `update_turn_label()`

This function updates the turn label to display whose turn it is.

## Dependencies

This project uses the `TKinter` library for creating the GUI. It is typically included in standard Python installations, so no additional installation steps are necessary.
