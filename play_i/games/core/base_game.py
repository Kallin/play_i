from player.player import Player


class BaseGame:
    def __init__(self):
        self.player_count = 0
        self.set_defaults()
        self.players = []
        self.play_area = {}

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

    def copy(self):
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

    def add_players(self, player_count):
        for x in range(player_count):
            self.player_count += 1
            self.players.append(Player())

    def add_player(self, player):
        self.player_count += 1
        player.number = self.player_count
        self.players.append(player)

    def player(self, player_num):
        return self.players[player_num - 1]
