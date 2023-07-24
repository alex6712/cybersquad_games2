from typing import List, Dict
from collections import defaultdict

from app.games.common import Card, Rank, Suit


class Hand:
    """Класс руки для блек-джека.

    Хранит карты отдельной руки игрока.

    Attributes
    ----------
    cards : List[Card]
        Список всех карт в руке.
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
        """Обновляет словари ``ranks`` и ``suits`` при добавлении новой карты в руку.

        Parameters
        ----------
        card : Card
            Добавленная карта.
        """
        self._ranks[card.rank] += 1
        self._suits[card.suit] += 1

    def append(self, card: Card):
        """Добавляет новую карту в руку.

        Parameters
        ----------
        card : Card
            Добавляемая карта.
        """
        self.cards.append(card)
        self._update(card)

    def extend(self, *cards: Card):
        """Добавляет в конец списка все переданные карты через метод ``append``.

        Note
        ----
        Все элементы ``*cards`` (т.е. все переданные аргументы) должны быть типа `Card`.

        Parameters
        ----------
        cards
            Произвольное количество карт.
        """
        for card in cards:
            self.append(card)

    def get_pairs(self) -> List[Rank]:
        """Возвращает список достоинств тех карт, которые в руке образуют по крайней мере пару.

        Returns
        -------
        ranks : List[Rank]
            Список достоинств всех карт, образующих по крайней мере пару.
        """
        return [rank for rank, amount in self._ranks.items() if amount >= 2]
