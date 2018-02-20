import unittest
from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.min_max_player import MinMaxPlayer
from play_i.player.console_player import ConsolePlayer
from play_i.player.random_player import RandomPlayer


class TestTicTacToe(unittest.TestCase):

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def testLine(self):
        # test
        t = TicTacToe()
        t.headless()
        t.add_player(RandomPlayer())
        t.add_player(RandomPlayer())
        t.play()
