# Challenge 1: Sorting

def sort_string():
    my_string = input("Enter a string of words, where each word is separated by a comma:\n")
    temp = my_string.split(',')
    sorted_list = sorted(temp)
    result = ', '.join(sorted_list)
    return result

print(sort_string())

# Challenge 2: 

my_sent = "Margaret's toy is a pretty doll."

def longest_word(sentence):
    longest = ''
    temp = sentence.split(' ')
    for word in temp:
        if len(word) > len(longest):
            longest = word
    return longest

