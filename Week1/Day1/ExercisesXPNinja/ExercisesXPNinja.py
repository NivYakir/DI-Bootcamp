# Exercise 3: Outputs

3 <= 3 < 9 # True
3 == 3 == 3 # True
bool(0) # False
bool(5 == "5") # False
bool(4 == 4) == bool("4" == "4") # True
bool(bool(None)) # False

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x) # x is True
print("y is", y) # y is False
print("a:", a) # a: 5
print("b:", b) # b: 10

# Exercise 4: How Many Characters in a Sentence?

my_text = """"Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco
laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit
esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

print(len(my_text))

# Exercise 5: Longest Word without a Specific Character

longest = ""

while True:
    sentence = input("Please type the longest sentence you can. If you would like to quit, simply type 'quit': ")
    if sentence.upper() == "QUIT":
        print("You have quit the challenge.")
        break
    if "A" in sentence.upper():
        print("Your sentence has the letter A")
        continue
    if len(sentence) > len(longest):
        longest = sentence
        print("Congratulations! You have entered a new longest sentence.")