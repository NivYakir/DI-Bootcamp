from game import Game

def get_user_menu_choice():
    while True:
        print("Menu:\n(g) Play a new game\n(x) Show scores and exit")
        user_input = input(": ")
        if user_input not in ['g', 'x']:
            print("Invalid Input. Select one of the below options: ")
            continue
        
        return user_input

def print_results(results):
    for k, v in results.items():
        print(f"You {k} {v} times!")
    
    print("\nThank you for playing!")


def main():
    results = {'won': 0, 'lost': 0, 'drew': 0}
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            g1 = Game()
            score = g1.play()
            if score == 'Win':
                results['won'] += 1
            elif score == 'Lose':
                results['lost'] += 1
            elif score == 'Draw':
                results['drew'] += 1
        
        else:
            print_results(results)
            break

main()


