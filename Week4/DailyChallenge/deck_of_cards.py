# # Daily Challenge
import random

# Exercise 1: Quiz

# 1. A class is a template or blueprint for creating objects. 
# 2. An instance is an object that is created from a specific class.
# 3. The bundling of data (attributes) and methods (functions) into a single unit - a class.
# 4. Abstraction is hiding unecessary details and only giving access to essential features from an object.
# 5. Inheritence is when a class can use the properties and methods of another class.
# 6. Multiple inheritence is when a child class inherits the methods and properties of multiple classes.
# 7. Polymorphism is a function that has the same number under different classes/objects but behaves differently.
# 8. MRO is the order in which Python looks for a method or attribute when you call it on an object.

# Exercise 2: Deck of Cards

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.suit}: {self.value}"


class Deck:
    def __init__(self):
        deck = []
        valid_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        valid_value = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        for suit in valid_suits:
            for value in valid_value:
                deck.append(Card(suit, value))
    
        self.deck = deck
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        return self
    
    def deal(self):
        c = random.choice(self.deck)
        self.deck.remove(c)
        return f"DEALT CARD: {c}"

    def __str__(self):
        return '\n'.join(str(c) for c in self.deck)