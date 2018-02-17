from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
import play_i.player.console_player
import play_i.player.random_player
from play_i.player.console_player import ConsolePlayer
from play_i.player.min_max_player import MinMaxPlayer


def play():
    t = TicTacToe()

    # this sets up the game to use random players
    # PlayerUtils.configure_random_players(t)

    # lets create a manually controlled player
    # t.add_player(player.minmax =Min())
    t.add_player(ConsolePlayer())
    t.add_player(MinMaxPlayer())

    # will have to create some playersa

    t.play()
