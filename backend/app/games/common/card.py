import itertools
import random
from enum import Enum, EnumMeta
from typing import (
    Iterable,
    List,
    Any,
    AnyStr,
)


class _CommonEnumMeta(EnumMeta):
    """Мета класс базового ``Enum``.

    Нужен для того, чтобы установить соответствия между экземплярами ``Enum`` и любым из
    значений итерируемого объекта, а не с единственным.
    """

    def __init__(cls, class_name, bases, class_dict):
        super().__init__(class_name, bases, class_dict)

        for member in cls.__members__.values():
            values = member.value

            if not isinstance(values, Iterable) or isinstance(values, str):
                raise TypeError(f"{member.name} = {values!r}, should be iterable, not {type(values)}!")

            for alias in values:
                if isinstance(alias, str):
                    alias = alias.upper()
                cls._value2member_map_.setdefault(alias, member)

    def __call__(cls, value, **kwargs):
        """Возвращает соответствующий экземпляр с любым из перечисленных значений.

        Если значения содержат текстовые типы, они будут искаться без учета регистра.

        Parameters
        ----------
        value : `Any`
            Значение ``Enum``

        Returns
        -------
        enum : `Any`
            Экземпляр по значению
        """
        if isinstance(value, str):
            value = value.upper()

        return super().__call__(value)


class CommonEnum(Enum, metaclass=_CommonEnumMeta):
    """Обобщённый базовый класс Enum.
    """

    def __str__(self):
        return str(self._value_[0])

    @classmethod
    def get_all(cls) -> List[Any]:
        """Возвращает список всех представлений Enum.

        Returns
        -------
        aliases : `List[Any]`
            Список всех представлений
        """
        return list(cls)

    @classmethod
    def make_random(cls) -> Any:
        """Возвращает случайное представление Enum.

        Returns
        -------
        alias : `Any`
            Случайное представление
        """
        return random.choice(cls.get_all())


class Suit(CommonEnum):
    """Enum класс с мастями карт.

    Поддерживает сравнение мастей. Масти записаны в порядке возрастания.
    """
    CLUBS = "♣", "c", "clubs"
    DIAMONDS = "♦", "d", "diamonds"
    HEARTS = "♥", "h", "hearts"
    SPADES = "♠", "s", "spades"


class Rank(CommonEnum):
    """Enum класс с достоинствами карт.

    Поддерживает сравнение достоинств. Достоинства записаны в порядке возрастания.
    """
    DEUCE = "2", 2
    THREE = "3", 3
    FOUR = "4", 4
    FIVE = "5", 5
    SIX = "6", 6
    SEVEN = "7", 7
    EIGHT = "8", 8
    NINE = "9", 9
    TEN = "T", 10
    JACK = ("J",)
    QUEEN = ("Q",)
    KING = ("K",)
    ACE = "A", 1

    @classmethod
    def difference(cls, first, second) -> int:
        """Возвращает целочисленную разницу между достоинством карт.

        Parameters
        ----------
        first : :obj:`Rank`
            Достоинство первой карты
        second : :obj:`Rank`
            Достоинство второй карты

        Returns
        -------
        difference : `int`
            Разница между достоинствами карт
        """
        first, second = cls(first), cls(second)
        rank_list = list(cls)
        return abs(rank_list.index(first) - rank_list.index(second))


class _CardMeta(type):
    """Мета класс инициализации класса игральных карт.

    Используется по большей части для кеширования всех возможных карт в атрибут _all_cards.
    """

    def __new__(metacls, class_name, bases, class_dict):
        """Кешируем все возможные комбинации достоинства и масти (= все возможные игральные карты) и
        сохраняем в атрибут класса _all_cards.

        Parameters
        ----------
        class_name : `AnyStr`
            Идентификатор класса
        bases : `tuple[type, ...]`
            Базовые классы иерархии
        class_dict : `dict[Any, Any]`
            __dict__ класса

        Returns
        -------
        class : `Any`
            Класс, создаваемый с помощью этого мета класса
        """
        cls = super(_CardMeta, metacls).__new__(metacls, class_name, bases, class_dict)
        cls._all_cards = list(
            cls(f"{rank}{suit}") for rank, suit in itertools.product(Rank, Suit)
        )
        return cls

    def __iter__(cls):
        return iter(cls._all_cards)


class Card(metaclass=_CardMeta):
    """Общий (распространённый) класс игральной карты.

    Содержит в себе информацию о достоинстве и масти карты.

    Attributes
    ----------
    rank: Rank
        достоинство карты
    suit: Suit
        масть карты
    """

    def __init__(self, card: Iterable | AnyStr):
        if len(card) != 2:
            raise ValueError(f"\"card\" argument must be iterable or string of length 2: {card!r}")

        self.rank: Rank = Rank(card[0])
        self.suit: Suit = Suit(card[1])

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.rank == other.rank and self.suit == other.suit
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ is not other.__class__:
            return NotImplemented

        if self.rank == other.rank:
            return self.suit < other.suit

        return self.rank < other.rank

    def __repr__(self):
        return f"<{self.__class__.__name__}(rank={self.rank!r}, suit={self.suit!r})>"

    def __str__(self):
        return f"{self.rank}{self.suit}"

    @classmethod
    def make_random(cls) -> "Card":
        """Возвращает случайную карту.

        Returns
        -------
        card : `Card`
            Случайная карта
        """
        new = object.__new__(cls)
        new.rank = Rank.make_random()
        new.suit = Suit.make_random()

        return new
