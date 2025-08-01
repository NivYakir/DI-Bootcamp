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
    
    word = random.choice(words)
    return word

def create_board(word):
    '''Takes a word and creates a hangman board from it'''
    board = ["*" for l in word]
    return board

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

def player_input(word, board):
    while True:
        letter = input("Enter a letter: ")
        if len(letter) == 1 and letter.isalpha() == True:
            for i in range(len(board)):
                if letter == word[i]:
                    board[i] = letter
            break
        else:
            print("Invalid Input.")



player_input()