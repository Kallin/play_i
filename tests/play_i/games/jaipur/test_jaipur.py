import unittest

from play_i.games.jaipur import Jaipur, CamelCard, DiamondCard, LeatherCard, SpiceCard, ClothCard, SilverCard, \
    GoldCard

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.j = Jaipur()

    def test_component_counts(self):
        # todo: should probably include all of these components in the play area

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

    # todo: should have a fluent cli
    # able to build up an action
    # then prompt 'are you sure'
    # also be able to backup action one step at a time

    def test_initial_options(self):
        jaipur = self.j
        jaipur.setup()

        player_1 = jaipur.player(1)
        player_2 = jaipur.player(2)

        market = jaipur.play_area['market'] = []

        player_area = jaipur.play_area['player_1'] = {}
        hand = player_area['hand'] = []
        camels = player_area['camels'] = []

        hand += [GoldCard, DiamondCard, LeatherCard]
        camels += [CamelCard, CamelCard]
        market += [CamelCard, CamelCard, CamelCard, DiamondCard, LeatherCard]

        player_1_options = jaipur.options(player_1)
        player_2_options = jaipur.options(player_2)

        self.assertEqual(len(player_2_options), 0)

        # options: sell, take 1, exchange, take camels
        self.assertEqual(len(player_1_options), 4)

        option_keys = [x.label for x in player_1_options]
        for key in ['sell', 'take camels', 'take one card', 'replace cards']:
            self.assertTrue(key in option_keys)

        sell_option = next(option for option in player_1_options if option.label == 'sell')
        children = sell_option.sub_options()

    # def test_cil(self):

#
'''
todo: look at https://github.com/jonathanslenders/python-prompt-toolkit
todo: look at http://click.pocoo.org/5/
cli should behave like this at the beginning of the game:

out:
*Render state*
Action required for player 1.
Select an action:
1. Sell cards
2. Exchange cards
3. Take all the camels
4. Take one card
?. Render State

B) in:
> 1

out:
Configuring action 1, "Sell cards"..
Select a type of card to sell:
1. Diamonds (2)
2. Leather (3)
x. Cancel 'Sell Cards' action

in:
> 1

out:
Confirm action
- Sell
- Diamonds(2)

y. yes
n. no

in:
> y

out:
executed action
Action required for player 2




...

B)
in: 2

out:
Configuring action "exchange cards"
Select which cards to exchange
1.) Diamond (keep)
2.) Diamond (keep)
3.) Leather (keep)
4.) Leather (keep)
5.) Leather (keep)
0.) Done
x.) Cancel 'exchange cards' action'

in: 3,4

out:
Configuring action "exchange cards"
Select which cards to exchange
1.) Diamond (exchange)
2.) Diamond (keep)
3.) Leather (exchange)
4.) Leather (exchange)
5.) Leather (exchange)
0.) Done

in: 0

out:

Configuring action "exchange cards"
Select which 2 cards from market to take:
1.) Leather (leave)
2.) Leather (leave)
3.) Gold (leave)
4.) Gold (leave)
0.) Done (not available)

in:
3,4

out:

Configuring action "exchange cards"
Select which 3 cards from market to take:
1.) Leather (leave)
2.) Leather (leave)
3.) Gold (take)
4.) Gold (take)
0.) Done 

in:
0


Confirm action
- Exchange Cards
- Exchange Leatherx2
- Take Gold x2

y. yes
n. no

in:
y

out:
executed action
Action required for player 2


'''
