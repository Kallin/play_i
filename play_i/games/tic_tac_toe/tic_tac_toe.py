# So, we need to build TicTactoe using some core game classes

from play_i.games.core.base_game import BaseGame


def game_over():
    pass


class TicTacToe(BaseGame):
    EMPTY_CELL = '-'
    X_CELL = 'X'
    O_CELL = 'O'

    def __init__(self):
        super().__init__()
        self.__player_count = None
        self.__active_player = None
        self.__player_x = None
        self.__player_o = None

    def set_defaults(self):
        self.player_count = 2

    # could be part of a generalized setup routine. figure out what parameters a game has and configure it.
    # there will be some common ones like '# of players', but also game specific ones

    def supported_player_counts(self):
        return 2, 2

    def name(self):
        return 'Tic Tac Toe'

    def setup(self):
        self.__assign_players()
        self.__create_play_area()
        self.__active_player = self.__player_x

    def __assign_players(self):
        self.__player_x = self._players[0]
        self.__player_o = self._players[1]

    def begin(self):
        print('starting game')
        while not game_over():
            self.print_grid()
            choice = self.__active_player.make_choice(self.options())
            self.apply_choice(choice)

            if self.x_is_active():
                self.__active_player = self.__player_o
            else:
                self.__active_player = self.__player_x

        print('game over')

    def __create_play_area(self):
        # we need to represent play spaces generically.. a layout, or coordinate system.
        self.play_area = [[self.EMPTY_CELL for i in range(3)] for j in range(3)]

    def options(self):
        # the options are going to be coordinates, like [0,0], [0,1] etc.

        options = []
        for i, row in enumerate(self.play_area):
            for j, cell in enumerate(row):
                if cell == self.EMPTY_CELL:
                    options.append([i, j])

        return options

    def print_grid(self):
        print('\n')
        print('\n'.join(''.join(row) for row in self.play_area))

    def apply_choice(self, choice):
        if self.x_is_active():
            self.place_marker(choice, self.X_CELL)
        else:
            self.place_marker(choice, self.O_CELL)

    def x_is_active(self):
        return self.__active_player == self.__player_x

    def place_marker(self, choice, marker):
        self.play_area[choice[0]][choice[1]] = marker
