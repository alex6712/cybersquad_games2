from typing import List

from games.blackjack import Hand


class Player:
    def __init__(self):
        self.hands: List[Hand] = list()

        self.money: int = 0
        self.bet: int = 0

    def bind_hand(self, hand: Hand):
        self.hands.append(hand)

    def split(self):
        pass
