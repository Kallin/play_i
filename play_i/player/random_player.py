import random

from play_i.player.player import Player


class RandomPlayer(Player):
    def make_choice(self, options):
        return random.choice(options)
