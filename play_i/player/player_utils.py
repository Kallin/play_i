from play_i.player.random_player import RandomPlayer


class PlayerUtils:
    @classmethod
    def configure_random_players(cls, game):
        player_count = game.player_count
        for i in range(player_count):
            game.add_player(RandomPlayer())
