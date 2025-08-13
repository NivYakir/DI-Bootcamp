# DailyChallenge JSON/IO
import os
import string
import re
from collections import Counter

stop_words = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can't", "cannot", "could", "couldn't",
    "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during",
    "each", "few", "for", "from", "further", "had", "hadn't", "has", "hasn't",
    "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here",
    "here's", "hers", "herself", "him", "himself", "his", "how", "how's", "i",
    "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it", "it's",
    "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself",
    "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought",
    "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than",
    "that", "that's", "the", "their", "theirs", "them", "themselves", "then",
    "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
    "this", "those", "through", "to", "too", "under", "until", "up", "very", "was",
    "wasn't", "we", "we'd", "we'll", "we're", "we've", "were", "weren't", "what",
    "what's", "when", "when's", "where", "where's", "which", "while", "who",
    "who's", "whom", "why", "why's", "with", "won't", "would", "wouldn't", "you",
    "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"
]

my_txt = "today, yesterday and tomorrow. They'll there was today a beach there was today a beach today!"
dir_path = os.path.dirname(os.path.realpath(__file__))
my_file = f"{dir_path}\\practice.txt"
print(my_file)

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


t1 = Text.from_file(my_file)
print(t1)

class TextModification(Text):
    def __init__(self, text):
        super().__init__(text)
    
    def remove_punctuation(self):
        result = ''.join(char for char in self.text if char not in string.punctuation)
        return result

    def remove_stop_words(self):
        filtered = [word for word in self.txt_list if word.lower() not in stop_words]
        result = ' '.join(word for word in filtered)
        return result
    
    def remove_special_characters(self):
        result = re.sub(r'[^A-Za-z0-9\s]', '', self.text)
        return result
        



# t1 = Text(my_txt)
# print(t1.most_common_word())
# print(t1.unique_words())

# t2 = TextModification(my_txt)
# print(t2.remove_stop_words())