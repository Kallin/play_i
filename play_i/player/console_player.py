import random

from play_i.player.player import Player


class ConsolePlayer(Player):
    def make_choice(self, options):
        print(options)
        choice = int(input('Choose the index of your move: '))
        return options[choice]
