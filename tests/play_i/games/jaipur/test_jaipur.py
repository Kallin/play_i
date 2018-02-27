import unittest

from play_i.games.jaipur.jaipur import Jaipur, CamelCard, DiamondCard, LeatherCard, SpiceCard, ClothCard, SilverCard, \
    GoldCard


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.j = Jaipur()

    def test_component_counts(self):
        deck = self.j.play_area['deck']
        self.assertEqual(deck.size(), 55)

        self.assertEqual(deck.card_count(CamelCard), 11)
        self.assertEqual(deck.card_count(DiamondCard), 6)
        self.assertEqual(deck.card_count(GoldCard), 6)
        self.assertEqual(deck.card_count(SilverCard), 6)
        self.assertEqual(deck.card_count(ClothCard), 8)
        self.assertEqual(deck.card_count(SpiceCard), 8)
        self.assertEqual(deck.card_count(LeatherCard), 10)

        self.assertEqual(len(self.j.bonus_tokens()), 18)

        self.assertEqual(len(self.j.goods_tokens()), 38)

        self.assertTrue(self.j.camel_token)

        self.assertEqual([x.value for x in self.j.diamond_tokens], [7, 7, 5, 5, 5])
        self.assertEqual([x.value for x in self.j.gold_tokens], [6, 6, 5, 5, 5])
        self.assertEqual([x.value for x in self.j.silver_tokens], [5, 5, 5, 5, 5])
        self.assertEqual([x.value for x in self.j.cloth_tokens], [5, 3, 3, 2, 2, 1, 1])
        self.assertEqual([x.value for x in self.j.spice_tokens], [5, 3, 3, 2, 2, 1, 1])
        self.assertEqual([x.value for x in self.j.leather_tokens], [4, 3, 2, 1, 1, 1, 1, 1, 1])

        self.assertEqual(self.j.camel_token.value, 5)

        self.assertEqual(len(self.j.five_tokens), 5)
        self.assertEqual(len(self.j.four_tokens), 6)
        self.assertEqual(len(self.j.three_tokens), 7)

        self.assertEqual([x.value for x in self.j.five_tokens], [10, 10, 9, 8, 8])
        self.assertEqual([x.value for x in self.j.four_tokens], [6, 6, 5, 5, 4, 4])
        self.assertEqual([x.value for x in self.j.three_tokens], [3, 3, 2, 2, 2, 1, 1])

    def test_starting_conditions(self):
        self.j.setup()

        for player_key in ['player_1', 'player_2']:
            player = self.j.play_area[player_key]
            hand = player['hand']
            camels = player['camels']
            self.assertEqual(len(hand) + len(camels), 5)

        market = self.j.play_area['market']
        self.assertEqual(len(market), 5)
