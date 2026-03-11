import random
from Base.Zwierze import Zwierze


class Zolw(Zwierze):
    SHELL_THRESHOLD = 5
    DEFAULT_SILA = 2

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'Z', "Zolw", sila, 1, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        # Turtle moves only 1 in 3 turns
        if random.randint(0, 2) != 0:
            return
        dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
        new_x, new_y = self._x + dx, self._y + dy
        if 0 <= new_x < wysokosc and 0 <= new_y < szerokosc:
            self._x, self._y = new_x, new_y

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        if self.czy_rozmnaza_sie(other):
            self._rozmnoz = True
            return self

        if other.sila < self.SHELL_THRESHOLD:
            self.print_log(f"{self.imie} odpiera atak {other.imie}")
            self._zolwodparlatak = True
            return self

        if self.sila > other.sila:
            self.print_log(f"{self.imie} wygrywa z {other.imie}")
            return self

        self.print_log(f"{self.imie} przegrywa z {other.imie}")
        return other
