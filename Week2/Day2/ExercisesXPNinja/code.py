# # Exercise 1: What's Your Name?

# def get_full_name(first_name = 'niv', last_name = 'yakir', middle_name=''):
#     first_name, last_name, middle_name = first_name.capitalize(), last_name.capitalize(), middle_name.capitalize()
#     if middle_name == '':
#         return f"{first_name} {last_name}"
#     else:
#         return f"{first_name} {middle_name} {last_name}"

# print(get_full_name())

# Exercise 2: From English to Morse

morse_code_dict = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--', ':': '---...',
    "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '"': '.-..-.', '@': '.--.-.', '=': '-...-'
}

reversed_code_dict = {v:k for k, v in morse_code_dict.items()}

def english_to_morse():
    '''Returns a morse encoded text'''
    text = input(f"Enter the text you wish to translate:\n")
    for char in text: