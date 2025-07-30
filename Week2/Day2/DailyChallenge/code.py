# Exercise 1: Solve the Matrix

MATRIX_STR = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

def string_to_2D(text):
    '''Converts a string to a 2D Matrix'''
    result = []
    temp = text.split('\n')
    for rows in temp:
        row = []
        for char in rows:
            row.append(char)
        result.append(row)
    return result

matrix = string_to_2D(MATRIX_STR)

# matrix = [[char for char in row] for row in MATRIX_STR.split('\n')]

def matrix_decoder():
    row_num = len(matrix)
    col_num = len(matrix[0])
    result = ''
    for col in range(col_num):
        for row in range(row_num):
            char = matrix[row][col]
            result += char
    return result

def text_clean():
    uncleaned = matrix_decoder()
    result = ''

    for i, char in enumerate(uncleaned):
        if i == 0:
            if char.isalpha():
                result += char
        elif char.isalpha():
            result += char
        elif (char.isalpha() == False) and (uncleaned[i - 1].isalpha() == True):
            result += ' '
    
    return result.strip()

print(text_clean())