from abc import ABC, abstractmethod

from Base.Organizm import Organizm


class Zwierze(Organizm, ABC):

    def standard_kolizja(self, other, plansza, szerokosc: int, wysokosc: int):
        if self.czy_rozmnaza_sie(other):
            self._rozmnoz = True
            return self
        if other.sila >= self.sila:
            other.print_log(f"{other.imie} wygrywa z {self.imie}")
            return other
        self.print_log(f"{self.imie} wygrywa z {other.imie}")
        return self

    @abstractmethod
    def akcja(self, plansza, gra, szerokosc: int, wysokosc: int, keycode):
        pass

    @abstractmethod
    def kolizja(self, other: Organizm, plansza, szerokosc: int, wysokosc: int) -> Organizm:
        pass
