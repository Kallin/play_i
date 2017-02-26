from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.player_utils import PlayerUtils

t = TicTacToe()

PlayerUtils.configure_random_players(t)

# will have to create some players

t.play()
