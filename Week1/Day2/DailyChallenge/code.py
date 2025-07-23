import random

my_sentence = input("Please enter a string that is exactly 10 characters long: ")

if len(my_sentence) < 10:
    print("String not long enough")
elif len(my_sentence) > 10:
    print("String too long")
else:
    print("Perfect string")
    print(my_sentence[0] + my_sentence[-1])
    builder = ""
    for letter in my_sentence:
        builder += letter
        print(builder)
    list_sentence = list(my_sentence)
    random.shuffle(list_sentence)
    shuffled = ''.join(list_sentence)
    print(shuffled)