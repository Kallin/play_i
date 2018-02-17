import random

from play_i.player.player import Player


class RandomPlayer(Player):
    def make_choice(self, options, game):
        return random.choice(options)
