from anagram_checker import AnagramChecker

def main():
    checker = AnagramChecker()
    print("Welcome to the anagram checker!")
    while True:
        try: 
            user_input = input("Enter a word to receive all of its anagrams, or 'Q' to quit:\n")
            user_input = user_input.strip()
            if user_input.upper() == 'Q':
                print("You have quit the program.")
                break
            
            if len(user_input.split()) != 1:
                raise ValueError("Only one word can be checked at a time.")
            
            if not user_input.isalpha():
                raise ValueError("Only alphabetic characters are allowed.")
            
            if not checker.is_valid_word(user_input):
                raise TypeError("That is not a valid word in the English language.")
            
            result = checker.get_anagrams(user_input)

            if len(result) == 0:
                print(f"The word '{user_input}' has no anagrams!")
            else:
                print(f"Word: {user_input}\nAnagrams: {result}")
            
        except Exception as e:
            print(f"Input Error: {e}")

main()