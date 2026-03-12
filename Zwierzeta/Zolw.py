import random
from Base.Zwierze import Zwierze


class Zolw(Zwierze):
    SHELL_THRESHOLD = 6
    DEFAULT_SILA = 2

    def __init__(self, print_log, x=0, y=0, sila=DEFAULT_SILA, wiek=0):
        super().__init__(x, y, 'Z', "Zolw", sila, 1, print_log, wiek)

    @property
    def has_special_defence(self) -> bool:
        return True

    def akcja(self, plansza, gra, szerokosc, wysokosc, keycode):
        # Turtle moves only 1 in 3 turns
        if random.randint(0, 2) != 0:
            return
        dx, dy = random.choice([(0, -1), (0, 1), (1, 0), (-1, 0)])
        new_x, new_y = self.x + dx, self.y + dy
        if 0 <= new_x < wysokosc and 0 <= new_y < szerokosc:
            self.x, self.y = new_x, new_y

    def kolizja_defend(self, attacker, plansza, szerokosc, wysokosc):
        if attacker.sila < self.SHELL_THRESHOLD:
            self.print_log(f"{self.imie} odpiera atak {attacker.imie}")
            self._zolwodparlatak = True
            return self
        return None

    def kolizja(self, other: Zwierze, plansza, szerokosc, wysokosc):
        return self.standard_kolizja(other, plansza, szerokosc, wysokosc)
