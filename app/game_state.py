from pprint import pprint

class GameState:
    """Class to store and load game state"""

    def __init__(self):
        self.state = {
            'player_score': 0,
            'comp_score': 0,
            'ties': 0
        }
    
    def print_scoreboard(self):
        print(">>> SCOREBOARD <<<")
        pprint(self.state)
        print()
