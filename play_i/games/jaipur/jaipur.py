from play_i.games.core.base_game import BaseGame


class Jaipur(BaseGame):

    def __init__(self):
        super().__init__()

    def set_defaults(self):
        self.player_count = 2

    def supported_player_counts(self):
        return 2, 2

    def name(self):
        return 'Jaipur'

    def setup(self):
        pass

    def begin(self):
        pass

    def copy(self):
        pass
