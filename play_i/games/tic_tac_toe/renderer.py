class Renderer:
    def __init__(self):
        pass

    def render_game_over(self, game):
        print(game.end_state)

        print("\n")
        self.render_game(game)

    def render_game_start(self):
        print("starting game")

    def render_game(self, game):
        self.print_grid(game)

    def print_grid(self, game):
        print("\n".join("".join(row) for row in game._play_area))
        print("\n")
