from typing import List, Dict
from collections import defaultdict

from games.common import Card, Rank, Suit


class Hand:
    """
    Класс руки для блек-джека.

    Хранит карты отдельной руки игрока.

    Attributes
    ----------
    cards: List[Card]
        список всех карт в руке
    """
    def __init__(self, *cards: Card):
        self.cards: List[Card] = list()

        self._ranks: Dict[Rank, int] = defaultdict(int)
        self._suits: Dict[Suit, int] = defaultdict(int)

        self.extend(*cards)

    def __repr__(self):
        return f"<{self.__class__.__name__}(cards={self.cards!r})>"

    def __str__(self):
        return f"{self.cards}"

    def __iter__(self):
        return iter(self.cards)

    def _update(self, card: Card):
        """
        Обновляет словари :attr:`ranks` и :attr:`suits` при добавлении новой карты
        в руку.

        :param card: Card, добавленная карта
        """
        self._ranks[card.rank] += 1
        self._suits[card.suit] += 1

    def append(self, card: Card):
        """
        Добавляет новую карту в руку.

        :param card: Card, добавляемая карта
        """
        self.cards.append(card)
        self._update(card)

    def extend(self, *cards: Card):
        """
        Добавляет в конец списка все переданные карты через метод :method:`append`.

        :param cards: ...Card, добавляемая карта
        """
        for card in cards:
            self.append(card)

    def get_pairs(self) -> List[Rank]:
        """
        Возвращает список достоинств тех карт, которые в руке образуют по крайней мере пару.

        :return: List[Rank], список достоинств
        """
        return [k for k, v in self._ranks.items() if v >= 2]
