import random

def random_word():
    '''Returns a random word from a list'''
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist)

def create_board(word):
    return ['*' for char in word]

def letter_check(word, board):
    while True:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) != 1 or user_input.isalpha() == False:
            for i in range(len(board)):
                if user_input == word[i]:
                    board[i] = user_input
                    break
        else:
            print("Invalid input.")
            continue


def display_gallows(attempt):
    '''Displays the hangman's status'''
    board_stage = ["""
            -------
            |  O  |
            | /|\\ |
            | / \\ |
            -------
    """,
        """
            -------
            |  O  |
            | /|\\ |
            | /   |
            -------
    """,
    """
            -------
            |  O  |
            | /|\\ |
            |     |
            -------
    """,
    """
            -------
            |  O  |
            | /|  |
            |     |
            -------
    """,
    """
            -----
            | O |
            | | |
            |   |
            -----
    """,
    """
            -------
            |  O  |
            |     |
            |     |
            -------
    """,
    """
            -------
            |     |
            |     |
            |     |
            -------
    """]