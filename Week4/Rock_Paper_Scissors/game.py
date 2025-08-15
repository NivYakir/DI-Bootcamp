import random

class Game:
    def get_user_item(self):
        while True:
            try:
                user_input = input("Select (r)ock, (p)aper, or (s)cissors: ")
                if user_input not in ['r','p','s']:
                    raise ValueError("Invalid Input.")
                
                return user_input
            
            except Exception as e:
                print(f"Error: {e}")
    
    def get_computer_item(self):
        return random.choice(['r','p','s'])
    
    def get_game_result(self, user_item, comp_item):
        if (user_item == 'r' and comp_item == 's') or (user_item == 's' and comp_item == 'p') or (user_item == 'p' and comp_item == 'r'):
            return 'Win'
        elif user_item == comp_item:
            return 'Draw'
        else:
            return 'Lose'

    def play(self):
        dict_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        user_item = self.get_user_item()
        comp_item = self.get_computer_item()
        result = self.get_game_result(user_item, comp_item)

        print(f"You selected {dict_map[user_item]}. The computer selected {dict_map[comp_item]}. You {result}.")
        return result
