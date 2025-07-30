# Tic-Tac-Toe

def display_board():
    '''Displays the current state of the gameboard'''
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")


def player_input(player):
    '''Inserts the players mark to the position on the board'''
    position_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}
    while True:
        try:
            position = int(input(f"Player {player}: Select your position (1 - 9):\n"))
            if position in range(1,10):
                row, column = position_map[position]
                if board[row][column] == ' ':
                    if player == 1:
                        board[row][column] = 'X'
                    else:
                        board[row][column] = 'O'
                    break
                else:
                    print("That position is already taken.")
            else:
                print("You must enter a number between 1 and 9.")
        except ValueError:
            print(f"You must enter a valid number.")


def check_win(board, player):
    '''Checks if the current player has 3 in-a-row'''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        elif board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    elif board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        return False

    
def check_tie(board):
    '''Checks if all the positions in the board are filled'''
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def play():
    '''Play a game of Tic-Tac-Toe with a friend'''
    global board 
    board = [[' ' for cells in range(3)] for cells in range(3)]
    player = 1
    while True:
        display_board()
        player_input(player)
        if check_win(board,player) == True:
            print(f"Player {player} wins!")
            display_board()
            break
        elif check_tie(board) == True:
            print("It's a tie!")
            display_board()
            break
        if player == 1:
            player = 2
        else:
            player = 1

play()