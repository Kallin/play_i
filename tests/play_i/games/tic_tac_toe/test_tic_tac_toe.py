import unittest

from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.random_player import RandomPlayer


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.t = TicTacToe()
        self.t.headless()
        self.t.add_player(RandomPlayer())
        self.t.add_player(RandomPlayer())

    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def test_horizontal_line(self):
        pass

    def test_vertical_line(self):
        pass

    def test_diagonals(self):
        pass

    def test_draw(self):
        pass

    def test_victory(self):
        pass

    def test_actions(self):
        pass

    def testLine(self):
        self.t.play()
