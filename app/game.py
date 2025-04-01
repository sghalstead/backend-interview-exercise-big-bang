import pprint
import random
from game_state import GameState


class Game:
    """Class to contain data and methods to run game"""

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


    def __init__(self):
        self.state = GameState()


    def __computer_action(self):
        """Selects an action for the computer player"""

        return self.ACTIONS[random.randint(0, len(self.ACTIONS) - 1)]


    def __evaluate_round(self, user_action, comp_action):
        """Compare user and computer actions, determine who won the round"""

        if user_action == comp_action:
            print("Tie!")
        elif comp_action in self.RULES[user_action]:
            print("You won the round!")
        elif user_action in self.RULES[comp_action]:
            print("The computer won the round!")
        else:
            raise Exception("INVALID GAME STATE")


    def play_round(self):
        """Execute a single round of the game"""

        user_action = input("\nChoose your action: ").lower()

        while user_action not in self.ACTIONS + self.COMMANDS:
            user_action = input("\nPlease choose a valid action or command: ").lower()

        print(f"You chose: {user_action}")
        
        if user_action == "exit":
            return 0
        
        comp_action = self.__computer_action()
        print(f"Computer chose: {comp_action}")

        self.__evaluate_round(user_action, comp_action)
        
        print()
        return 1
    

    def print_instructions(self):
        """Print game instructions to user"""

        print("🪨 📜 ✂️ 🦎 🖖  Welcome to RPSLS!  🪨 📜 ✂️ 🦎 🖖")
        print(self.INSTRUCTIONS)
        print(f"Valid game commands are: {self.COMMANDS}\n")
        print(f"Your possible actions are: {self.ACTIONS}\n")
        print("Each action wins against two other actions as follows:")
        pprint.pprint(self.RULES)
        print("\nLet the fun begin!\n")


    def print_game_summary(self):
        """Print summary of game results to user"""

        print("\nThanks for playing, bye!\n")
