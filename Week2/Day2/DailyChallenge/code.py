# Exercise 1: Solve the Matrix

MATRIX_STR = '''7ii
Tsx
h%?
i #
sM 
$a 
#t%'''

def list_to_2d(text):
    result = []
    temp = text.split('\n')
    for line in temp:
        row = []
        for char in line:
            row.append(char)
        result.append(row)
    return result

print(list_to_2d(MATRIX_STR))

def decode_matrix(text):
    result = ''
    matrix = list_to_2d(text)
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            letter = matrix[row][col]
            result += letter
    return result


uncleaned = decode_matrix(MATRIX_STR)

def filter_text(text):
    result = ''
    for i, char in enumerate(text):
        if i == 0:
            if char.isalpha() == True:
                result += char

        elif char.isalpha() == True:
            result += char
        
        elif (char.isalpha() == False) and text[i - 1].isalpha() == True:
            result += ' '
    return result


print(filter_text(uncleaned))