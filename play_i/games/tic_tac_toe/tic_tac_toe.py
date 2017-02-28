# So, we need to build TicTactoe using some core game classes

from play_i.games.core.base_game import BaseGame


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
        self.__winner = None
        self.__draw = None

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
        self.render_game_start()
        while True:
            self.render_game()

            self.player_turn()

            self.check_game_over()

            if self.game_over():
                break

            self.swap_players()

        self.render_game_over()

    def render_game_over(self):
        if self.__winner is not None:
            if self.__winner == self.__player_x:
                print('player X wins')
            else:
                print('player O wins')
        else:
            print('draw')

        print('\n')
        self.render_game()

    def render_game_start(self):
        print('starting game')

    def swap_players(self):
        if self.x_is_active():
            self.__active_player = self.__player_o
        else:
            self.__active_player = self.__player_x

    def player_turn(self):
        choice = self.__active_player.make_choice(self.options())
        self.apply_choice(choice)

    def render_game(self):
        self.print_grid()

    def __create_play_area(self):
        # we need to represent play spaces generically.. a layout, or coordinate system.
        self.play_area = [[self.EMPTY_CELL for i in range(3)] for j in range(3)]

    def options(self):
        options = []
        for i, row in enumerate(self.play_area):
            for j, cell in enumerate(row):
                if cell == self.EMPTY_CELL:
                    options.append([i, j])

        return options

    def print_grid(self):
        print('\n'.join(''.join(row) for row in self.play_area))
        print('\n')

    def apply_choice(self, choice):
        if self.x_is_active():
            self.place_marker(choice, self.X_CELL)
        else:
            self.place_marker(choice, self.O_CELL)

    def x_is_active(self):
        return self.__active_player == self.__player_x

    def place_marker(self, choice, marker):
        self.play_area[choice[0]][choice[1]] = marker

    def check_game_over(self):
        lines = []

        # rows
        for row in self.play_area:
            lines.append(row)

        # columns
        for i in range(3):
            lines.append([row[i] for row in self.play_area])

        # top-left to bottom-right
        diag_1 = []
        for i in range(3):
            diag_1.append(self.play_area[i][i])
        lines.append(diag_1)

        # top-right to bottom-left
        diag_2 = []
        for i in range(3):
            diag_2.append(self.play_area[i][2 - i])
        lines.append(diag_2)

        for line in lines:
            if all(cell == self.X_CELL for cell in line):
                self.__winner = self.__player_x
                break
            elif all(cell == self.O_CELL for cell in line):
                self.__winner = self.__player_o
                break

        all_spaces_used = True
        for row in self.play_area:
            for cell in row:
                if cell == self.EMPTY_CELL:
                    all_spaces_used = False
                    break

        if all_spaces_used:
            self.__draw = True

    def game_over(self):
        return (self.__winner is not None) or self.__draw
