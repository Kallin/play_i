class BaseGame:
    def doit(self):
        print('doing it!')

    def name(self):
        raise Exception('implement me')

    def supported_player_counts(self):
        raise Exception('implement me')

    def play(self):
        counts = self.supported_player_counts()
        selected_count = input("How many players, between {} and {}?\n".format(counts[0], counts[1]))
        print("beginning to play {} with {} players.\n".format(self.name(), selected_count))
