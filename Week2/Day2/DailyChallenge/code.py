# Exercise 1: Solve the Matrix
import re

MATRIX_STR = '''7iiTsxh%?i #sM $a #t%'''

def string_to_2D(text):
    result = []
    for i in range(0,len(text),3):
        result.append(text[i:i + 3])
    return result

matrix = string_to_2D(MATRIX_STR)
print(matrix)

def filter():
    matrix = string_to_2D(MATRIX_STR)
    for _ in range(len(matrix)):
        collumn = 0
        result = ''
        while collumn != 3:
            for ele in matrix:
                letter = ele[collumn]
                result += letter
            collumn += 1
        
    cleaned = re.sub(
    r'(?<=[A-Za-z])[^A-Za-z]+(?=[A-Za-z])'  # junk between letters
    r'|^[^A-Za-z]+'                         # junk at the start
    r'|[^A-Za-z]+$',                        # junk at the end
    ' ',result).strip()

    return cleaned

print(filter())