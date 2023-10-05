from play_i.player.player import Player


class ConsolePlayer(Player):
    def make_choice(self, options, game):
        text_options = (f"{ind}: {x}" for ind, x in enumerate(options))
        print(", ".join(text_options))
        choice = int(input("Choose the index of your move: "))
        return options[choice]
