import random
from Base.Zwierze import Zwierze


class Wilk(Zwierze):
    DEFAULT_SILA = 9

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'W', "Wilk", sila, 5, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
        nx, ny = self._x + dx, self._y + dy
        if 0 <= nx < wysokosc and 0 <= ny < szerokosc:
            self._x, self._y = nx, ny

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
