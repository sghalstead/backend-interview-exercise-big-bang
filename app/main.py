# Application execution starts from this file

from game import Game


def main():
    """Main application loop"""

    game = Game()

    game.print_instructions()

    while game.play_round() == 1:
        pass

    game.print_game_summary()



if __name__ == "__main__":
    main()

