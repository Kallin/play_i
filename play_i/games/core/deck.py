from random import shuffle


class Deck:

    def __init__(self):
        super().__init__()
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def size(self):
        return len(self.cards)

    def card_count(self, card_clazz):
        return len([card for card in self.cards if card.__class__ == card_clazz])

    def shuffle(self):
        shuffle(self.cards)

    def find_and_draw_card(self, matcher):
        card = next(card for card in self.cards if matcher(card))
        self.cards.remove(card)
        return card

    def draw_card(self):
        return self.cards.pop()



class Card:

    def __init__(self):
        super
