from pprint import pprint

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class GameState:
    """Class to store and load game state"""

    PLAYER_SCORE = "PLAYER_SCORE"
    COMP_SCORE = "COMP_SCORE"
    TIES = "TIES"


    def __init__(self):
        self.state = dotdict({
            self.PLAYER_SCORE: 0,
            self.COMP_SCORE: 0,
            self.TIES: 0
        })


    def print_scoreboard(self):
        print(">>> SCOREBOARD <<<")
        pprint(self.state)
        print()


    def log_player_win(self):
        self.state.PLAYER_SCORE += 1


    def log_comp_win(self):
        self.state.COMP_SCORE += 1


    def log_tie(self):
        self.state.TIES += 1
