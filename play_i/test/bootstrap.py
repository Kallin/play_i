from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.player_utils import PlayerUtils
from play_i.player.random_player import RandomPlayer
from play_i.player.console_player import ConsolePlayer

t = TicTacToe()

# this sets up the game to use random players
# PlayerUtils.configure_random_players(t)

# lets create a manually controlled player
t.add_player(RandomPlayer())
t.add_player(ConsolePlayer())


# will have to create some playersa

t.play()
