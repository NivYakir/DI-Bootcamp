 # Exercise 1: Random Sentence Generator

dir_path = os.path.dirname(os.path.realpath(__file__))

def get_words_from_file(path):
    with open(f'{path}/words.txt', 'r', encoding='utf-8') as f:
        word_list = f.readlines()
        result = []
        for line in word_list:
            line = line.strip()
            result.append(line)
        return result

def get_random_sentence(num):
    words = get_words_from_file(dir_path)
    random_words = [random.choice(words) for _ in range(num)]

    result = ' '.join(word.lower() for word in random_words) + '.'
    return result

def main():
    print("This function will generate a random sentence of your desired length.")
    while True:
        try:
            # Get user input and check for non-integer values.
            length_input = input("How many words do you want in your sentence? Choose a number between 2 and 20:\n")
            length = int(length_input)
            
            # Validate the input number.
            if length in range(2, 21):
                sentence = get_random_sentence(length)
                print(f"\nYour random sentence is:\n{sentence}")
                break  # Exit the loop after a valid sentence is generated.
            else:
                print("Invalid input. The number must be between 2 and 20 (inclusive). Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

main()