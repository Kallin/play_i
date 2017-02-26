class BaseGame:

    def __init__(self):
        self.set_defaults()
        self._players = []

    def set_defaults(self):
        raise Exception('implement me')

    def name(self):
        raise Exception('implement me')

    def setup(self):
        raise Exception('implement me')

    def supported_player_counts(self):
        raise Exception('implement me')

    def begin(self):
        raise Exception('implement me')

    # def play(self):
    #     counts = self.supported_player_counts()
    #     selected_count = input("How many players, between {} and {}?\n".format(counts[0], counts[1]))
    #     print("beginning to play {} with {} players.\n".format(self.name(), selected_count))

    def play(self):
        self.setup()
        self.begin()

        # choose next player, have them select an option..
        pass

    def add_player(self, player):
        self._players.append(player)





