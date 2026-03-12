from abc import ABC, abstractmethod
from typing import Callable, Optional


class Organizm(ABC):

    def __init__(self, x: int, y: int, orgid: str, imie: str, sila: int, inicjatywa: int,
                 print_log: Callable[[str], None], wiek: int = 0):
        self._id = orgid
        self._imie = imie
        self._x = x
        self._y = y
        self._sila = sila
        self._inicjatywa = inicjatywa
        self._wiek = wiek
        self._print_log = print_log
        self._rozsiane = False
        self._rozmnoz = False
        self._zolwodparlatak = False

    def print_log(self, message: str):
        self._print_log(message)

    @property
    def id(self) -> str:
        return self._id

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    @property
    def sila(self) -> int:
        return self._sila

    @sila.setter
    def sila(self, value: int):
        self._sila = value

    @property
    def inicjatywa(self) -> int:
        return self._inicjatywa

    @property
    def imie(self) -> str:
        return self._imie

    @property
    def rozsiane(self) -> bool:
        return self._rozsiane

    @property
    def rozmnoz(self) -> bool:
        return self._rozmnoz

    @property
    def zolwodparlatak(self) -> bool:
        return self._zolwodparlatak


    @property
    def wiek(self) -> int:
        return self._wiek

    @wiek.setter
    def wiek(self, value: int):
        self._wiek = value

    def begin_turn(self):
        self._rozsiane = False
        self._rozmnoz = False
        self._zolwodparlatak = False

    def end_turn(self):
        self.wiek += 1

    def kolizja_defend(self, attacker: 'Organizm', plansza, szerokosc: int, wysokosc: int) -> Optional['Organizm']:
        return None

    @abstractmethod
    def akcja(self, plansza, gra, szerokosc: int, wysokosc: int, keycode):
        pass

    @abstractmethod
    def kolizja(self, other: 'Organizm', plansza, szerokosc: int, wysokosc: int) -> 'Organizm':
        pass
