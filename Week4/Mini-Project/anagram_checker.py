import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class AnagramChecker:
    '''This class can take a valid word in English and return all of its anagrams!'''
    def __init__(self):
        with open(f'{dir_path}/sowpods.txt', 'r', encoding='utf-8') as file:
            self.word_list = [line.strip() for line in file]
        
    def is_valid_word(self, word):
        '''Checks if the word exists'''
        return word.upper() in self.word_list
    
    def is_anagram(self, word1, word2):
        '''Checks if two given words are an anagram of one another'''
        w1 = word1.upper()
        w2 = word2.upper()
        return sorted(w1) == sorted(w2)
    
    def get_anagrams(self, word):
        '''Returns all of the anagrams of a given word'''
        word = word.upper()
        anagrams = []
        for target in self.word_list:
            if target != word and self.is_anagram(word, target):
                anagrams.append(target)
                
        return anagrams

