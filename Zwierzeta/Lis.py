import random
from Base.Zwierze import Zwierze


class Lis(Zwierze):
    DEFAULT_SILA = 3

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'L', "Lis", sila, 7, print_log, wiek)

    def _can_move_to(self, plansza, nx, ny):
        target = plansza[nx][ny]
        if isinstance(target, Zwierze):
            return target.sila < self.sila or self.czy_rozmnaza_sie(target)
        return True

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < wysokosc and 0 <= ny < szerokosc and self._can_move_to(plansza, nx, ny):
            self.x, self.y = nx, ny

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
