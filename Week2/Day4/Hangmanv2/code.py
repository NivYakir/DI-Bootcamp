import random

def generate_word():
    '''Generates a random word from a pre-set list'''

    words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "iguana", "jungle", "kangaroo", "lemon", "mango", "nectarine", "orange", "papaya",
    "quartz", "raspberry", "strawberry", "tangerine", "umbrella", "violet", "watermelon",
    "xylophone", "yogurt", "zebra", "amazing", "brave", "calm", "daring", "eager",
    "friendly", "gentle", "happy", "intelligent", "jolly", "kind", "lively", "mighty",
    "nice", "obedient", "polite", "quick", "respectful", "strong", "thoughtful", "useful",
    "vast", "wise", "xenial", "young", "zealous", "climb", "draw", "eat", "fly", "grow",
    "help", "imagine", "jump", "kick", "laugh", "move", "nod", "open", "play", "question",
    "run", "sleep", "talk", "understand", "visit", "walk", "x-ray", "yawn", "zoom",
    "book", "cloud", "dream", "energy", "fire", "garden", "hill", "island", "jewel",
    "key", "light", "mountain", "night", "ocean", "path", "quiet", "rain", "sun", "tree",
    "universe", "valley", "wind", "xenon", "yard", "zone","xenomorph","geography",
    ]

    return random.choice(words)

def create_board(word):
    '''Takes a word and creates a hangman board from it'''
    board = ["*" for _ in word]
    return board

def display_board(board):
    print(board)

def show_gallows(attempt):
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

def player_input(word, board, guessed_letters):
    while True:
        letter = input("Enter a letter: ")
        if len(letter) == 1 and letter.isalpha() == True:
            if letter in word: 
                for i in range(len(board)):
                    if letter == word[i]:
                        board[i] = letter
                break
            else:
                guessed_letters.append(letter)
        else:
            print("Invalid Input.")


def hangman():
    word = generate_word()
    board = create_board(word)
    attempt = 6
    guessed_letters = []
    print(f"Welcome to Hangman! See if you can guess the word, letter by letter.\nYou have {attempt} attempts left!")
    show_gallows(attempt)
    while True:
        display_board(board)
        player_input(word, board, guessed_letters)


hangman()