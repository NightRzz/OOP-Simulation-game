import random
from Base.Zwierze import Zwierze


class Antylopa(Zwierze):
    MOVE_DISTANCE = 2
    DEFAULT_SILA = 4

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'A', "Antylopa", sila, 4, print_log, wiek)

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        dx, dy = random.choice([(0, -self.MOVE_DISTANCE), (0, self.MOVE_DISTANCE),
                                 (self.MOVE_DISTANCE, 0), (-self.MOVE_DISTANCE, 0)])
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < wysokosc and 0 <= new_y < szerokosc:
            self.x, self.y = new_x, new_y

    def _try_escape(self, plansza, szerokosc, wysokosc, threat):
        dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
        ex, ey = self.x + dx, self.y + dy
        if 0 <= ex < wysokosc and 0 <= ey < szerokosc and plansza[ex][ey] is None:
            self.x, self.y = ex, ey
            plansza[ex][ey] = self
            self.print_log(f"{self.imie} ucieka przed {threat.imie} na pole {ex} {ey}")
            return True
        return False

    def kolizja(self, other, plansza, szerokosc, wysokosc):
        if isinstance(other, Zwierze) and not self.czy_rozmnaza_sie(other) and random.randint(0, 1) == 1:
            if self._try_escape(plansza, szerokosc, wysokosc, other):
                return other
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
