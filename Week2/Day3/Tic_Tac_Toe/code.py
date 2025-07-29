# Tic-Tac-Toe

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def display_board():
    '''Displays the current state of the gameboard'''
    print(f"  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  ")
    print(f"-----|-----|-----")
    print(f"  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  ")

def player_input():
    '''Inserts the players mark to the inputted position on the board'''
    position_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2)
}
    while True:
        try:
            position = int(input("Select your position (1 - 9):\n"))
            if position in range(1,10):
                row, column = position_map[position]
                if board[row][column] == ' ':
                    board[row][column] = 'X'
                    break
                else:
                    print("That position is already taken.")
            else:
                print("You must enter a number between 1 and 9.")
        except ValueError:
            print(f"You must enter a valid number.")
    display_board()

player_input()