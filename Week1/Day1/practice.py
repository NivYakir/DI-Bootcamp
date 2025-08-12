from collections import Counter
import os

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


t1 = Text(my_text)
print(t1.word_frequency('people'))
print(t1.most_common_word())
print(t1.unique_words())