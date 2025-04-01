# Application execution starts from this file

import pprint

INSTRUCTIONS = """
>> USER INSTRUCTIONS <<
At any time type "exit" to exit the game.
"""

RULES = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock']
}


def print_instructions():
    """Print game instructions to user"""

    print("Welcome to RPSLS!")
    print(INSTRUCTIONS)
    print(f"Your possible actions are: {list(RULES.keys())}\n")
    print("Each action wins against two other actions as follows:")
    pprint.pprint(RULES)
    print("\nLet the fun begin!\n")


def print_game_summary():
    """Print summary of game results to user"""

    print("Thanks for playing, bye!")


def play_round():
    """Execute a single round of the game"""
    
    user_input = input("\nChoose your action: ").lower()
    print(f"You chose: {user_input}\n")

    if user_input == "exit":
        return 0
    
    return 1


def main():
    """Main application loop"""

    print_instructions()

    while play_round() == 1:
        pass

    print_game_summary()



if __name__ == "__main__":
    main()

