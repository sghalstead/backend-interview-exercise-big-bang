from pprint import pprint
import json
from pathlib import Path
from templates import SCOREBOARD


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

    DATA_STORE_FILE = 'game_state.json'

    def __init__(self):
        data_store = Path(self.DATA_STORE_FILE)
        if data_store.is_file():
            self.__read_state()
        else:
            self.state = dotdict({
                self.PLAYER_SCORE: 0,
                self.COMP_SCORE: 0,
                self.TIES: 0
            })


    def __del__(self):
        self.__write_state()


    def __write_state(self):
        with open(self.DATA_STORE_FILE, 'w') as file:
            file.write(json.dumps(self.state))


    def __read_state(self):
        with open(self.DATA_STORE_FILE) as file:
            self.state = dotdict(json.load(file))


    def print_scoreboard(self):
        print(SCOREBOARD.format(
            player_score=self.state.PLAYER_SCORE,
            computer_score=self.state.COMP_SCORE,
            ties=self.state.TIES
        ))
        print()


    def log_player_win(self):
        self.state.PLAYER_SCORE += 1


    def log_comp_win(self):
        self.state.COMP_SCORE += 1


    def log_tie(self):
        self.state.TIES += 1


    def restart(self):
        self.state.PLAYER_SCORE = 0
        self.state.COMP_SCORE = 0
        self.state.TIES = 0
        self.__write_state()

