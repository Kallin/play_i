from collections import Counter

from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.player_utils import PlayerUtils

results = []
for _ in range(10000):
    t = TicTacToe()

    PlayerUtils.configure_random_players(t)

    t.play()

    end_state = t.end_state

    results.append(end_state)

print(Counter(results))
