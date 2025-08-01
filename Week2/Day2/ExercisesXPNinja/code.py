# Exercise 1: What's Your Name?

def get_full_name(first_name = 'niv', last_name = 'yakir', middle_name=''):
    first_name, last_name, middle_name = first_name.capitalize(), last_name.capitalize(), middle_name.capitalize()
    if middle_name == '':
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"

print(get_full_name())

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
    '"': '.-..-.', '@': '.--.-.', '=': '-...-', ' ' : '/'
}

reversed_code_dict = {v:k for k, v in morse_code_dict.items()}

def english_to_morse():
    '''Returns a morse encoded text'''
    text = input(f"Enter the text you wish to translate:\n")
    text = text.upper()
    tranlated = ""
    for char in text:
        if char == ' ':
            tranlated += '/ '
        else:
            tranlated += morse_code_dict[char] + " "
    return tranlated

print(english_to_morse())

def morse_to_english():
    '''Translates a text in morse code to English'''
    text = input(f"Enter the encoded text you wish to translate:\n")
    words = text.split(' ')
    cleaned = [word for word in words if word != '']
    tranlated = ""
    for word in cleaned:
        tranlated += reversed_code_dict[word]
    return tranlated

print(morse_to_english())

def insertion_sort(alist):
   '''Sorts a list of numbers from smallest to larges'''
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)

