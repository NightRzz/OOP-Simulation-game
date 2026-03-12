from abc import ABC
from Base.Organizm import Organizm


class Zwierze(Organizm, ABC):
    MIN_WIEK_ROZMNAZANIA: int = 3

    def czy_rozmnaza_sie(self, other: 'Zwierze') -> bool:
        return (type(self) is type(other)
                and self.wiek >= self.MIN_WIEK_ROZMNAZANIA
                and other.wiek >= other.MIN_WIEK_ROZMNAZANIA)

    def standard_kolizja(self, other, plansza, szerokosc: int, wysokosc: int):
        if self.czy_rozmnaza_sie(other):
            self._rozmnoz = True
            return self
        if self.sila >= other.sila:
            self.print_log(f"{self.imie} wygrywa z {other.imie}")
            return self
        other.print_log(f"{other.imie} wygrywa z {self.imie}")
        return other
