from play_i.games.core.base_game import BaseGame
from play_i.games.tic_tac_toe.renderer import Renderer
from play_i.games.tic_tac_toe.headless_renderer import HeadlessRenderer


class TicTacToe(BaseGame):
    EMPTY_CELL = '-'
    X_CELL = 'X'
    O_CELL = 'O'

    def __init__(self):
        super().__init__()
        self.__renderer = Renderer()
        self.__player_count = None
        self._active_player = None
        self._player_x = None
        self._player_o = None
        self.__winner = None
        self._draw = None



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
        self.create_play_area()
        self._active_player = self._player_x
        self.__lines = self.build_lines()

    def __assign_players(self):
        self._player_x = self.players[0]
        self._player_o = self.players[1]

    def begin(self):
        self.__renderer.render_game_start()
        while True:
            self.__renderer.render_game(self)

            self.player_turn()

            self.check_game_over()

            if self.game_over():
                break

            self.swap_players()

        self.end_game()
        self.__renderer.render_game_over(self)

    def swap_players(self):
        if self.x_is_active():
            self._active_player = self._player_o
        else:
            self._active_player = self._player_x

    def player_turn(self):
        choice = self._active_player.make_choice(self.options(), game=self)
        self.apply_choice(choice)

    def create_play_area(self):
        # we need to represent play spaces generically.. a layout, or coordinate system.
        self._play_area = [[self.EMPTY_CELL for i in range(3)] for j in range(3)]

    def options(self):
        options = []
        for i, row in enumerate(self._play_area):
            for j, cell in enumerate(row):
                if cell == self.EMPTY_CELL:
                    options.append([i, j])

        return options

    def apply_choice(self, choice):
        if self.x_is_active():
            self.place_marker(choice, self.X_CELL)
        else:
            self.place_marker(choice, self.O_CELL)

    def x_is_active(self):
        return self._active_player == self._player_x

    def o_is_active(self):
        return self._active_player == self._player_o

    def place_marker(self, choice, marker):
        self._play_area[choice[0]][choice[1]] = marker

    def check_game_over(self):
        self.check_victory()
        if self.__winner is None:
            self.check_draw()

    def check_draw(self):
        all_spaces_used = True
        for row in self._play_area:
            for cell in row:
                if cell == self.EMPTY_CELL:
                    all_spaces_used = False
                    break
        if all_spaces_used:
            self._draw = True

    def x_victory(self, line):
        return self.x_is_active() and self.complete_line(line, self.X_CELL)

    def o_victory(self, line):
        return self.o_is_active() and self.complete_line(line, self.O_CELL)

    def check_victory(self):
        for line in self.__lines:
            if self.x_victory(line):
                self.__winner = self._player_x
                break
            elif self.o_victory(line):
                self.__winner = self._player_o
                break

    def complete_line(self, line, marker):
        for index in line:
            if self._play_area[index[0]][index[1]] != marker:
                return False

        return True

    def build_lines(self):
        lines = []

        self.add_rows(lines)
        self.add_columns(lines)
        self.add_diag_1(lines)
        self.add_diag_2(lines)

        return lines

    def add_diag_2(self, lines):
        line = []
        for i, row in enumerate(self._play_area):
            line.append([i, len(row) - i - 1])

        lines.append(line)

    def add_diag_1(self, lines):
        line = []
        for i, row in enumerate(self._play_area):
            line.append([i, i])

        lines.append(line)

    def add_straight_lines(self, lines, line_indexer):
        for i, row in enumerate(self._play_area):
            line = []
            for j, column in enumerate(row):
                line_indexer(line, i, j)

            lines.append(line)

    def column_indexer(self, line, i, j):
        line.append([j, i])

    def add_columns(self, lines):
        self.add_straight_lines(lines, self.column_indexer)

    def row_indexer(self, line, i, j):
        line.append([i, j])

    def add_rows(self, lines):
        self.add_straight_lines(lines, self.row_indexer)

    def game_over(self):
        return (self.__winner is not None) or self._draw

    def end_game(self):
        if self.__winner is not None:
            if self.__winner == self._player_x:
                self.end_state = 'player X wins'
            else:
                self.end_state = 'player O wins'
        else:
            self.end_state = 'draw'

    def copy(self):
        copy = TicTacToe()
        copy.__player_count = self.__player_count
        copy._active_player = self._active_player
        copy._player_x = self._player_x
        copy._player_o = self._player_o
        copy.__winner = self.__winner
        copy._draw = self._draw
        copy.players = self.players
        copy.__lines = self.__lines

        # can share state of everything except play area
        copy._play_area = [row[:] for row in self._play_area]

        return copy

    def headless(self):
        self.__renderer = HeadlessRenderer()
