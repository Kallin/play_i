from play_i.games.core.base_game import BaseGame
from play_i.games.core.deck import Deck, Card


class Jaipur(BaseGame):

    def __init__(self):
        super().__init__()
        self.create_components()

    def create_components(self):
        self.create_deck()
        self.create_tokens()

    def create_deck(self):
        deck = Deck()
        for i in range(11):
            deck.add_card(CamelCard())
        for i in range(6):
            deck.add_card(DiamondCard())
        for i in range(6):
            deck.add_card(GoldCard())
        for i in range(6):
            deck.add_card(SilverCard())
        for i in range(8):
            deck.add_card(ClothCard())
        for i in range(8):
            deck.add_card(SpiceCard())
        for i in range(10):
            deck.add_card(LeatherCard())

        self.play_area['deck'] = deck

    def create_tokens(self):
        self.create_bonus_tokens()
        self.create_camel_token()
        self.create_goods_tokens()

    def set_defaults(self):
        self.player_count = 2

    def supported_player_counts(self):
        return 2, 2

    def name(self):
        return 'Jaipur'

    def setup(self):
        market = self.play_area['market'] = []

        deck = self.play_area['deck']
        # put 3 camel cards in 'market'
        for i in range(3):
            market.append(deck.find_and_draw_card(lambda x: isinstance(x, CamelCard)))

        # shuffle deck
        deck.shuffle()

        player_1_area = self.play_area['player_1'] = {}
        player_2_area = self.play_area['player_2'] = {}

        # deal 5 cards to each player
        for player_area in [player_1_area, player_2_area]:
            hand = player_area['hand'] = []
            camels = player_area['camels'] = []
            for i in range(5):
                # todo: get this logic into hand class maybe?
                card = deck.draw_card()
                if isinstance(card, CamelCard):
                    camels.append(card)
                else:
                    hand.append(card)

        for i in range(2):
            market.append(deck.draw_card())

    def begin(self):
        pass

    def copy(self):
        pass

    def bonus_tokens(self):
        return self.five_tokens + self.four_tokens + self.three_tokens

    def create_bonus_tokens(self):
        self.five_tokens = self.create_five_tokens()
        self.four_tokens = self.create_four_tokens()
        self.three_tokens = self.create_three_tokens()

    def create_five_tokens(self):
        tokens = []
        tokens.append(FiveToken(10))
        tokens.append(FiveToken(10))
        tokens.append(FiveToken(9))
        tokens.append(FiveToken(8))
        tokens.append(FiveToken(8))
        return tokens

    def create_four_tokens(self):
        tokens = []
        tokens.append(FourToken(6))
        tokens.append(FourToken(6))
        tokens.append(FourToken(5))
        tokens.append(FourToken(5))
        tokens.append(FourToken(4))
        tokens.append(FourToken(4))
        return tokens

    def create_three_tokens(self):
        tokens = []
        tokens.append(ThreeToken(3))
        tokens.append(ThreeToken(3))
        tokens.append(ThreeToken(2))
        tokens.append(ThreeToken(2))
        tokens.append(ThreeToken(2))
        tokens.append(ThreeToken(1))
        tokens.append(ThreeToken(1))
        return tokens

    def create_camel_token(self):
        pass

    def goods_tokens(self):
        return self.diamond_tokens + self.gold_tokens + self.silver_tokens \
               + self.cloth_tokens + self.spice_tokens + self.leather_tokens

    def create_goods_tokens(self):
        self.diamond_tokens = self.create_diamond_tokens()
        self.gold_tokens = self.create_gold_tokens()
        self.silver_tokens = self.create_silver_tokens()
        self.cloth_tokens = self.create_cloth_tokens()
        self.spice_tokens = self.create_spice_tokens()
        self.leather_tokens = self.create_leather_tokens()
        self.camel_token = CamelToken(5)

    def create_diamond_tokens(self):
        tokens = []
        tokens.append(DiamondToken(7))
        tokens.append(DiamondToken(7))
        tokens.append(DiamondToken(5))
        tokens.append(DiamondToken(5))
        tokens.append(DiamondToken(5))
        return tokens

    def create_gold_tokens(self):
        tokens = []
        tokens.append(GoldToken(6))
        tokens.append(GoldToken(6))
        tokens.append(GoldToken(5))
        tokens.append(GoldToken(5))
        tokens.append(GoldToken(5))
        return tokens

    def create_silver_tokens(self):
        tokens = []
        tokens.append(SilverToken(5))
        tokens.append(SilverToken(5))
        tokens.append(SilverToken(5))
        tokens.append(SilverToken(5))
        tokens.append(SilverToken(5))
        return tokens

    def create_cloth_tokens(self):
        tokens = []
        tokens.append(ClothToken(5))
        tokens.append(ClothToken(3))
        tokens.append(ClothToken(3))
        tokens.append(ClothToken(2))
        tokens.append(ClothToken(2))
        tokens.append(ClothToken(1))
        tokens.append(ClothToken(1))
        return tokens

    def create_spice_tokens(self):
        tokens = []
        tokens.append(SpiceToken(5))
        tokens.append(SpiceToken(3))
        tokens.append(SpiceToken(3))
        tokens.append(SpiceToken(2))
        tokens.append(SpiceToken(2))
        tokens.append(SpiceToken(1))
        tokens.append(SpiceToken(1))
        return tokens

    def create_leather_tokens(self):
        tokens = []
        tokens.append(LeatherToken(4))
        tokens.append(LeatherToken(3))
        tokens.append(LeatherToken(2))
        tokens.append(LeatherToken(1))
        tokens.append(LeatherToken(1))
        tokens.append(LeatherToken(1))
        tokens.append(LeatherToken(1))
        tokens.append(LeatherToken(1))
        tokens.append(LeatherToken(1))
        return tokens


class Token:

    def __init__(self, value):
        self.value = value


class DiamondToken(Token):
    pass


class GoldToken(Token):
    pass


class SilverToken(Token):
    pass


class ClothToken(Token):
    pass


class SpiceToken(Token):
    pass


class LeatherToken(Token):
    pass


class CamelToken(Token):
    pass


class FiveToken(Token):
    pass


class FourToken(Token):
    pass


class ThreeToken(Token):
    pass


class CamelCard(Card):
    pass


class DiamondCard(Card):
    pass


class GoldCard(Card):
    pass


class SilverCard(Card):
    pass


class ClothCard(Card):
    pass


class SpiceCard(Card):
    pass


class LeatherCard(Card):
    pass
