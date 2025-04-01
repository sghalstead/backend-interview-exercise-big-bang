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
    print("Welcome to RPSLS!")
    print(INSTRUCTIONS)
    print(f"Your possible actions are: {list(RULES.keys())}\n")
    print("Each action wins against two other actions as follows:")
    pprint.pprint(RULES)
    print("\nLet the fun begin!\n")

def main():
    """Main application loop"""

    print_instructions()

    while True:
        user_input = input("\nChoose your action: ").lower()
        print(f"You chose: {user_input}\n")

        if user_input == "exit":
            print("Thanks for playing, bye!")
            break


if __name__ == "__main__":
    main()

