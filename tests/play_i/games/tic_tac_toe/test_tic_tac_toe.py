import unittest

from play_i.games.tic_tac_toe.tic_tac_toe import TicTacToe
from play_i.player.random_player import RandomPlayer


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.t = TicTacToe()
        self.t.headless()
        self.t.add_player(RandomPlayer())
        self.t.add_player(RandomPlayer())
        self.t.setup()

    def test_horizontal_line(self):
        self.t._play_area[0][0] = 'X'
        self.t._play_area[0][1] = 'X'
        self.t._play_area[0][2] = 'X'

        self.t.check_game_over()
        self.assertTrue(self.t.game_over())
        self.t.end_game()
        self.assertTrue(self.t.end_state == 'player X wins')

    def test_vertical_line(self):
        self.t._play_area[0][0] = 'X'
        self.t._play_area[1][0] = 'X'
        self.t._play_area[2][0] = 'X'

        self.t.check_game_over()
        self.assertTrue(self.t.game_over())
        self.t.end_game()
        self.assertTrue(self.t.end_state == 'player X wins')

    def test_diagonal(self):
        self.t._play_area[0][0] = 'X'
        self.t._play_area[1][1] = 'X'
        self.t._play_area[2][2] = 'X'

        self.t.check_game_over()
        self.assertTrue(self.t.game_over())
        self.t.end_game()
        self.assertTrue(self.t.end_state == 'player X wins')

    def test_draw(self):
        self.t._play_area[0][0] = 'X'
        self.t._play_area[0][1] = 'X'
        self.t._play_area[0][2] = 'O'

        self.t._play_area[1][0] = 'O'
        self.t._play_area[1][1] = 'O'
        self.t._play_area[1][2] = 'X'

        self.t._play_area[2][0] = 'X'
        self.t._play_area[2][1] = 'O'
        self.t._play_area[2][2] = 'X'

        self.t.check_game_over()
        self.assertTrue(self.t._draw)
        self.t.end_game()
        self.assertTrue(self.t.end_state == 'draw')

    def test_actions(self):
        options = self.t.options()
        expected_options = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assert_options_equal(expected_options, options)

        self.t._play_area[0][0] = 'X'
        self.t._play_area[0][1] = 'O'
        options = self.t.options()
        expected_options = [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
        self.assert_options_equal(expected_options, options)

    def assert_options_equal(self, expected_options, options):
        self.assertEqual(len(expected_options), len(options))
        for option in options:
            found = False
            for expected_option in expected_options:
                if (expected_option[0] == option[0]) and (expected_option[1] == option[1]):
                    found = True

            self.assertTrue(found)
