import unittest

from play_i.games.jaipur.jaipur import Jaipur


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.j = Jaipur()

    def test_component_counts(self):
        self.assertEqual(self.j.deck.size, 55)

        self.assertEqual(self.j.deck.camel_count, 11)
        self.assertEqual(self.j.deck.diamond_count, 6)
        self.assertEqual(self.j.deck.gold_count, 6)
        self.assertEqual(self.j.deck.silver_count, 6)
        self.assertEqual(self.j.deck.cloth_count, 8)
        self.assertEqual(self.j.deck.spice_count, 8)
        self.assertEqual(self.j.deck.leather_count, 10)

        self.assertEqual(self.j.bonus_tokens.size, 18)

        self.assertEqual(self.j.goods_tokens.size, 38)

        self.assertTrue(self.j.camel_token)

        self.assertEqual(self.j.diamond_values, [7, 7, 5, 5, 5])
        self.assertEqual(self.j.gold_values, [6, 6, 5, 5, 5])
        self.assertEqual(self.j.silver_values, [5, 5, 5, 5, 5])
        self.assertEqual(self.j.cloth_values, [5, 3, 3, 2, 2, 1, 1])
        self.assertEqual(self.j.spice_values, [5, 3, 3, 2, 2, 1, 1])
        self.assertEqual(self.j.leather_values, [4, 3, 2, 1, 1, 1, 1, 1, 1])
        self.assertEqual(self.j.camel_token.value, 5)

        self.assertEqual(self.j.camel_token.value, 5)

        self.assertEqual(self.j.five_tokens.size, 5)
        self.assertEqual(self.j.four_tokens.size, 6)
        self.assertEqual(self.j.three_tokens.size, 7)

        self.assertEqual(self.j.five_token_values, [10, 10, 9, 8, 8])
        self.assertEqual(self.j.four_token_values, [6, 6, 5, 5, 4, 4])
        self.assertEqual(self.j.three_token_values, [3, 3, 2, 2, 2, 1, 1])
