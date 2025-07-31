import random

def random_word():
    '''Returns a random word from a list'''
    wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    return random.choice(wordslist)

def create_board(word):
    return ['*' for char in word]

def display_board(board):
    print(f"Board Status: {board}")

def letter_check(board,word,guessed_letters):
    while True:
        user_input = input("Guess a letter: ").lower()
        print(user_input)
        if len(user_input) == 1 and (user_input.isalpha() == True):
            if user_input in guessed_letters:
                print("You have already guessed this letter")
            else: 
                if user_input in word:
                    for i in range(len(board)):
                        if user_input == word[i]:
                            board[i] = user_input
                            if user_input not in guessed_letters:
                                guessed_letters.append(user_input)
                    return True
                else:
                    if user_input not in guessed_letters:
                        guessed_letters.append(user_input)
                        print("Letter is not in the word.")
                    return False
        else:
            print("Invalid input.")


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
            -------
            |  O  |
            |  |  |
            |     |
            -------
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

    print(board_stage[attempt])


def win_check(board):
    '''Returns True if all the letters have been guessed correctly'''
    if '*' in board:
        return False
    else:
        return True


def main():
    word = random_word()
    board = create_board(word)
    guessed_letters = []
    attempt = 6
    print("Welcome to Hangman! Try to guess the word by inputting a letter. You have 6 tries to guess all the letters!")
    while attempt > 0:
        print(f"You have {attempt} tries left!")
        display_board(board)
        print(f"Guessed Letters: {guessed_letters}")
        display_gallows(attempt)
        if letter_check(board,word,guessed_letters) == False:
            attempt -= 1
        if win_check(board) == True:
            break
    if win_check(board) == False:
        print("You lose!")
    else:
        print("You win!")
    display_gallows(attempt)
    print(f"The word was {word}")


main()





