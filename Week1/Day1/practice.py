from collections import Counter
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
my_file = f"{dir_path}\\practice.txt"
my_text = 'hello hello hello hi hi how are you today hello hi hi'

class Text:
    def __init__(self, text):
        self.text = text

    @property
    def word_list(self):
        return self.text.split()
    
    def word_frequency(self, word):
        result = Counter(self.word_list)
        return result[word]
    
    def most_common_word(self):
        my_dict = {}
        for word in self.word_list:
            my_dict[word] = my_dict.get(word, 0) + 1
        
        return max(my_dict, key=my_dict.get)
    
    def unique_words(self):
        result = set(self.word_list)
        return list(result)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return cls(content)

    def __str__(self):
        return f"{self.text}"

text_instance = Text.from_file(f"{dir_path}/practice.txt")

print(text_instance)
