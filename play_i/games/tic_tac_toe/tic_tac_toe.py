# So, we need to build TicTactoe using some core game classes
from play_i.games.core.base_game import BaseGame


class TicTacToe(BaseGame):

    # could be part of a generalized setup routine. figure out what parameters a game has and configure it.
    # there will be some common ones like '# of players', but also
    def supported_player_counts(self):
        return 2, 2

    def name(self):
        return 'Tic Tac Toe'



