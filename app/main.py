# Application execution starts from this file

import pprint
import random

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

ACTIONS = list(RULES.keys())

COMMANDS = [
    'exit'
]


def print_instructions():
    """Print game instructions to user"""

    print("Welcome to RPSLS!")
    print(INSTRUCTIONS)
    print(f"Valid game commands are: {COMMANDS}\n")
    print(f"Your possible actions are: {ACTIONS}\n")
    print("Each action wins against two other actions as follows:")
    pprint.pprint(RULES)
    print("\nLet the fun begin!\n")


def print_game_summary():
    """Print summary of game results to user"""

    print("\nThanks for playing, bye!\n")


def computer_action():
    """Selects an action for the computer player"""

    return ACTIONS[random.randint(0, len(ACTIONS) - 1)]


def evaluate_round(user_action, comp_action):
    """Compare user and computer actions, determine who won the round"""

    if user_action == comp_action:
        print("Tie!")
    elif comp_action in RULES[user_action]:
        print("You won the round!")
    elif user_action in RULES[comp_action]:
        print("The computer won the round!")
    else:
        raise Exception("INVALID GAME STATE")


def play_round():
    """Execute a single round of the game"""

    user_action = input("\nChoose your action: ").lower()

    while user_action not in ACTIONS + COMMANDS:
        user_action = input("\nPlease choose a valid action or command: ").lower()

    print(f"You chose: {user_action}")
    
    if user_action == "exit":
        return 0
    
    comp_action = computer_action()
    print(f"Computer chose: {comp_action}")

    evaluate_round(user_action, comp_action)
    
    print()
    return 1


def main():
    """Main application loop"""

    print_instructions()

    while play_round() == 1:
        pass

    print_game_summary()



if __name__ == "__main__":
    main()

