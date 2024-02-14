def display_board(board): #function to display the board at the current point in the game
    print(" " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "\n---+---+---")
    print(" " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "\n---+---+---")
    print(" " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])

def player_input(Player_Symbol, played_moves): #function to get player to enter their move
    while True:
        try:
            move = int(input("Player "+ Player_Symbol +". Enter your move (1-9): "))
            if 1<=move<=9:
                if move not in played_moves: #check if move has already been played
                    played_moves.append(move) # add move to list of moves that have been played
                    return move 
                else:
                    print("This move has already been played. Try again.")
            else:
                print("Invalid input. Please enter a number between 1 and 9")
        except:
            print("Invalid input. Please enter a number.")

def play_tic_tac_toe(): #function to play the game
    # initialising variables
    Players = ["X", "O"]
    Current_player = 0
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    played_moves = []

    while True:
        display_board(board)
        move = player_input(Players[Current_player], played_moves) #obtaining move from player

        ################adding move to board################
        if move <= 3:
            board[0][move - 1] = Players[Current_player]
        elif 4 <= move <= 6:
            board[1][(move % 3) - 1] = Players[Current_player]
        else:
            board[2][(move % 3) - 1] = Players[Current_player]
        ####################################################

        if Current_player == 0: #swapping players for next round
            Current_player = 1
        else:
            Current_player = 0


if __name__ == "__main__":
    play_tic_tac_toe()